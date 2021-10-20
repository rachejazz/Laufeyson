from bs4 import BeautifulSoup
import re

def run(self, q):
	stack_list = []
	try:
		self.info(f"whichcms: Scanning {q}...")
		url = f"https://w3techs.com/sites/info/{q}"
		data = {'add_site': "+Crawl+now!+"}
		res = self.request(
				'POST',
				url = url,
				data = data,
				)
		data = res.text
	except:
		self.error(f"whichcms: Something went wrong. Please try again.")
	else:
		send = BeautifulSoup(data, 'html.parser')
		if re.match(r'(\n|.)*Possibly this is not a proper url.(\n|.)*', data):
			self.error(f"whichcms: {q} may not be a proper url.")
			return False
		data = send.find('td', class_='tech_main')
		new = data.p.p.p.p
		tech_stack = new.find_all('div', class_='si_tech_np')
		for each in tech_stack:
			try:
				stack_list.append(each.p.string.split(' ')[0])
			except:
				pass
		if not stack_list:
			self.error(f"whichcms: No Technologies found for {q}. Is it accessible?")
			return False
		else:
			return stack_list
