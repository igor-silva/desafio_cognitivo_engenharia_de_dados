import requests

header = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAAxIigEAAAAAo09Wig9u4UpL9fBwB3Kr1t7mREQ%3DQyzxC8WOFnRlqk62UXPzpd0VXlA6QyCjEenddAzRvh5UzcFxTO'}
url = 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=book'

resp = requests.request("GET",
    url=url,
    headers=header
).text
print(resp)
