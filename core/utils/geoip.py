import json

def run(self, q):
	try:
		self.info(f"geoip: Scanning {q}...")
		url = f"http://ip-api.com/json/{q}?fields=status,continent,country,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query"
		res = self.request('GET',url)
		data = res.text
		data_json = res.json()
	except:
		self.error(f"geoip: Something went wrong. Please try again.")
	else:
		self.info(json.dumps(data_json['status'], indent = 4))
		del data_json['status']
	return data_json
