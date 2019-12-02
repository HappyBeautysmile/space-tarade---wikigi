from src.UsersAPI import get_user_with_id
from src.ItemsAPI import get_item

class Trade:
    def __init__(self, id, buyer_id, seller_id, seller_item):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.seller_item = seller_item
        self.id = id
        self.type = None
        self.status = "PENDING"

    @staticmethod
    def from_dict(source):
        type = source.get('type')
        if (type == None):
            id = source.get('id')
            buyer_id = source.get('buyer_id')
            seller_id = source.get('seller_id')
            seller_item = source.get('seller_item')
            return Trade(id, buyer_id, seller_id, seller_item)
        elif type == "BARTER":
            return BarterTrade.from_dict(source)
        elif type == "MONEY":
            return MoneyTrade.from_dict(source)
        elif type == "BARTER_AND_MONEY":
            return BarterAndMoneyTrade.from_dict(source)
        else:
            return None

    def to_dict(self):
        return {
            'id': self.id,
            'buyer_id': self.buyer_id,
            'seller_id': self.seller_id,
            'type': self.type,
            'seller_item': self.seller_item,
            'status': self.status
        }

    def compute_status(self, curr_uid):
        if (self.status ==  "PENDING"):
            if self.type is None:
                if self.buyer_id == curr_uid:
                    return 0
                elif self.seller_id == curr_uid:
                    return 1
            else:
                return 2
        elif (self.status == "COMPLETED"):
            return 3
        elif (self.status == "CANCELLED"):
            return 4
        else:
            return -1 # undefined

    def mark_completed(self):
        self.status = "COMPLETED"

    def mark_cancelled(self):
        self.status = "CANCELLED"

    def render_for_buyer(self, rendered_trade):
        response, response_code = get_item(self.seller_item)
        if (response_code != 200):
            return False
        rendered_trade['their_item'] = response
        return True

    def render_for_seller(self, rendered_trade):
        response, response_code = get_item(self.seller_item)
        if (response_code != 200):
            return False
        rendered_trade['your_item'] = response
        return True

    def render(self, curr_uid):
        rendered_trade = {
            'trade_id': self.id,
            'status': self.compute_status(curr_uid),
            'type': self.type
        }

        if curr_uid == self.buyer_id:
            other_user_id = self.seller_id
            rendered_trade['requesting_user_is'] = "BUYER"
            did_render = self.render_for_buyer(rendered_trade)
        elif curr_uid == self.seller_id:
            other_user_id = self.buyer_id
            rendered_trade['requesting_user_is'] = "SELLER"
            did_render = self.render_for_seller(rendered_trade)
        else:
            return None

        if (not did_render):
            return None

        other_user_dict, response_code = get_user_with_id(other_user_id)
        rendered_trade['other_user'] = other_user_dict.get_json()

        return rendered_trade


class BarterTrade(Trade):
    def __init__(self, id, buyer_id, seller_id, seller_item, buyer_item):
        super().__init__(id, buyer_id, seller_id, seller_item)
        self.buyer_item = buyer_item
        self.type = "BARTER"

    @staticmethod
    def from_dict(source):
        id = source.get('id')
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_item = source.get('buyer_item')
        return BarterTrade(id, buyer_id, seller_id, seller_item, buyer_item)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_item'] = self.buyer_item
        return dict_

    def render_for_buyer(self, rendered_trade):
        result = super().render_for_buyer(rendered_trade)
        if not result: return False # if super method failed
        response, response_code = get_item(self.buyer_item)
        if (response_code != 200):
            return False
        rendered_trade['your_item'] = response
        return True

    def render_for_seller(self, rendered_trade):
        result = super().render_for_seller(rendered_trade)
        if not result: return False # if super method failed
        response, response_code = get_item(self.buyer_item)
        if (response_code != 200):
            return False
        rendered_trade['their_item'] = response
        return True


class MoneyTrade(Trade):
    def __init__(self, id, buyer_id, seller_id, seller_item, buyer_price):
        super().__init__(id, buyer_id, seller_id, seller_item)
        self.buyer_price = buyer_price
        self.type = "MONEY"

    @staticmethod
    def from_dict(source):
        id = source.get('id')
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_price = source.get('buyer_price')
        return MoneyTrade(id, buyer_id, seller_id, seller_item, buyer_price)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_price'] = self.buyer_price
        return dict_

    def render_for_buyer(self, rendered_trade):
        result = super().render_for_buyer(rendered_trade)
        if not result: return False # if super method failed
        rendered_trade['your_price'] = self.buyer_price
        return True

    def render_for_seller(self, rendered_trade):
        result = super().render_for_seller(rendered_trade)
        if not result: return False # if super method failed
        rendered_trade['their_price'] = self.buyer_price
        return True

class BarterAndMoneyTrade(Trade):
    def __init__(self, id, buyer_id, seller_id, seller_item, buyer_item, buyer_price):
        super().__init__(id, buyer_id, seller_id, seller_item)
        self.buyer_item = buyer_item
        self.buyer_price = buyer_price
        self.type = "BARTER_AND_MONEY"

    @staticmethod
    def from_dict(source):
        id = source.get('id')
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_price = source.get('buyer_price')
        buyer_item = source.get('buyer_item')
        return BarterAndMoneyTrade(id, buyer_id, seller_id, seller_item, buyer_price)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_item'] = self.buyer_item
        dict_['buyer_price'] = self.buyer_price
        return dict_

    def render_for_buyer(self, rendered_trade):
        result = super().render_for_buyer(rendered_trade)
        if not result: return False # if super method failed
        response, response_code = get_item(self.buyer_item)
        if (response_code != 200):
            return False
        rendered_trade['your_item'] = response
        rendered_trade['your_price'] = self.buyer_price
        return True

    def render_for_seller(self, rendered_trade):
        result = super().render_for_seller(rendered_trade)
        if not result: return False # if super method failed
        response, response_code = get_item(self.buyer_item)
        if (response_code != 200):
            return False
        rendered_trade['their_item'] = response
        rendered_trade['their_price'] = self.buyer_price
        return True