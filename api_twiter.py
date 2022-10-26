import requests

'''
============================================================================
Class: APITwiter
Description: Responsável por gerar integração com API do Twiter,
            retornar dados com busca dinãmica.
Params: args=term
Autor: Igor Silva
Date: 25/10/2022
Updates: 
===============================================================================
'''
class APITwiter:

    def __init__(self, args):
        self.bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAxIigEAAAAAo09Wig9u4UpL9fBwB3Kr1t7mREQ%3DQyzxC8WOFnRlqk62UXPzpd0VXlA6QyCjEenddAzRvh5UzcFxTO'
        self.search_url = "https://api.twitter.com/2/spaces/search"
        self.search_term = args  # Replace this value with your search term
        self.query_params = {'query': self.search_term, 'space.fields': 'title,created_at', 'expansions': 'creator_id'}

    def create_headers(self, args=None):
        headers = {
            "Authorization": "Bearer {}".format(self.bearer_token),
            "User-Agent": "v2SpacesSearchPython"
        }
        return headers

    def connect_to_endpoint(self):
        response = requests.request("GET", self.search_url, headers=self.create_headers(), params=self.query_params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main(self):
        headers = self.create_headers(self.bearer_token)
        json_response = self.connect_to_endpoint()
        #return json.dumps(json_response, indent=4, sort_keys=True)

        return json_response


if __name__ == '__main__':
    """api_music = APITwiter('Book')
    count_music = api_music.main()
    title = [x['title'] for x in count_music['data']]
    print(len(title))"""
