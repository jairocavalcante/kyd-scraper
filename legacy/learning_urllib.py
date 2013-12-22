import urllib2
import inspect
import pprint
import httplib

opener = urllib2.build_opener()
req = urllib2.Request('http://www.anbima.com.br/merc_sec/resultados/msec_16dez2013_ntn-b.asp')
res = opener.open(req)
print res.getcode()
print dir(res.info())
print res.info().getheader('date')
print res.info().getheader('content-type')
print res.info().getheader('connection')
print res.info().getheader('server')
print res.info().getheader('content-length')
print res.info().headers
print res.geturl()

conn = httplib.HTTPConnection("www.anbima.com.br")
conn.request("GET", "/merc_sec/resultados/msec_16dez2013_ntn-b.asp")
r1 = conn.getresponse()
print dir(r1)
print r1.getheaders()
print r1.status, r1.reason

conn = httplib.HTTPConnection("www.aboutwilson.net")
conn.request("GET", "/merc_sec/resultados/index.html")
r1 = conn.getresponse()
print dir(r1)
print r1.getheaders()
print r1.status, r1.reason

