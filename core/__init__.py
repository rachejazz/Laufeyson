import os

allfiles = list()
for (dirpath, dirnames, filenames) in os.walk(os.path.dirname(__file__)):
    allfiles += [os.path.join(dirpath, file) for file in filenames if file.endswith('.py') and not file.startswith('__')]

__all__ = [os.path.basename(x).replace('.py','') for x in allfiles]

from .utils import *
