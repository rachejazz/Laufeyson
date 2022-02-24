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
	buff = []
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
				if each.find(".") == -1:
					buff.append(each)
			return buff
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
		dirs = re.findall(r'Disallow: (/[\w\-_]*)', data)
		sitemap_crawl(self, q, data)
		if dirs:
			return list(set(dirs))
	return []

def cms(self, q):
	tech_list = list(filter(lambda x: x not in ['A', 'The'], wh.run(self, q)))
	if tech_list:
		self.output(f"CMS apears to be:")
		for each in tech_list[:3]:
			self.list_output(each)
	return []

def run(self, q):
	subdirs = []
	try:
		self.info(f"subdirectory: Scanning {q}...")
	except:
		self.error(f"subdirectory: Something went wrong. Please try again.")
	else:
		utils = ['cms', 'raw', 'robots']
		for each in utils:
			subdirs.extend(globals()[each](self, q))
		return subdirs
