import os
import sys
import requests
import argparse
from core.rootdir import ROOT_DIR
from core.banner import BANNER,INFO
import modules as m
import core.utils as u

####
# INIT FACTORS
####

__author__ = 'Divya Goswami (@rachejazz)'
with open("VERSION", 'r') as v:
	__version__ = v.read().strip('\n')

WELCOME = f"[ {__version__}, {__author__} ]"

class Checkfuncs:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

class Colors(object):
	R = '\033[31m'
	G = '\033[32m'
	B = '\033[34m'
	N = '\033[m'
	Y = '\033[33m'

class Laufeyson(object):

	def __init__(self, config=False, banner=True):
		self.app_path = ROOT_DIR
		self.core_path = os.path.join(self.app_path, 'core')
		self.mod_path = os.path.join(self.app_path, 'modules')

	def init_load_options(self, argv):
		parser = argparse.ArgumentParser(description=WELCOME)
		parser.add_argument('-B', '--nobanner', help='run without banner', dest='nobanner', action='store_true')
		parser.add_argument('-m', '--module',  help='run a module', dest='module', action='store')
		mod_name = argv[2]
		arg_ops = [x if x.startswith('-') else '' for x in argv]

		with Checkfuncs():
			is_found = self.search_modules(mod_name)

		if is_found:
			mod_ops = self.load_modules()[mod_name]['options']
			for each in mod_ops:
				if each[1] in arg_ops:
					try:
						parser.add_argument(each[1], f'--{each[0]}', dest=each[0], action='store')
					except argparse.ArgumentError as e:
						self.error(f"ModuleException: {str(e)}")
						return False
		args = parser.parse_args()
		return vars(args)


####
# METHODS
####

	def show_about(self):
		with open("README.md", 'r') as f:
			lines = f.readlines()
			for each in lines:
				if each.startswith('#') or each.isupper():
					self.output(each.strip())
				elif each == '\n':
					continue
				else:
					self.list_output(each.strip())

	def request(self, method, url, **kwargs):
		if '://' not in url:
			url = f'https://{url}'
		kwargs['timeout'] = kwargs.get('timeout')
		headers = kwargs.get('headers') or {}
		kwargs['verify'] = False
		requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
		resp = getattr(requests, method.lower())(url, **kwargs)
		return resp

####
# PRETTY PRINTS
####
	def welcome(self, nobanner=False):
		self.print_message(f"{Colors.G}{BANNER}", nobanner)
		self.print_message(f"{Colors.Y}{WELCOME}", nobanner)
		self.print_message(f"{Colors.G}{INFO}", nobanner)


	def print_message(self, message, bool_val):
		if not bool_val:
			print(message)
		else:
			pass
	
	def output(self, string):
		print(f"{Colors.B}[*]{Colors.Y}{string}")
	
	def error(self, string):
		print(f"{Colors.R}[!]{string}")

	def info(self, string):
		print(f"{Colors.G}[√]{string}")

	def list_output(self, string):
		print(f"{Colors.B}>  {Colors.N}{string}")

####
# ABOUT MODULES
####
	def load_modules(self):
		files = [f.split('.py')[0] for f in os.listdir(self.mod_path)if not f.startswith('__')]
		file_info = {}
		for each in files:
			mod = getattr(m, each).meta
			file_info.update({each: mod})
		return file_info

	def run_modules(self, name, q, banner_bool):
#		try:
		with Checkfuncs():
			is_found = self.search_modules(name)

		if is_found:
			engine = getattr(m, name)
			engine.mod_run(self, name, q)
#		except:
#			self.error(f"Something went wrong.\n(Not your fault? raise an issue!)")

	def search_modules(self, name, banner_bool=True):
		file_info = self.load_modules()
		self.output(f"Searching for {name}...")
		if name in file_info:
			if banner_bool:
				self.info(f"{name}:")
				for each in file_info[name]:
					self.output(f"{each}: {file_info[name][each]}")
			return True
		else:
			self.error(f"{name}: Module not found.")
			return False
	
	def show_modules(self):
		file_info = self.load_modules()
		self.output("Available modules are:")
		for each in file_info:
			self.list_output(f"{each} ")

####
# READ FROM CONFIG
####
	
	def read_config(self):
		self.info("Will be added soon!")
