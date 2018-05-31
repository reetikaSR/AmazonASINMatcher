import Region
import Check_Url
import Check_pattern
import re


class Link:
    def __init__(self, link_string):
        self.__link_string = link_string
        self.__is_valid = False
        self.__market_place = ''
        self.__id = ''
        self.__id_type = ''

# region get methods
    def get_valid(self):
        return self.__is_valid

    def get_market_place(self):
        return self.__market_place

    def get_id(self):
        return self.__id

    def get_id_type(self):
        return self.__id_type
# end region


# region set methods
    def __set_is_valid(self):
        self.__is_valid = Check_pattern.check_url_pattern(self.__link_string) and Check_Url.check_url(self.__link_string)

    def __set_market_place(self):
        if self.__is_valid:
            try:
                link_list = self.__link_string.split('/')
                region_string = link_list[2]
                self.__market_place = Region.region_dict[region_string.split('.')[-1].upper()]
            except:
                self.__market_place = ''

    def __set_id(self):
        if self.__is_valid:
            try:
                link_list = self.__link_string.split('/')
                if 'dp' in link_list:
                    self.__id = link_list[link_list.index('dp') + 1]
                elif 'gp' in link_list:
                    self.__id = link_list[link_list.index('gp') + 2]
                else:
                    self.__id = link_list[link_list.index('d') + 3]
            except:
                self. __id = ''

    # depends on product id
    def __set_id_type(self):
        if self.__is_valid and self.__id != '':
            prod_id = self.__id
            try:
                if (len(prod_id) == 10 or len(prod_id) == 13) and re.match(r'[0-9]+', prod_id):
                    self.__id_type = "ISBN"
                elif len(prod_id) == 10 and re.match(r'[A-Z0-9]', prod_id):
                    self.__id_type = "ASIN"
            except:
                self.__id_type = ''

    def set_details(self):
        self.__set_is_valid()
        self.__set_market_place()
        self.__set_id()
        self.__set_id_type()
# end region
