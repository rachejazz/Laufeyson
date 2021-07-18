from setuptools import setup, find_packages

with open("README.md", 'r') as desc:
	read_desc = desc.read()

with open("VERSION", 'r') as v:
	read_ver = v.read()

setup(
	name = 'Laufeyson',
	version = read_ver,
	url = 'will be updated'
	creator = 'Divya Goswami',
	email = 'updated'
	description = read_desc,
	content_type = "text/markdown",
	packages = find_packages()
	install_requires = ['requests']
	classifiers = [
	"Programming Language :: Python :: 3",
	'License :: OSI Approved :: not yet',
	'Operating System :: POSIX :: Linux',
	'Environment :: Console',
	],
	python_requires = '>=3.8',
)
