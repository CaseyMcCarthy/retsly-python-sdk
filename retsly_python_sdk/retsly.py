from request import Request
from listingRequest import ListingRequest
BASE_URL = 'https://dev.rets.io/api/v1'

class Retsly:
  def __init__(self, token, vendor='test'):
    """
    Construct Retsly client

    Args:
      token (string):         access token
      vendor (string):        vendor ID

    """
    self.token = token
    self.vendor = vendor

  def getRequest(self, method, url, query):
    return Request(self, method, url, query)

  def getURL(self, resource):
    return '%s/%s/%s' % (BASE_URL, self.vendor, resource)

  def listings(self, query={}):
    return ListingRequest(self, query)