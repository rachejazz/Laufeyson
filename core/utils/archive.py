from bs4 import BeautifulSoup
import re

def run(self, query):
	send_records = {}
	if not 'from' in query:
		query['from'] = ''
	if not 'to' in query:
		query['to'] = ''
	try:
		self.info(f"archive: Scanning {query['query']}...")
		url_timestamp = f"http://web.archive.org/cdx/search/cdx?url={query['query']}&from={query['from']}&to={query['to']}&limit=20"

		res = self.request(
				'GET',url_timestamp,
		)
		data = res.text
		if not data:
			raise
		records_timestamp = re.findall(r'/\s(\d*)\shttp', data)
		records_url = re.findall(rf"(http.*{query['query']})", data)[0]
	
		send_records = [f"http://web.archive.org/web/{x}/{records_url}/" for x in records_timestamp]
	except:
		self.error(f"archive: Something went wrong. Are the inputs valid?")
		return {}
	return send_records
