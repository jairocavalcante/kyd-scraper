
import yaml
import pprint

fetchers = yaml.load(file('scraps.yaml'))
print pprint.pformat(fetchers)
for fetcher in fetchers:
	print(fetcher['name'])