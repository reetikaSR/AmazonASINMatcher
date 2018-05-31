import urllib2


def check_url(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        response = opener.open(url)
    except urllib2.URLError as e:
        response = e
    if response.code == 200:
        return True
    return False
