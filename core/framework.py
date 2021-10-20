import os
import requests
from core.rootdir import ROOT_DIR
import modules as m
import core.utils as u

__author__ = 'Divya Goswami (@rachejazz)'
with open("VERSION", 'r') as v:
	__version__ = v.read().strip('\n')

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

####
# METHODS
####

	def show_about(self, bool_val):
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

	def print_banner(self, message, bool_val=True):
		if bool_val:
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

	def run_modules(self, name, q, banner_bool):
#		try:
		bool_val = self.search_modules(name, banner_bool)
		if bool_val:
			engine = getattr(m, name)
			engine.mod_run(self, name, q)
#		except:
#			self.error(f"Something went wrong.\n(Not your fault? raise an issue!)")

	def search_modules(self, name, banner_bool=True):
		files = [f for f in os.listdir(self.mod_path)if not f.startswith('__')]
		if f"{name}.py" in files:
			engine = getattr(m, name)
			if banner_bool:
				self.info(f"{name}: ")
				engine.options(self)
			return True
		else:
			self.error(f"{name}: Module not found.")
			return False
	
	def show_modules(self, name):
		files = [f for f in os.listdir(self.mod_path) if f.endswith('.py') and not f.startswith('__')]
		self.output("Available modules are:")
		for each in files:
			self.list_output(each.replace('.py', ''))
			

####
# READ FROM CONFIG
####
	
	def read_config(self, bool_val):
		self.info("Will be added soon!")
