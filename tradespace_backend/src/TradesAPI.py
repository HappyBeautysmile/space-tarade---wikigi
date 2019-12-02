from flask import Blueprint, request, g
from src.TokenAuthentication import auth
from firebase_admin import firestore
from itertools import chain

from src.ItemsAPI import get_item

from src.models.Item import Item
from src.models.Trades import Trade, BarterTrade, MoneyTrade, BarterAndMoneyTrade


trades_api = Blueprint('trades_api', __name__)
TRADES_COLLECTION = 'trades'
ITEMS_COLLECTION = 'items'

"""
Get a single trade with the given ID. The returned object is of type of given trade.
Responses: 200 - ok, 400 - bad request, 500 - internal error
"""
@trades_api.route('/<string:trade_id>', methods=['GET'])
@auth.login_required
def render_trade(trade_id):
    db = firestore.client()
    try:
        trade_dict = db.collection(TRADES_COLLECTION).document(trade_id).get().to_dict()
        trade_object = Trade.from_dict(trade_dict)
        if trade_object is None:
            return {'error': 'something is wrong, we are on it.'}, 500
    except Exception as inst:
        print (inst)
        return {'error': 'given trade not found'}, 404

    rendered_trade = trade_object.render(g.uid)
    if (rendered_trade is None):
        return {"error": "something went wrong on our end. please try again later."}, 500

    return rendered_trade, 200

def get_trade(trade_id):
    db = firestore.client()
    try:
        trade_dict = db.collection(TRADES_COLLECTION).document(trade_id).get().to_dict()
        trade_object = Trade.from_dict(trade_dict)
        if trade_object is None:
            return {'error': 'something is wrong, we are on it.'}, 500
    except Exception as inst:
        print (inst)
        return {'error': 'given trade not found'}, 404

    return trade_object.to_dict(), 200

"""
Called when the buyer clicks "request trade" on the user's item `itemId`.
Creates a trade with type "none" and basic info seller & buyer UIDs and
selling_item ID.
Response codes: 201 - successfully created, 400 - bad request, 500 - internal error
"""
@trades_api.route('/request_new', methods=['POST'])
@auth.login_required
def create_trade():
    try:
        selling_item_id = request.form['item_id']
    except:
        return {'error': 'missing required params'}, 400

    response, response_code = get_item(selling_item_id)
    if response_code != 200:
        return response, response_code

    item = Item.from_dict(response)
    if (item.owner_uid == g.uid):
        return {'error': 'cannot request trade with your own item'}, 400

    # TODO: add check to make sure user hasn't already requested trade with this item.

    db = firestore.client()

    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document()
    except:
        return {'error': 'could not create new trade, try again later'}, 500

    new_trade = Trade(new_trade_ref.id, g.uid, item.owner_uid, selling_item_id)

    try:
        new_trade_ref.set(new_trade.to_dict())
    except:
        return {'error': 'could not push new trade, try again later'}, 500

    return new_trade.to_dict(), 201

@trades_api.route('/<string:trade_id>/barter', methods=['PUT'])
@auth.login_required
def make_barter_trade(trade_id):
    # param validation
    try:
        buying_item_id = request.form['buyer_item']
    except:
        return {'error': 'missing required params'}, 400

    # make sure trade exists
    response, response_code = get_trade(trade_id)
    if response_code != 200:
        return response, response_code

    trade_dict = response

    # ensure provided item ID exsists
    response, response_code = get_item(buying_item_id)
    if response_code != 200:
        return response, response_code

    item_dict = response

    # ensure trade buyer owns given item
    if (item_dict['owner_uid'] != trade_dict['buyer_id']):
        return {'error': "this trade's buyer doesn't own the given item"}, 400

    trade_obj = Trade.from_dict(trade_dict)

    if (trade_obj.compute_status(g.uid) != 1):
        return {'error': "this trade's status is not 1 and hence cannot be updated with this method."}, 400

    trade_dict['buyer_item'] = buying_item_id
    new_trade_obj = BarterTrade.from_dict(trade_dict)

    db = firestore.client()

    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document(trade_id)
        new_trade_ref.update(new_trade_obj.to_dict())
    except:
        return {'error': 'could not update trade, try again later'}, 500

    return new_trade_obj.to_dict(), 200


@trades_api.route('/<string:trade_id>/money', methods=['PUT'])
@auth.login_required
def make_money_trade(trade_id):
    # param validation
    try:
        buyer_price = request.form['buyer_price']
    except:
        return {'error': 'missing required params'}, 400

    # make sure trade exists
    response, response_code = get_trade(trade_id)
    if response_code != 200:
        return response, response_code

    trade_dict = response
    trade_obj = Trade.from_dict(trade_dict)

    if (trade_obj.compute_status(g.uid) != 1):
        return {'error': "this trade's status is not 1 and hence cannot be updated with this method."}, 400

    trade_dict['buyer_price'] = buyer_price
    new_trade_obj = MoneyTrade.from_dict(trade_dict)

    db = firestore.client()

    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document(trade_id)
        new_trade_ref.update(new_trade_obj.to_dict())
    except:
        return {'error': 'could not update trade, try again later'}, 500

    return new_trade_obj.to_dict(), 200

