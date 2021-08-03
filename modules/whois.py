import core as u
import re

meta = {
		'name': 'WhoIs Lookup',
		'author': 'Divya Goswami',
		'version': '0.0.1',
		'description': 'Issues a whois/rdap lookup on a domain',
		'options': 'uhh...',
		'example': 'whois -q <domain>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	values = engine.run(self, q, 0)
	if any(re.match(r'(\n|.)*unavailable', str(value)) for value in values):
		self.error("Not found in whois.")
		values = engine.run(self, q, 1)
		for i in values.strings:
			j = re.sub(r'(<a[^>]*>)', '', str(i))
			if not re.match(r'^\n\nAccess', j):
				self.list_output(j)
	else:
		entries = values[0].find_all('div', 'col-md-8')
		entries = values[0].find_all('div', 'col-md-8')
		if all(each.string == None or each.string == '\n' for each in entries):
			for i in values[4].div.div.pre.strings:
				self.list_output(str(i))
		else:
			for value in values[:2]:
				keys = value.find_all('div', 'col-md-4')
				entries = value.find_all('div', 'col-md-8')
				for i in range(3):
					self.output(f"{keys[i].string}")
					self.list_output(f"\t{entries[i].string}")
			entries = values[2].find_all('div', 'col-md-8')
			self.output("Nameservers:")
			for x in entries:
				if not x.a.string == None:
					self.list_output(x.a.string)
