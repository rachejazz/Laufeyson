from bs4 import BeautifulSoup
import re

def run(self, q):
	send_record = ''
	url = f'https://safeweb.norton.com/report/show?url={q}'
	self.info('norton: Scanning domain...')
	try:
		req = self.request('GET',url)
	except Exception as e:
		self.error(f"norton: Norton could not scan! due to {e}")
	else:
		e_reg = 'is a known dangerous web page'
		s_reg = 'found no issues with'
		if e_reg in req.text:
			send_record = f"norton: {q} {e_reg}"
		elif s_reg in req.text:
			send_record = f"norton: {s_reg} {q}"
		else:
			send_record = f"norton: {q} not yet rated as dangerous."
	return send_record
