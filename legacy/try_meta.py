import pprint

class Attr(object):
    id = 0
    def __init__(self):
        Attr.id += 1
        self.id = Attr.id
    def __set__(self, obj, value):
        obj.attrs[self.id] = value
    def __get__(self, obj, typo):
        try:
            return obj.attrs[self.id]
        except KeyError:
            obj.attrs[self.id] = None
            return obj.attrs[self.id]
    def __delete__(self, obj):
        obj.attrs[self.id] = None

class A(object):
    def __new__(cls, *args, **kwargs):
        obj = super(A, cls).__new__(cls)
        obj.attrs = {}
        return obj
    def __init__(self, **kwargs):
        for prop_name, prop_value in kwargs.items():
            setattr(self, prop_name, prop_value)
    def __str__(self):
        unlikely = lambda x: not x.startswith('__') and x is not 'attrs'
        prop_names = [propname for propname in dir(self) if unlikely(propname)]
        d = {}
        for propname in prop_names:
            d[propname] = getattr(self, propname)
        return pprint.pformat(d)
    __repr__ = __str__

class C(A):
	x = Attr()
	y = Attr()

c0 = C()
c1 = C(x=1, y=2)
c2 = C(x=2)
print(c0.x, c0.y)
print(c1.x, c1.y)
print(c2.x, c2.y)
print(c1)