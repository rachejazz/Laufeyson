from bs4 import BeautifulSoup

def run(self, q): 
	try:
		self.info(f"whois: Looking up {q}...")
		urls = [f"https://who.is/whois/{q}"]
		for url in urls:
			res = self.request('GET',url)
			data = res.text
	except:
		self.error(f"whois: Something went wrong. Please try again.")
	else:
		send = BeautifulSoup(data, 'html.parser')
		data = send.find_all('div', 'queryResponseBody')
	return data
