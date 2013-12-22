
from datetime import datetime

def today(fmt, locale=None):
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
            'date' : today('%y%m%d')
        }
    },
    {
        'fetcher'       : 'kyd.fetchers.anbima.IGPMTitPubFetcher',
        'name'          : 'anbima-inflacao-ipca',
        'parameters'    : {
            'date' : today('%d%b%Y', 'pt_BR').lower()
        }
    },
    {
        'fetcher'       : 'kyd.fetchers.anbima.IPCATitPubFetcher',
        'name'          : 'anbima-inflacao-igpm',
        'parameters'    : {
            'date' : today('%d%b%Y', 'pt_BR').lower()
        }
    }
]

