import core as u
import re

meta = {
		'name': 'DNS Recorder',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'extracts dns records of the given domain name',
		'options': 'uhh...',
		'example': 'dns_record -q <domain>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	for each in value:
		self.output(each)
		headers = (' '*10).join(value[each][0])
		self.list_output(headers.ljust(20))
		for entries in value[each][1]:
			elements = ''
			for x in entries.contents:
				if not x == '\n':
					elements += x.string + '\t'
			self.list_output(elements.ljust(20))
