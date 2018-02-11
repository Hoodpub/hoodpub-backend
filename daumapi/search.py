import requests

DAUM_API_URL = 'https://apis.daum.net/search/'


class Search():

    def __init__(self, category='book'):
        self.category = category

    def request(self, keyword=None):

        items = []

        payload = {
            "output": "json",
            "result": 20,
            "apikey": "9f68e425f40e190b407745eb855619262ce0b2cc",
            "searchType": "title"
        }

        if keyword:
            payload['q'] = keyword

        url = "%s/%s" % (DAUM_API_URL, self.category)
        res = requests.get(url, params=payload)

        for ele in res.json()['channel']['item']:
            items.append(ele)

        return dict(items=items)
