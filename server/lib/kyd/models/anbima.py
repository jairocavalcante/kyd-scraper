
from google.appengine.ext import ndb

class InflacaoTitPub(ndb.Model):
    """
    This represents inflation rates extracted from Anbima's govt bonds page.
    """
    indice = ndb.StringProperty()
    data_atual = ndb.DateProperty()
    taxa = ndb.FloatProperty()
    tipo = ndb.StringProperty()

class TitPub(ndb.Model):
    """
    This represents the govt bonds extracted from Anbima's text file.
    """
    codigo_selic = ndb.StringProperty()
    titulo = ndb.StringProperty()
    data_referencia = ndb.DateProperty()
    data_base = ndb.DateProperty()
    data_vencimento = ndb.DateProperty()
    taxa_max = ndb.FloatProperty()
    taxa_min = ndb.FloatProperty()
    taxa_ind = ndb.FloatProperty()
    pu = ndb.FloatProperty()
    desvio_padrao = ndb.FloatProperty()

