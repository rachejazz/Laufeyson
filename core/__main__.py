VERSION = ''

import argparse
import sys
from core import framework as f
sys.path.append(sys.path[0])
sys.dont_write_bytecode = True

def lauf(args):
	help_menu= 'usage: laufeyson [-h] [-c] [-a] [-S] [-m MODULE] [-B]'\
			   '\n     -h, --help     show this help message and exit'\
			   '\n     -c, --config   load and execute from config file'\
			   '\n     -a, --about    show about tool and exit'\
			   '\n     -S, --show     show all available modules and exit'\
			   '\n     -m, --module   show info of module and exit'\
			   '\n     -B, --nobanner execute tool without banner'\

	lauf = f.Laufeyson()
	option = args[1] if not len(args) == 1 else '-h'

	if option == '-c' or option == '--config':
		lauf.read_config()
	else:
		if option == '-m' or option == '--module':
			value = lauf.init_load_options(args)
			lauf.welcome(value['nobanner'])
			if 'query' in value:
				lauf.run_modules(value['module'], value['query'], value['nobanner'])
			else:	
				lauf.search_modules(value['module'])
		elif option == '-S' or option == '--show':
			lauf.welcome()
			lauf.show_modules()
		elif option == '-a' or option == '--about':
			lauf.welcome()
			lauf.show_about()
		elif option == '-h' or option == '--help':
			lauf.welcome()
			lauf.print_message(f"{f.Colors.N}{help_menu}", False)
		else:
			lauf.welcome()
			lauf.output(f"{f.Colors.N}To get started, use the -h option to see what options are available")
	
args = sys.argv
lauf(args)
