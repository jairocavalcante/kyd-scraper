
import pprint
import inspect
import urllib2
from datetime import datetime

class Fetcher(object):
	"""	Fetcher class represents the request handler. It defines the URL to be
		requested so as the method to parse.
	"""
	def fetch(self):
		opener = urllib2.build_opener()
		req = urllib2.Request(self.url)
		return self.parse(opener.open(req))
	
	def parse(self, content):
		"""	it receives the fetched content, parses it and returns a Scrap."""
		raise NotImplemented('This method must be inherited.')

class MetaScraps(type):
	def __new__(mcls, name, bases, classdict):
		attrs = {}
		new_classdict = {}
		for n, v in classdict.iteritems():
			if isinstance(v, Attribute):
				attrs[n] = v
			else:
				new_classdict[n] = v
		cls = type.__new__(mcls, name, bases, new_classdict)
		cls.attrs = cls.attrs.copy()
		cls.attrs.update(attrs)
		return cls
		
class Scrap(object):
	"""	Scrap class represents a bunch of data collected from information
		sources.
	"""
	__metaclass__ = MetaScraps
	def __init__(self, **kwargs):
		prop_names = [prop_name for prop_name, prop_type in inspect.getmembers(self)
			if not prop_name.startswith('__')]
		if 'error_is_none' not in prop_names:
			self.error_is_none = False
		for prop_name, prop_value in kwargs.items():
			if prop_name not in prop_names:
				raise KeyError('Invalid attribute: ' + prop_name)
			try:
				setattr(self, prop_name, prop_value)
			except Exception, e:
				if not self.error_is_none:
					raise e
	
	def __repr__(self):
		prop_names = [prop_name for prop_name, prop_type in inspect.getmembers(self)
			if not prop_name.startswith('__')]
		d = {}
		for prop_name in prop_names:
			d[prop_name] = getattr(self, prop_name)
		return pprint.pformat(d)

class Attribute(object):
	"""	Attribute class is a descriptor which represents each chunk of
		data extracted from a source of information.
	"""
	def __init__(self, repeat=False, transform=lambda x: x):
		self.value = None
		self.repeat = repeat
		self.transform = transform
	
	def __set__(self, obj, value):
		"""sets attribute's value"""
		value = self.transform(value)
		if self.repeat:
			try:
				self.value.append(value)
			except:
				self.value = [value]
		else:
			self.value = value
	
	def __get__(self, obj, typo):
		"""gets attribute's value"""
		return self.value
		
	def __delete__(self, obj):
		"""resets attribute's initial state"""
		self.value = None

class FloatAttr(Attribute):
	"""	FloatAttr class is an Attribute descriptor which tries to convert to 
		float every value set. It should convert mainly strings though numeric 
		types such as int and decimal could be set.
	"""
	def __init__(self, thousandsep=None, decimalsep=None, percentage=False, **kwargs):
		super(FloatAttr, self).__init__(**kwargs)
		self.decimalsep = decimalsep
		self.percentage = percentage
		self.thousandsep = thousandsep
	
	def __set__(self, obj, value):
		if type(value) in (str, unicode):
			if self.thousandsep is not None:
				value = value.replace(self.thousandsep, '')
			if self.decimalsep is not None:
				value = value.replace(self.decimalsep, '.')
			if self.percentage:
				value = value.replace('%', '')
		if self.percentage:
			value = float(value)/100
		else:
			value = float(value)
		super(FloatAttr, self).__set__(obj, value)
	
class DatetimeAttr(Attribute):
	"""	DatetimeAttr class is an Attribute descriptor which tries to convert to
		datetime.datetime every value set.
	"""
	def __init__(self, formatstr=None, locale=None, **kwargs):
		super(DatetimeAttr, self).__init__(**kwargs)
		self.formatstr = formatstr
		self.locale = locale
		
	def __set__(self, obj, value):
		if self.locale is not None:
			import locale
			locale.setlocale(locale.LC_TIME, 'pt_BR')
		value = datetime.strptime(value, self.formatstr)
		if self.locale is not None:
			locale.setlocale(locale.LC_TIME, '')
		super(DatetimeAttr, self).__set__(obj, value)
		
		
		