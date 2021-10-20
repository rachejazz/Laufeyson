from bs4 import BeautifulSoup
import re

def run(self, q):
	records = []
	send_records = {}
	try:
		self.info(f"dns_record: Scanning {q}...")
		url = f"https://dns-lookup.com/{q}"
		res = self.request('GET',url)
		data = res.text
	except:
		self.error(f"dns_record: Something went wrong. Please try again.")
	else:
#		if re.match(r'(\n|.)*No(\n|.)*DNS(\n|.)*', data):
		if re.match(r'(\n|.)*No[\n\s]+DNS(\n|.)*', data):
			self.error(f"No DNS records found for {q}")
		else:
			send = BeautifulSoup(data, 'html.parser')
			data = send.find_all('table', 'table outer')
			records.extend(each.contents for each in data)
			for i in records:
				each_record = []
				r_entries_headers_list = []
				r_entries_list = []
				r_type = i[1].contents[1].find('th', 'type').string
				r_entries_headers = i[1].tr.find('th', 'type').find_next_siblings('th')
				r_entries = i[1].tr.find_next_siblings()
				for j in r_entries_headers:
					r_entries_headers_list.append(j.string)
				for j in r_entries:
					r_entries_list.append(j)
				each_record = {r_type : [r_entries_headers_list, r_entries_list]}
				send_records.update(each_record)
	return send_records
