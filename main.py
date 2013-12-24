import webapp2
from markupsafe import Markup, escape
import scraps
import pprint
from datetime import datetime
import itertools
import functools

(   ('Feb', 'Fev'),
    ('Apr', 'Abr'),
    ('May', 'Mai'),
    ('Aug', 'Ago'),
    ('Sep', 'Set'),
    ('Oct', 'Out'),
    ('Dec', 'Dez'))

class Processor(webapp2.RequestHandler):
    def get(self):
        session_date = self.request.get('session_date')
        pre = Markup('<pre>%s</pre>')
        self.response.write(pre % session_date)
        processor = scraps.ProcessFetchers()
        fetchers = self.gen_fetchers(session_date)
        processor.process(fetchers)
        self.response.write(pre % pprint.pformat(fetchers, indent=4))
    
    def gen_fetchers(self, session_date):
        def format_date(fmt, locale=None):
            sd = datetime.strptime(session_date, '%Y-%m-%d')
            dt = sd.strftime(fmt)
            dt = dt.replace(*('Dec', 'Dez'))
            return dt
        
        fetchers = [
            {
                'fetcher'       : 'kyd.fetchers.anbima.TitPubTextFetcher',
                'name'          : 'anbima-tit-pub-text',
                'parameters'    : {
                    'date' : format_date('%y%m%d')
                }
            },
            {
                'fetcher'       : 'kyd.fetchers.anbima.IGPMTitPubFetcher',
                'name'          : 'anbima-inflacao-ipca',
                'parameters'    : {
                    'date' : format_date('%d%b%Y', 'pt_BR').lower()
                }
            },
            {
                'fetcher'       : 'kyd.fetchers.anbima.IPCATitPubFetcher',
                'name'          : 'anbima-inflacao-igpm',
                'parameters'    : {
                    'date' : format_date('%d%b%Y', 'pt_BR').lower()
                }
            }
        ]

        return fetchers


class KydIndex(webapp2.RequestHandler):
    def get(self):
        f = open('scraps.yaml')
        self.response.write(f.read())

app = webapp2.WSGIApplication([
    ('/', KydIndex),
    ('/process', Processor)
], debug=True)
