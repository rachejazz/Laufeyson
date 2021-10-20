import core as u

meta = {
		'name': 'Subdirectory Lister',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'List subdirectories of the query domain given',
		'options': 'uhh...',
		'example': 'subdirectory -q <domain>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
#	value = engine.run(self, q)
	engine.run(self, q)
#	if value:
#		self.output(f"Top Technologies Used in {q}:")
#		for each in value:
#			self.list_output(each)
#	for each in value:
#		self.output(each.title())
#		self.list_output(f"\t{value[each]}")
