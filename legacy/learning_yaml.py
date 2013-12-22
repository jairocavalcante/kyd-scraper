
import yaml

fetchers = yaml.load(file('scraps.yaml'))
for fetcher in fetchers:
	print(fetcher['name'])