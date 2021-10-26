import re
from . import whichcms as wh

def sitemap_crawl(self, q, data = ""):
	sm_reg_rob = re.findall(r'\n*Sitemap: (.*)', data)
	sm_reg_raw = re.findall(r'/sitemaps?\.\w+', data)
	if sm_reg_rob:
		self.info(f"Sitemap found: {sm_reg_rob[0]}")
		return True
	elif sm_reg_raw:
		self.info(f"Sitemap found: https://{q}{sm_reg_raw[0]}")
		return True
	else:
		return False

def raw(self, q):
	try:
		res = self.request('GET', q)
		data = res.text
	except:
		self.error(f"subdirectory: Something went wrong. Please try again.")
	else:
		sitemap_crawl(self, q, data)
		dir_reg = re.findall(r'href=\"(/[\w\-.]+)', data)
		if dir_reg:
			dir_reg = list(set(dir_reg))
			for each in dir_reg:
				print(f"Checking for {each}")
				if "." in each:
					print(each)
					dir_reg.remove(each)
				else:
					print(f"Not in {each}")
			return dir_reg
		else:
			return []

def robots(self, q):
	self.info(f"subdirectory: Searching for robots.txt...")
	url = f"{q}/robots.txt"
	res = self.request('GET', url)
	if res.status_code == 404:
		self.error("No robots.txt found.")
	else:
		data = res.text
#		dirs = re.findall(r'(?<!(:/))(/[\w\.-]+)/*', data)
		dirs = re.findall(r'Disallow: (/[\w\-_]*)', data)
		sitemap_crawl(self, q, data)
		if dirs:
			return list(set(dirs))
		else:
			return []

def cms(self, q):
	tech_list = list(filter(lambda x: x not in ['A', 'The'], wh.run(self, q)))
	return tech_list

def cert(self, q):
	pass

def js(self, q):
	pass

def run(self, q):
	subdirs = []
	try:
		self.info(f"subdirectory: Scanning {q}...")
	except:
		self.error(f"subdirectory: Something went wrong. Please try again.")
	else:
#		utils = ['cms', 'robots', 'raw', 'cert', 'js']
		utils = ['raw']
#		subdirs.extend(list(set(robots(self, q))))
#		print(subdirs)
		for each in utils:
			self.list_output(globals()[each](self, q))
