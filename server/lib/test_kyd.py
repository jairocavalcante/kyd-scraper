
from kyd.fetchers.anbima import *
# from kyd.scraps.anbima import *

fetcher = InflacaoTitPubFetcher()
scrap = fetcher.fetch(date='16dez2013', contrato='ntn-c')
print(scrap)

scrap = fetcher.fetch(date='16dez2013', contrato='ntn-b')
print(scrap)

fetcher = TitPubTextFetcher()
scrap = fetcher.fetch(date='131216')
print(scrap)

fetcher = TitPubFetcher()
scrap = fetcher.fetch(date='16dez2013', contrato='ltn')
print(scrap)

scrap = fetcher.fetch(date='16dez2013', contrato='ntn-f')
print(scrap)

scrap = fetcher.fetch(date='16dez2013', contrato='lft')
print(scrap)

scrap = fetcher.fetch(date='16dez2013', contrato='ntn-b')
print(scrap)

scrap = fetcher.fetch(date='16dez2013', contrato='ntn-c')
print(scrap)