@trades_api.route('/<string:trade_id>/barter_and_money', methods=['PUT'])
@auth.login_required
def make_barter_and_money_trade(trade_id):
    # param validation
    try:
        buying_item_id = request.form['buyer_item']
        buyer_price = request.form['buyer_price']
    except:
        return {'error': 'missing required params'}, 400

    # make sure trade exists
    response, response_code = get_trade(trade_id)
    if response_code != 200:
        return response, response_code

    trade_dict = response

    # ensure provided item ID exsists
    response, response_code = get_item(buying_item_id)
    if response_code != 200:
        return response, response_code

    item_dict = response

    # ensure trade buyer owns given item
    if (item_dict['owner_uid'] != trade_dict['buyer_id']):
        return {'error': "this trade's buyer doesn't own the given item"}, 400

    trade_obj = Trade.from_dict(trade_dict)
    # ensure trade's status allows it to be updated like this
    if (trade_obj.compute_status(g.uid) != 1):
        return {'error': "this trade's status is not 1 and hence cannot be updated with this method."}, 400

    trade_dict['buyer_item'] = buying_item_id
    trade_dict['buyer_price'] = buyer_price
    new_trade_obj = BarterAndMoneyTrade.from_dict(trade_dict)

    db = firestore.client()

    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document(trade_id)
        new_trade_ref.update(new_trade_obj.to_dict())
    except:
        return {'error': 'could not update trade, try again later'}, 500

    return new_trade_obj.to_dict(), 200

@trades_api.route('/<string:trade_id>/complete', methods=['POST'])
@auth.login_required
def complete_trade(trade_id):
    # make sure trade exists
    response, response_code = get_trade(trade_id)
    if response_code != 200:
        return response, response_code

    # ensure trade's status is valid for this method
    trade_dict = response
    trade_obj = Trade.from_dict(trade_dict)
    if (trade_obj.compute_status(g.uid) != 2):
        return {'error': "this trade is not ready to be completed."}, 400

    # ensure user is either buyer or seller for this trade
    if (trade_dict['seller_id'] != g.uid and trade_dict['buyer_id'] != g.uid):
        return {'error': "this user is not the seller for this trade and is unathorized to perform this action"}, 401

    trade_obj.mark_completed()

    db = firestore.client()
    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document(trade_id)
        new_trade_ref.update(trade_obj.to_dict())
    except:
        return {'error': 'could not update trade status, try again later'}, 500

    return trade_obj.to_dict(), 200

@trades_api.route('/<string:trade_id>/remove', methods=['POST'])
@auth.login_required
def remove_trade(trade_id):
    # make sure trade exists
    response, response_code = get_trade(trade_id)
    if response_code != 200:
        return response, response_code

    # ensure trade's status is valid for this method
    trade_dict = response
    trade_obj = Trade.from_dict(trade_dict)
    if (trade_obj.compute_status(g.uid) != 2):
        return {'error': "this trade is not ready to be cancelled."}, 400

    # ensure user is either buyer or seller for this trade
    if (trade_dict['seller_id'] != g.uid and trade_dict['buyer_id'] != g.uid):
        return {'error': "this user is not the seller for this trade and is unathorized to perform this action"}, 401

    trade_obj.mark_cancelled()

    db = firestore.client()
    try:
        new_trade_ref = db.collection(TRADES_COLLECTION).document(trade_id)
        new_trade_ref.update(trade_obj.to_dict())
    except:
        return {'error': 'could not update trade status, try again later'}, 500

    return trade_obj.to_dict(), 200

@trades_api.route('/', methods=['GET'])
@auth.login_required
def get_trades():
    db = firestore.client()

    try:
        trades_collection = db.collection(TRADES_COLLECTION)
        buyer_trade_docs = trades_collection.where('buyer_id', '==', g.uid).stream()
        seller_trade_docs = trades_collection.where('seller_id', '==', g.uid).stream()
    except:
        return {'error': 'could not get trades for given user, try again later'}, 500

    all_trade_docs = chain(buyer_trade_docs, seller_trade_docs)

    all_trades = []
    for trade_doc in all_trade_docs:
        trade_dict = trade_doc.to_dict()
        trade_obj = Trade.from_dict(trade_dict)
        all_trades.append(trade_obj.render(g.uid))

    return {'trades': all_trades}, 200