AmazonASINMatcher is used to get the details of the product using the product links on Amazon.
It validates if the url entered by the user actually points to a product on Amazon. 
It searches for all the market places like India, America, Europe, China etc
You can obtain the ASIN/ISBN of the product by just using the product link.
It is written in python2.7


Installation:
pip install AmazonASINMatcher

Usage:
import AmazonASINMatcher

AmazonASINMatcher.url_matcher(product_link) -- returns the object with all the details like validity of the link, market place, ASIN/ISBN etc
AmazonASINMatcher.is_valid_link(product_link) -- returns True if the amazon product link is valid
AmazonASINMatcher.get_market_place(product_link) -- returns the market place of the product link, if invalid url, return blank value
AmazonASINMatcher.get_id(product_link) -- returns the ASIN/ISBN of the url, if invalid url, return blank value
AmazonASINMatcher.get_id_type(product_link) -- returns the id type (e.g. "ISBN" or "ASIN") of the url, if invalid url, return blank value