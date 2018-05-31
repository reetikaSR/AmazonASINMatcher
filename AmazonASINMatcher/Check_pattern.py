import re


def check_url_pattern(url):
    pattern = re.compile(r'^(?:http|ftp)s?://'
                         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)?(?:amazon\.))'
                         r'(?:\S+(?:/dp/|/gp/|/d/)\S+)$',
                         re.IGNORECASE)
    if re.match(pattern, url):
        return True
    return False
