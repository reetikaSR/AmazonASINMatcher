__author__ = 'reetikasingla'


class LinkObject:
    def __init__(self, link):
        self.is_valid = link.get_valid()
        self.ID = link.get_id()
        self.ID_type = link.get_id_type()
        self.market_place = link.get_market_place()
