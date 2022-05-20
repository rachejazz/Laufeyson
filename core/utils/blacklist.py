#from bs4 import BeautifulSoup
import re

def run(self, query):
	send_records = {}
	with open("dschit.com.html") as I:
		data = I.read()

#	try:
	self.info(f"blacklist: Scanning {query}...")
#		url = f"https://mailcheck.p.rapidapi.com/"
#		q = {
#			"disable_test_connection":"true",
#			"domain":f"{query}"
#		}
#		headers = {
#			'x-rapidapi-host': "mailcheck.p.rapidapi.com",
#			'x-rapidapi-key': f"{key}"
#		}
#		res = self.request(
#				'GET',url,
#				headers=headers,
#				params=q
#		)
#		send_records = res.text
	keys=re.findall(r'<th.*">(.*)</th>', data)
#	values=re.findall(r'<tr>.*</td>(.*)</tr>', data, re.DOTALL)
	for name in keys:
		list_type = name.replace(' ', '').replace('Summary', '')
		value = re.findall(rf'.*{list_type}.*', data)
		send_records.update({name:value})
#	except:
#		self.error(f"blacklist: {query}")
#		return {}
	return send_records
