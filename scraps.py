
from decimal import Decimal
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
		
class Scrap(object):
	"""	Scrap class represents a bunch of data collected from information
		sources.
	"""
	def __new__(cls, *args, **kwargs):
		obj = super(Scrap, cls).__new__(cls)
		obj.attrs = {}
		return obj
	
	def __init__(self, **kwargs):
		prop_names = [member[0] for member in inspect.getmembers(self)
			if not member[0].startswith('__')]
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
		unlikely = lambda x: not x.startswith('__') and x is not 'attrs'
		prop_names = [member[0] for member in inspect.getmembers(self) if unlikely(member[0])]
		d = {}
		for propname in prop_names:
			d[propname] = getattr(self, propname)
		return pprint.pformat(d)
	
	__str__ = __repr__

class Attribute(object):
	"""	Attribute class is a descriptor which represents each chunk of
		data extracted from a source of information.
	"""
	index = 0
	def __init__(self, repeat=False, transform=lambda x: x):
		Attribute.index += 1
		self.index = Attribute.index
		# self.value = None
		self.repeat = repeat
		self.transform = transform
	
	def __set__(self, obj, value):
		"""sets attribute's value"""
		value = self.transform(value)
		if self.repeat:
			try:
				obj.attrs[self.index].append(value)
			except:
				obj.attrs[self.index] = [value]
		else:
			obj.attrs[self.index] = value
	
	def __get__(self, obj, typo=None):
		"""gets attribute's value"""
		try:
			return obj.attrs[self.index]
		except KeyError:
			return None
		
	def __delete__(self, obj):
		"""resets attribute's initial state"""
		obj.attrs[self.index] = None

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
		
		
		