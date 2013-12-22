# encoding: utf-8

from bs4 import BeautifulSoup as bs
from kyd.scraps.anbima import *
import scraps

class InflacaoTitPubFetcher(scraps.Fetcher):
	url = 'http://www.anbima.com.br/merc_sec/resultados/msec_{date}_{contrato}.asp'
	def parse(self, content):
		soup = bs(content.text)
		tables = soup.html.body.table.tr.td.div.find_all('table')
		data_atual = tables[2].tr.td.next_sibling.next_sibling.string
		taxa = tables[7].tr.td.contents[0].string.split(':')[1].replace('%', '')
		scrap = InflacaoTitPubScrap(data_atual=data_atual, taxa=taxa)
		return scrap

class TitPubFetcher(scraps.Fetcher):
	url = 'http://www.anbima.com.br/merc_sec/resultados/msec_{date}_{contrato}.asp'
	def parse(self, content):
		soup = bs(content.text)
		tables = soup.html.body.table.tr.td.div.find_all('table')
		data_atual = tables[2].tr.td.next_sibling.next_sibling.string
		nome = tables[2].tr.next_sibling.next_sibling.td.next_sibling.next_sibling.string
		scraps = TitPubsScrap(data_atual=data_atual, nome=nome)
		for sib in tables[2].tr.next_sibling.next_sibling.next_sibling.next_sibling.next_siblings:
			row = [str(elm.string) for elm in sib.contents if str(elm.string).strip() is not '']
			tit = TitPubScrap(codigo_selic=row[0], data_base=row[1],
				data_vencimento=row[2], taxa_max=row[3], taxa_min=row[4],
				taxa_ind=row[5], pu=row[6])
			scraps.titulos = tit
		return scraps

class TitPubTextFetcher(scraps.Fetcher):
	url = 'http://www.anbima.com.br/merc_sec/arqs/ms{date}.txt'
	def parse(self, content):
		from itertools import dropwhile, ifilter
		from StringIO import StringIO
		text = StringIO(content.text)
		scraps = TitPubsTextScrap()
		_drop_first_3 = dropwhile(lambda x: x[0] < 3, enumerate(text))
		_drop_empy = ifilter(lambda x: x[1].strip() is not '', _drop_first_3)
		for c, line in _drop_empy:
			row = line.split('@')
			tit = TitPubTextScrap(titulo=row[0], data_referencia=row[1],
				codigo_selic=row[2], data_base=row[3],
				data_vencimento=row[4], taxa_max=row[5], taxa_min=row[6],
				taxa_ind=row[7], pu=row[8], desvio_padrao=row[9])
			scraps.titulos = tit
		return scraps

