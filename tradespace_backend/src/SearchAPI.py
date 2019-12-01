from flask import Blueprint, request, g, jsonify
from firebase_admin import firestore
from fuzzywuzzy import fuzz
from src.TokenAuthentication import auth

search_api = Blueprint('search_api', __name__)
ITEMS_COLLECTION = 'items'

@search_api.route('/<string:search_text>', methods=['GET'])
@auth.login_required
def search(search_text):
  #esear to sent get
  db = firestore.client()
  print(str(request))
  search_str = search_text
  if search_str is None:
    print('No search string')
    return {'error': 'must pass a search string'}, 401
  items = db.collection(ITEMS_COLLECTION).stream()
  matched_items = {}
  for item in items:
    item_dict = item.to_dict()
    title_ratio = fuzz.ratio(search_str, item_dict['title'])
    desc_ratio = fuzz.ratio(search_str, item_dict['description'])
    tag_ratios = []
    for tag in item_dict['tags']:
      tag_ratios.append(fuzz.ratio(search_str, tag))
    #ValueError: max() arg is an empty sequence
    #when try to search 'shoes', the tag_ratios was equal to [] what would cause a crash so added a check
    if tag_ratios == []:
        tag_ratios = [0]
    max_ratio = max(title_ratio, desc_ratio, max(tag_ratios))
    if max_ratio > 80:
      if max_ratio in matched_items:
        matched_items[max_ratio].append(item_dict)
      else:
        matched_items[max_ratio] = [item_dict]
  matched_items_list = []
  for i in sorted(matched_items, reverse=True):
    matched_items_list += matched_items[i]
  print(matched_items_list)
  if len(matched_items_list) < 1:
    matched_items_list = []
  #easear to return json, plus the empty list case
  return jsonify(data=matched_items_list)
