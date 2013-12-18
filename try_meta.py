import inspect
import pprint

class Attr(object):
	def __init__(self):
		self.value = None
	
	def __set__(self, obj, value):
		print('set', obj, value)
		self.value = value
	
	def __get__(self, obj, typo):
		print('get', obj, typo)
		return self.value
		
	def __delete__(self, obj):
		self.value = None

class MetaClass(type):
	def __new__(mcls, name, bases, classdict):
		attrs = {}
		new_classdict = {}
		for n, v in classdict.iteritems():
			if isinstance(v, Attr):
				attrs[n] = v
			else:
				new_classdict[n] = v
		cls = type.__new__(mcls, name, bases, new_classdict)
		cls.attrs = cls.attrs.copy()
		cls.attrs.update(attrs)
		return cls

import copy

class A(object):
	# attrs = {}
	# __metaclass__ = MetaClass
	def __new__(cls, *args, **kwargs):
		obj = super(A, cls).__new__(cls, *args, **kwargs)
		for n, v in cls.__dict__.iteritems():
			if isinstance(v, Attr):
				print(n,v)
				setattr(obj, n, copy.copy(v))
		# for prop_name, prop_value in obj.attrs.items():
		# 	setattr(obj, prop_name, copy.copy(prop_value))
		return obj
	
	def __init__(self, **kwargs):
		for prop_name, prop_value in kwargs.items():
			setattr(self, prop_name, prop_value)
	
	def __getattribute__(self, key):
		"Emulate type_getattro() in Objects/typeobject.c"
		v = object.__getattribute__(self, key)
		if hasattr(v, '__get__'):
			return v.__get__(self, type(self))
		return v
	
	def __setattr__(self, key, value):
		try:
			v = object.__getattribute__(self, key)
			if hasattr(v, '__set__'):
				v.__set__(self, value)
			else:
				self.__dict__[key] = value
		except AttributeError, err:
			self.__dict__[key] = value

	# def __delattr__(self, name):
	# 	pass
	
	# def __repr__(self):
	# 	prop_names = [prop_name for prop_name, prop_type in inspect.getmembers(self)
	# 		if not prop_name.startswith('__')]
	# 	d = {}
	# 	for prop_name in prop_names:
	# 		d[prop_name] = getattr(self, prop_name)
	# 	return pprint.pformat(d)

class C(A):
	x = Attr()
	y = Attr()

c0 = C()
# print(c0.x)
# c0.x = 1
# print(c0.x)
# print dir(c0)
# c1 = C(x=1, y=2)
# c2 = C(x=2)
# print(c0.x, c0.y)
# print(c1.x, c1.y)
# print(c2.x, c2.y)


