from AmazonASINMatcher import Link
from AmazonASINMatcher import Link_object


# wrapper methods
def url_matcher(link_string):
    if not (link_string.startswith("http://") or link_string.startswith("https://")):
        link_string = "https://" + link_string
    new_link = Link.Link(link_string)
    new_link.set_details()
    return Link_object.LinkObject(new_link)


def is_valid_link(link_string):
    new_link = url_matcher(link_string)
    return new_link.is_valid


def get_market_place(link_string):
    new_link = url_matcher(link_string)
    return new_link.market_place


def get_id(link_string):
    new_link = url_matcher(link_string)
    return new_link.ID


def get_id_type(link_string):
    new_link = url_matcher(link_string)
    return new_link.ID_type
