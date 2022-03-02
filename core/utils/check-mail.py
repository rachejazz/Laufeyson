from bs4 import BeautifulSoup
import re

def run(self, query, key):
	send_records = {}

	try:
		self.info(f"check-mail: Scanning {query}...")
		url = f"https://mailcheck.p.rapidapi.com/"
		q = {
			"disable_test_connection":"true",
			"domain":f"{query}"
		}
		headers = {
			'x-rapidapi-host': "mailcheck.p.rapidapi.com",
			'x-rapidapi-key': f"{key}"
		}
		res = self.request(
				'GET',url,
				headers=headers,
				params=q
		)
		send_records = res.text
		if 'API' in send_records:
			raise
	except:
		self.error(f"check-mail: {send_records}")
		return {}
	return send_records
