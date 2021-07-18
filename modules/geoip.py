import core as u

meta = {
		'name': 'GeoIP Locator',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'geoIP module',
		'options': 'uhh...',
		'example': 'geoip -q <IP>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	for each in value:
		self.output(f"{each}: {value[each]}")
