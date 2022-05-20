import core as u

meta = {
		'name': 'GeoIP Locator',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'extracts geolocation of the given IP or domain name',
		'options': [
				('query', '-q')
		],
		'example': 'geoip -q <IP>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	self.output(f"Snapshots of {q['query']} till date:")
	for each in value:
		self.list_output(f"{each}")
	self.output("For saving screenshots, use module: screen with the archive url.")
