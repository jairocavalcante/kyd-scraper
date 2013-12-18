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


class B(object):
	x = Attr()
	y = Attr()

# b0 = B()
# print(b0.x)
# b0.x = 1
# print(b0.x)

class D(object):
	def __init__(self):
		self.x = Attr()
		self.y = Attr()
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

d0 = D()
d1 = D()
print(d0.x, d1.x)
d0.x = 1
d1.x = 'w'
print(d0.x, d1.x)
d0.x = 2
d1.x = 'i'
print(d0.x, d1.x)

class E(object):
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

# e0 = E()
# e0.x = Attr()
# print(e0.x)
# e0.x = 1
# print(e0.x)
