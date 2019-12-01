from flask import Blueprint, request, g
from src.TokenAuthentication import auth
from firebase_admin import firestore

from src.ItemsAPI import get_item

from src.models.Item import Item
from src.models.Trades import Trade, BarterTrade, MoneyTrade, BarterAndMoneyTrade


trades_api = Blueprint('trades_api', __name__)
TRADES_COLLECTION = 'trades'
ITEMS_COLLECTION = 'items'

@trades_api.route('/', methods=['GET'])
def get_trade():
  return {'trades': 'api'}, 200
