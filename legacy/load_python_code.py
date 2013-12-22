import sys
import os
import pprint

sys.path.append(os.getcwd())

modnames = ['fetchers']

for modname in modnames:
  mod = __import__(modname, globals(), locals(), [None], -1)

for modname in modnames:
  mod = sys.modules[modname]
  for k in mod.__dict__:
    if k[:2] != '__':
      print modname, k, pprint.pformat(mod.__dict__[k])

