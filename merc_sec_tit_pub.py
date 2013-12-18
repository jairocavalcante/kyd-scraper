# encoding: utf-8

from bs4 import BeautifulSoup
import bs4
import urllib2
import cookielib
import pprint
import scraps

class TituloNtnbScrap(scraps.Scrap):
	"""This represents scrapss of information from Anbima's NTN-B page"""
	error_is_none = True
	codigo_selic = scraps.Attribute()
	data_base = scraps.DatetimeAttr(formatstr='%d/%m/%Y')
	data_vencimento = scraps.DatetimeAttr(formatstr='%d/%m/%Y')
	taxa_max = scraps.FloatAttr(decimalsep=',', transform=lambda x: x/100.0)
	taxa_min = scraps.FloatAttr(decimalsep=',', transform=lambda x: x/100.0)
	taxa_ind = scraps.FloatAttr(decimalsep=',', transform=lambda x: x/100.0)
	pu = scraps.FloatAttr(thousandsep='.', decimalsep=',')
	
class AnbimaNtnbScrap(scraps.Scrap):
	"""This represents scrapss of information from Anbima's NTN-B page"""
	data_atual = scraps.DatetimeAttr(formatstr='%d/%b/%Y', locale='pt_BR')
	ipca_final = scraps.FloatAttr(decimalsep=',', percentage=True)
	nome = scraps.Attribute()
	titulos = scraps.Attribute(repeat=True)
	
class AnbimaNTNBFetcher(scraps.Fetcher):
	name = 'anbima-ntn-b'
	url = 'http://www.anbima.com.br/merc_sec/resultados/msec_16dez2013_ntn-b.asp'
	def parse(self, content):
		soup = BeautifulSoup(content)
		tables = soup.html.body.table.tr.td.div.find_all('table')
		data_atual = tables[2].tr.td.next_sibling.next_sibling.string
		nome = tables[2].tr.next_sibling.next_sibling.td.next_sibling.next_sibling.string
		ipca_final = tables[7].tr.td.contents[0].string.split(':')[1]
		scraps = AnbimaNtnbScrap(data_atual=data_atual, nome=nome, 
			ipca_final=ipca_final)
		for sib in tables[2].tr.next_sibling.next_sibling.next_sibling.next_sibling.next_siblings:
			row = [str(elm.string) for elm in sib.contents if str(elm.string).strip() is not '']
			print(row)
			tit = TituloNtnbScrap(codigo_selic=row[0], data_base=row[1],
				data_vencimento=row[2], taxa_max=row[3], taxa_min=row[4],
				taxa_ind=row[5], pu=row[6])
			# print(scraps.titulos)
			print(tit)
			scraps.titulos = tit
		return scraps

fetcher = AnbimaNTNBFetcher()
ret = fetcher.fetch()
# print ret

# cj = cookielib.LWPCookieJar()
# proc = urllib2.HTTPCookieProcessor(cj)
# url = 'http://www.anbima.com.br/merc_sec/resultados/msec_16dez2013_ntn-b.asp'
# 
# opener = urllib2.build_opener()
# req = urllib2.Request(url)
# ret = opener.open(req)
# 
# soup = BeautifulSoup(ret.read())
# 
# tables = soup.html.body.table.tr.td.div.find_all('table')
# 
# # td = tables[2].tr.find_all('td')
# # print len(td)
# # print td[0].string
# # print td[1].string
# 
# # print tables[2].tr.td.string
# print tables[2].tr.td.next_sibling.next_sibling.string
# 
# print tables[2].tr.next_sibling.next_sibling.td.string
# print tables[2].tr.next_sibling.next_sibling.td.next_sibling.next_sibling.string



