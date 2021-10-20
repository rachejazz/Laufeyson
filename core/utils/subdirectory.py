import re
from . import whichcms as wh

def sitemap_crawl(self, q):
	pass

def robots(self, q):
	self.info(f"subdirectory: Searching for robots.txt...")
	url = f"{q}/robots.txt"
	res = self.request('HEAD', url)
	if res.status_code == 404:
		print(res.url)
		self.error("No robots.txt found.")
	else:
		res = self.request('GET', url)
		data = res.text
		rob_dirs = re.findall(r'(?<!(:/))(/[\w\.-]+)/*', data)
		print(rob_dirs)

def cert(self, q):
	pass

def js(self, q):
	pass

def run(self, q):
	try:
		self.info(f"subdirectory: Scanning {q}...")
#		url = f""
#		res = self.request('GET',url)
#		data = res.text
#		data_json = res.json()
	except:
		self.error(f"subdirectory: Something went wrong. Please try again.")
	else:
		tech_list = list(filter(lambda x: x not in ['A', 'The'], wh.run(self, q)))
		print(tech_list)
		robots(self, q)
#	if tech_list:
#		return tech_list
