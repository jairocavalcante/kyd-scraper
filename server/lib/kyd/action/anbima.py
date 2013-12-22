
from kyd.models.anbima import *

class IGPMTitPubAction(object):
    def execute(self, scrap):
        model = InflacaoTitPub()
        model.indice = 'IGPM'
        model.data_atual = scrap.data_atual
        model.taxa = scrap.taxa
        model.tipo = scrap.tipo
        model.put()

class IPCATitPubAction(object):
    def execute(self, scrap):
        model = InflacaoTitPub()
        model.indice = 'IPCA'
        model.data_atual = scrap.data_atual
        model.taxa = scrap.taxa
        model.tipo = scrap.tipo
        model.put()
        
class TitPubTextAction(object):
    def execute(self, scrap):
        pass
