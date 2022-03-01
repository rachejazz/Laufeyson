import core as u

meta = {
		'name': 'Subdirectory Lister',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'List subdirectories of the query domain given',
		'options': [
				('query', '-q')
		],
		'example': 'subdirectory -q <domain>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	self.output(f"Subdirectories found in {q}:")
	for each in value:
		self.list_output(each)
