import core as u

meta = {
		'name': 'Web Archive Finder',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'extracts old snapshots from webarchive of the given url or domain name',
		'options': [
				('query', '-q'),
				('from', '-f'),
				('to', '-t')
		],
		'example': 'archive -q <url> -f 2019 -t 2022'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	print(q)
	engine = getattr(u, util)
	value = engine.run(self, q)
	self.output(f"Snapshots of {q['query']} till date:")
	for each in value:
		self.list_output(f"{each}")
	self.output("For saving screenshots, use module: screen with the archive url.")
