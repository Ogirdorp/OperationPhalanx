import os
import inspect
import importlib
import settings as cfg

ldir = os.path.join(cfg.mish, 'loads')
if not os.path.isdir(ldir):
	os.mkdir(ldir)
os.chdir(ldir)

for grp in ['ana', 'marine', 'ukbaf', 'acr', 'abe', 'det5', 'det5_crates', 'soar', 'ana_vic_lite']:
	lib = importlib.import_module('loads.' + grp)
	for name, obj in inspect.getmembers(lib):
		if inspect.isclass(obj) and 'NoWrite' not in obj.__dict__:
			obj().write()
