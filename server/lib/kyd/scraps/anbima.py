
import scraps

class InflacaoTitPubScrap(scraps.Scrap):
	"""This represents inflation scraps which appears in Anbima's govt bonds
		page."""
	data_atual = scraps.DateAttr(formatstr='%d/%b/%Y', locale='pt_BR')
	taxa = scraps.FloatAttr(decimalsep=',')

class TitPubTextScrap(scraps.Scrap):
	"""This represents scraps of information from Anbima's govt bonds text
		file."""
	_error_is_none = True
	codigo_selic = scraps.Attribute()
	titulo = scraps.Attribute()
	data_referencia = scraps.DateAttr(formatstr='%Y%m%d')
	data_base = scraps.DateAttr(formatstr='%Y%m%d')
	data_vencimento = scraps.DateAttr(formatstr='%Y%m%d')
	taxa_max = scraps.FloatAttr(decimalsep=',')
	taxa_min = scraps.FloatAttr(decimalsep=',')
	taxa_ind = scraps.FloatAttr(decimalsep=',')
	pu = scraps.FloatAttr(thousandsep='.', decimalsep=',')
	desvio_padrao = scraps.FloatAttr(decimalsep=',')
	
class TitPubsTextScrap(scraps.Scrap):
	"""This represents scraps of information from Anbima's govt bonds text
		file."""
	titulos = scraps.Attribute(repeat=True)

class TitPubScrap(scraps.Scrap):
	"""This scrap represents each contract from Anbima's govt bonds page."""
	_error_is_none = True
	codigo_selic = scraps.Attribute()
	data_base = scraps.DateAttr(formatstr='%d/%m/%Y')
	data_vencimento = scraps.DateAttr(formatstr='%d/%m/%Y')
	taxa_max = scraps.FloatAttr(decimalsep=',')
	taxa_min = scraps.FloatAttr(decimalsep=',')
	taxa_ind = scraps.FloatAttr(decimalsep=',')
	pu = scraps.FloatAttr(thousandsep='.', decimalsep=',')
	
class TitPubsScrap(scraps.Scrap):
	"""This represents scraps of information from Anbima's govt bonds page."""
	data_atual = scraps.DateAttr(formatstr='%d/%b/%Y', locale='pt_BR')
	nome = scraps.Attribute(transform=lambda x: x.split()[0])
	titulos = scraps.Attribute(repeat=True)


