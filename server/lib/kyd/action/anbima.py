
from kyd.models.anbima import *

class IGPMTitPubAction(object):
    def execute(self, scrap):
        query = InflacaoTitPub.query(InflacaoTitPub.indice == 'IGPM', 
            InflacaoTitPub.data_atual == scrap.data_atual)
        if query.count() == 0:
            model = InflacaoTitPub()
            model.indice = 'IGPM'
            model.data_atual = scrap.data_atual
            model.taxa = scrap.taxa
            model.tipo = scrap.tipo
            model.put()

class IPCATitPubAction(object):
    def execute(self, scrap):
        query = InflacaoTitPub.query(InflacaoTitPub.indice == 'IPCA', 
            InflacaoTitPub.data_atual == scrap.data_atual)
        if query.count() == 0:
            model = InflacaoTitPub()
            model.indice = 'IPCA'
            model.data_atual = scrap.data_atual
            model.taxa = scrap.taxa
            model.tipo = scrap.tipo
            model.put()
        
class TitPubTextAction(object):
    def execute(self, scrap):
        for scrp in scrap.titulos:
            query = TitPub.query(TitPub.codigo_selic == scrp.codigo_selic, 
                TitPub.data_referencia == scrp.data_referencia,
                TitPub.data_vencimento == scrp.data_vencimento)
            if query.count() == 0:
                model = TitPub()
                model.codigo_selic = scrp.codigo_selic
                model.titulo = scrp.titulo
                model.data_referencia = scrp.data_referencia
                model.data_base = scrp.data_base
                model.data_vencimento = scrp.data_vencimento
                model.taxa_max = scrp.taxa_max
                model.taxa_min = scrp.taxa_min
                model.taxa_ind = scrp.taxa_ind
                model.pu = scrp.pu
                model.desvio_padrao = scrp.desvio_padrao
                model.put()
