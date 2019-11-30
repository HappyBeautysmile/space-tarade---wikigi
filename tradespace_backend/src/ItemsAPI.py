from flask import Blueprint, request, g
from src.TokenAuthentication import auth
from firebase_admin import firestore
from src.models.Item import Item

items_api = Blueprint('items_api', __name__)
ITEMS_COLLECTION = 'items'

@items_api.route('/', methods=['POST'])
@auth.login_required
def create_item():
  try:
    title = request.form['title']
    location = request.form['location']
    description = request.form['description']
    tags = request.form.getlist('tags')
  except:
    return {'error': 'missing required params'}, 400

  photo_url = request.form.get('photo_url')
  owner_uid = g.uid

  item = Item(title=title, location=location, description=description, tags=tags, photo_url=photo_url, owner_uid=owner_uid)
  db = firestore.client()
  try:
    db.collection(ITEMS_COLLECTION).add(item.to_dict())
  except:
    return {'error': 'something went wrong, please try again later'}, 500

  return item.to_dict(), 201

@items_api.route('/<string:item_id>', methods=['GET'])
@auth.login_required
def get_item(item_id):
  db = firestore.client()
  try:
    item_dict = db.collection(ITEMS_COLLECTION).document(item_id).get().to_dict()
    item = Item.from_dict(item_dict)
    item_info = item.to_dict()
    item_info['item_id'] = item_id
  except:
    return {'error': 'item not found'}, 404
  return item_info, 200

@items_api.route('/<string:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
  response, response_code = get_item(item_id)
  if response_code != 200:
    return response, response_code

  item = Item.from_dict(response)
  if item.owner_uid != g.uid:
    return {'error': 'user does not own this item'}, 401

  title = request.form.get('title')
  location = request.form.get('location')
  description = request.form.get('description')
  tags = request.form.getlist('tags')
  photo_url = request.form.get('photo_url')

  item.update(title=title, location=location, description=description, tags=tags, photo_url=photo_url)
  db = firestore.client()
  try:
    db.collection(ITEMS_COLLECTION).document(item_id).update(item.to_dict())
  except:
    return {'error': 'something went wrong, please try again later'}, 500

  return item.to_dict(), 200

@items_api.route('/<string:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
  response, response_code = get_item(item_id)
  if response_code != 200:
    return response, response_code

  item = Item.from_dict(response)
  if item.owner_uid != g.uid:
    return {'error': 'user does not own this item'}, 401

  db = firestore.client()
  try:
    db.collection(ITEMS_COLLECTION).document(item_id).delete()
  except:
    return {'error': 'something went wrong, please try again later'}, 500

  return item.to_dict(), 200

#### GET ITEM COLLECTION

@items_api.route('/', methods=['GET'])
@auth.login_required
def get_items():
  db = firestore.client()
  target_uid = request.args.get('user_id')
  if target_uid is None:
    target_uid = g.uid
  else:
    # TODO: verify that uid passed is valid
    pass

  items = db.collection(ITEMS_COLLECTION).where("owner_uid", "==", target_uid).stream()

  result = {}
  for item in items:
    item_info = item.to_dict()
    item_info['item_id'] = item_id
    result[item.id] = item_info

  return result, 200
