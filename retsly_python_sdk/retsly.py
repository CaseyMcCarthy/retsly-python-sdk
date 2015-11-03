import requests, json

class Retsly:
  variable = 100
  uri = 'https://dev.rets.io/api/v1/test/listings?access_token=70aa7c12bdb7b6a0bec5b11833c63ad5';
  r = requests.get(uri, verify=False);
  print r.status_code
  listings = r.json()['bundle']
  # for listing in listings:
    # print 'i: %s \n' % listing