from bs4 import BeautifulSoup
import re

def run(self, q):
	send_records = {}
	
	try:
		query = q.split('_')[0]
		api_key = q.split('_')[1]
	except:
		self.error(f"check-mail: Cannot proceed scanning, did you provide an API key?")
		return send_records
	
	try:
		self.info(f"check-mail: Scanning {q}...")
		url = f"https://mailcheck.p.rapidapi.com/"
		q = {
			"disable_test_connection":"true",
			"domain":f"{query}"
		}
		headers = {
			'x-rapidapi-host': "mailcheck.p.rapidapi.com",
			'x-rapidapi-key': f"{api_key}"
		}
		res = self.request(
				'GET',url,
				headers=headers,
				params=q
		)
		send_records = res.json
	except:
		self.error(f"check-mail: Something went wrong. Please try again.")
	return send_records
