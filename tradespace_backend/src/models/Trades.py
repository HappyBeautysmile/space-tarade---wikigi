class Trade:
    def __init__(self, buyer_id, seller_id, seller_item):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.seller_item = seller_item
        self.type = None

    @staticmethod
    def from_dict(source):
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        return Trade(buyer_id, seller_id, type, seller_item)

    def to_dict(self):
        return {
            'buyer_id': self.buyer_id,
            'seller_id': self.seller_id,
            'type': self.type,
            'seller_item': self.seller_item
        }

class BarterTrade(Trade):
    def __init__(self, buyer_id, seller_id, seller_item, buyer_item):
        super().__init__(self, buyer_id, seller_id, seller_item)
        self.buyer_item = buyer_item
        self.type = "BARTER"

    @staticmethod
    def from_dict(source):
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_item = source.get('buyer_item')
        return BarterTrade(buyer_id, seller_id, type, seller_item, buyer_item)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_item'] = self.buyer_item
        return dict_


class MoneyTrade(Trade):
    def __init__(self, buyer_id, seller_id, seller_item, buyer_price):
        super().__init__(self, buyer_id, seller_id, seller_item)
        self.buyer_price = buyer_price
        self.type = "MONEY"

    @staticmethod
    def from_dict(source):
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_price = source.get('buyer_price')
        return MoneyTrade(buyer_id, seller_id, type, seller_item, buyer_price)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_price'] = self.buyer_price
        return dict_

class BarterAndMoneyTrade(Trade):
    def __init__(self, buyer_id, seller_id, seller_item, buyer_item, buyer_price):
        super().__init__(self, buyer_id, seller_id, seller_item)
        self.buyer_item = buyer_item
        self.buyer_price = buyer_price
        self.type = "BARTER_AND_MONEY"

    @staticmethod
    def from_dict(source):
        buyer_id = source.get('buyer_id')
        seller_id = source.get('seller_id')
        type = source.get('type')
        seller_item = source.get('seller_item')
        buyer_price = source.get('buyer_price')
        buyer_item = source.get('buyer_item')
        return BarterAndMoneyTrade(buyer_id, seller_id, type, seller_item, buyer_price)

    def to_dict(self):
        dict_ = super().to_dict()
        dict_['buyer_item'] = self.buyer_item
        dict_['buyer_price'] = self.buyer_price
        return dict_