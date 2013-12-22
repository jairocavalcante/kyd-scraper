
import sys
import os
import types
import yaml
import json
from datetime import datetime
from kyd.fetchers.anbima import *

session_date = '2013-12-13'

def import_func(className, modName=None):
    if not modName:
        fields = className.split('.')
        modName = '.'.join(fields[:-1])
        className = fields[-1]
    if modName is '':
        modName = '__main__'
    module = __import__(modName, globals(), locals(), [className], -1)
    func = getattr(module, className)
    if type(func) is types.ModuleType:
        raise TypeError("Not callable object found")
    else:
        return func

def format_session_date(fmt, locale=None):
    global session_date
    if locale:
        import locale as loc
        loc.setlocale(loc.LC_TIME, 'pt_BR')
    sd = datetime.strptime(session_date, '%Y-%m-%d')
    dt = sd.strftime(fmt)
    if locale:
        loc.setlocale(loc.LC_TIME, '')
    return dt

fetchers = [
    {
        'fetcher'       : 'kyd.fetchers.anbima.TitPubTextFetcher',
        'name'          : 'anbima-tit-pub-text',
        'parameters'    : {
            'date' : format_session_date('%y%m%d')
        }
    },
    {
        'fetcher'       : 'kyd.fetchers.anbima.IGPMTitPubFetcher',
        'name'          : 'anbima-inflacao-ipca',
        'parameters'    : {
            'date' : format_session_date('%d%b%Y', 'pt_BR').lower()
        }
    },
    {
        'fetcher'       : 'kyd.fetchers.anbima.IPCATitPubFetcher',
        'name'          : 'anbima-inflacao-igpm',
        'parameters'    : {
            'date' : format_session_date('%d%b%Y', 'pt_BR').lower()
        }
    }
]

for fetcher_config in fetchers:
    fetcher_name = fetcher_config['fetcher']
    fetcher_klass = import_func(fetcher_config['fetcher'])
    fetcher = fetcher_klass()
    parms = fetcher_config['parameters']
    scrap = fetcher.fetch(**parms)
    action_name = fetcher_name.replace('Fetcher', 'Action').replace('fetchers', 'action')
    action_klass = import_func(action_name)
    action = action_klass()
    action.execute(scrap)

# fetcher = InflacaoTitPubFetcher()
# scrap = fetcher.fetch(date='16dez2013', contrato='ntn-c')
# print(scrap)
# 
# scrap = fetcher.fetch(date='16dez2013', contrato='ntn-b')
# print(scrap)
# 
# fetcher = TitPubTextFetcher()
# scrap = fetcher.fetch(date='131216')
# print(scrap)
# 
# fetcher = TitPubFetcher()
# scrap = fetcher.fetch(date='16dez2013', contrato='ltn')
# print(scrap)
# 
# scrap = fetcher.fetch(date='16dez2013', contrato='ntn-f')
# print(scrap)
# 
# scrap = fetcher.fetch(date='16dez2013', contrato='lft')
# print(scrap)
# 
# scrap = fetcher.fetch(date='16dez2013', contrato='ntn-b')
# print(scrap)
# 
# scrap = fetcher.fetch(date='16dez2013', contrato='ntn-c')
# print(scrap)
# 
