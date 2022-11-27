import core as u

meta = {
		'name': 'Screenshotty',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'extracts of a given domain page',
		'options': [
				('query', '-q')
		],
		'example': 'screen -q <domain/url>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")

def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	self.output(f"Screenshot of {q['query']} was saved at data/screenshots/")
