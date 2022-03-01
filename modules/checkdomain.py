import core as u
import re

meta = {
		'name': 'Domain Checker',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'Checks for domain reputation. (API required)',
		'options': [
				('query', '-q'),
				('key', '-k')
		],
		'example': 'checkdomain -q <domain> -k <API_KEY>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engines = ['check-mail', 'norton']
#	key = self.options['example']
#	print(self.key)
	for each in engines:
		engine = getattr(u, each)
		value = engine.run(self, q)
		self.output(value)
