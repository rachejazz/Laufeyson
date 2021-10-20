VERSION = ''

import argparse
import sys
from core import framework as f
from core.banner import BANNER,INFO
sys.path.append(sys.path[0])

sys.dont_write_bytecode = True

def welcome():
	lauf = f.Laufeyson()
	lauf.print_banner(f"{f.Colors.G}{BANNER}", args.nobanner)
	lauf.print_banner(f"{f.Colors.Y}{WELCOME}", args.nobanner)
	lauf.print_banner(f"{f.Colors.G}{INFO}", args.nobanner)

def lauf(args):
	lauf = f.Laufeyson()
	if args.config:
		lauf.read_config(args.config)
	else:
		if args.module:
			welcome()
			lauf.output(f"Searching for {args.module}...")
			if args.query:
				lauf.run_modules(args.module, args.query, args.nobanner)
			else:	
				lauf.search_modules(args.module)		
		elif args.show:
			welcome()
			lauf.show_modules(args.show)
		elif args.about:
			welcome()
			lauf.show_about(args.about)
		elif args.search:
			welcome()
			lauf.output(f"Searching for module {args.search}...")
			lauf.search_modules(args.search)
		else:
			lauf.output(f"{f.Colors.N}To get started, use the -h option to see what options are available")
	
WELCOME = f"[ {f.__version__}, {f.__author__} ]"
parser = argparse.ArgumentParser(description=WELCOME)
parser.add_argument('-a', '--about', help='show the details of this tool', dest='about', action='store_true')
parser.add_argument('-S', '--show', help='list all available modules', dest='show', action='store_true')
parser.add_argument('-B', '--nobanner', help='run without banner', dest='nobanner', action='store_false')
parser.add_argument('-c', '--config', help='execute according to config', dest='config', action='store_true')
parser.add_argument('-s', '--search', metavar='MODULE', help='search for a module', dest='search', action='store')
parser.add_argument('-m', '--module',  help='run a module', dest='module', action='store')
parser.add_argument('-q', '--query',  help='query domain/IP', dest='query', action='store')
args = parser.parse_args()
lauf(args)
