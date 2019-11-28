from flask import Blueprint, request, g
from firebase_admin import firestore
from fuzzywuzzy import fuzz

search_api = Blueprint('search_api', __name__)
ITEMS_COLLECTION = 'items'

@search_api.route('/', methods=['GET'])
def search():
  db = firestore.client()
  search_str = request.args.get('search')
  if search_str is None:
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
    max_ratio = max(title_ratio, desc_ratio, max(tag_ratios))
    print(max_ratio)
    print(item_dict['title'])
    if max_ratio > 80:
      if max_ratio in matched_items:
        matched_items[max_ratio].append(item_dict)
      else:
        matched_items[max_ratio] = [item_dict]
  matched_items_list = []
  for i in sorted(matched_items, reverse=True):
    matched_items_list += matched_items[i]
  return {'results': matched_items_list}
