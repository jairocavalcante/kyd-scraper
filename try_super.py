
class super1(object):
	def __new__(cls, *args, **kwargs):
		obj = super(super1, cls).__new__(cls, *args, **kwargs)
		obj.attr1 = []
		return obj
	def __str__(self):
		show_attr = []
		for attr, value in sorted(self.__dict__.iteritems()):
			show_attr.append('%s:%r' % (attr, value))
		return '%s with %s' % (self.__class__.__name__, ', '.join(show_attr))

class super2(object):
	def __new__(cls, *args, **kwargs):
		obj = super(super2, cls).__new__(cls, *args, **kwargs)
		obj.attr2 = {}
		return obj
	

class derived(super1, super2):
	def __init__(self):
		self.attr1.append(111)
		self.attr3 = ()

d1 = derived()
d1.attr1.append(222)
print(d1)
d2 = derived()
d2.attr1.append(333)
print(d2)