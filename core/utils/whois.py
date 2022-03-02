from bs4 import BeautifulSoup

def run(self, q, c): 
	try:
		urls = [f"https://who.is/whois/{q}", f"https://multirbl.valli.org/whois-lookup/{q}.html"]
		self.info(f"whois: Looking up {q} in {(lambda:'whois', lambda:'multirbl')[c]()}...")
		res = self.request('GET',urls[c])
		data = res.text
	except:
		self.error(f"whois: Something went wrong. Please try again.")
	else:
		send = BeautifulSoup(data, 'html.parser')
		if not c:
			data = send.find_all('div', 'queryResponseBody')
		else:
			data = send.find('div', 'whoisOutput')
	return data
