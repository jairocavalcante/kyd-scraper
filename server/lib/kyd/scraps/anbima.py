
import scraps

class TitPubTextScrap(scraps.Scrap):
	"""This represents scraps of information from Anbima's Govt Bonds text file."""
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
	"""This represents scraps of information from Anbima's Public Bonds page."""
	titulos = scraps.Attribute(repeat=True)

class TitPubScrap(scraps.Scrap):
	"""This represents scrapss of information from Anbima's NTN-B page"""
	_error_is_none = True
	codigo_selic = scraps.Attribute()
	data_base = scraps.DateAttr(formatstr='%d/%m/%Y')
	data_vencimento = scraps.DateAttr(formatstr='%d/%m/%Y')
	taxa_max = scraps.FloatAttr(decimalsep=',')
	taxa_min = scraps.FloatAttr(decimalsep=',')
	taxa_ind = scraps.FloatAttr(decimalsep=',')
	pu = scraps.FloatAttr(thousandsep='.', decimalsep=',')
	
class AnbimaTitPubScrap(scraps.Scrap):
	"""This represents scrapss of information from Anbima's NTN-B page"""
	data_atual = scraps.DateAttr(formatstr='%d/%b/%Y', locale='pt_BR')
	nome = scraps.Attribute(transform=lambda x: x.split()[0])
	titulos = scraps.Attribute(repeat=True)

class AnbimaNtnbScrap(scraps.Scrap):
	"""This represents scrapss of information from Anbima's NTN-B page"""
	data_atual = scraps.DateAttr(formatstr='%d/%b/%Y', locale='pt_BR')
	ipca_final = scraps.FloatAttr(decimalsep=',')
	nome = scraps.Attribute(transform=lambda x: x.split()[0])
	titulos = scraps.Attribute(repeat=True)
	
