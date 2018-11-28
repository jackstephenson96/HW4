import requests
import json
api_key = 's7EZWPipghdNLp7IPqHgHJJFfCFwlKCp'
def get_gifs_from_giphy(search_string):
	""" Returns data from Giphy API with up to 5 gifs corresponding to the search input"""
	baseurl = "https://api.giphy.com/v1/gifs/search"
	gifs = []
	params = {}
	params['api_key'] = api_key
	params['q'] = search_string
	params['limit'] = 5
	r = requests.get(baseurl, params)
	for gif in json.loads(r.text)['data']:
		gifs.append(gif)
	return gifs

print(get_gifs_from_giphy("hello"))
