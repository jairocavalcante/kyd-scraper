
import unittest
import scraps

class TestScrap(unittest.TestCase):
	def test_Scrap(self):
		"""it should create and instanciate a Scrap class"""
		class MyScrap(scraps.Scrap):
			a1 = scraps.Attribute()
		
		myScrap = MyScrap()
		self.assertEquals(myScrap.a1, None)
		
		myScrap.a1 = 1
		self.assertEquals(myScrap.a1, 1)
		
		del(myScrap.a1)
		self.assertEquals(myScrap.a1, None)
	
	def test_Scrap_instanciation(self):
		"""it should instanciate a Scrap passing parameter."""
		import inspect
		class MyScrap(scraps.Scrap):
			title = scraps.Attribute()
		myScrap = MyScrap(title='Normstron')
		self.assertEquals(myScrap.title, 'Normstron')
		
	def test_Scrap_instanciation2(self):
		"""it should instanciate a Scrap passing an invalid parameter."""
		import inspect
		class MyScrap(scraps.Scrap):
			title = scraps.Attribute()
		with self.assertRaises(Exception):
			myScrap = MyScrap(title1='Normstron')
			
	def test_Scrap_errorisnone(self):
		"""it should instanciate a Scrap passing an invalid parameter."""
		import inspect
		class MyScrap(scraps.Scrap):
			float_attr = scraps.FloatAttr()
			error_is_none = True
		myScrap = MyScrap(float_attr='--')
		class MyScrap(scraps.Scrap):
			float_attr = scraps.FloatAttr()
		with self.assertRaises(Exception):
			myScrap = MyScrap(float_attr='--')

class TestAttribute(unittest.TestCase):
	def test_Attribute(self):
		"""	it should instanciate an Attribute class and its descriptor 
			methods
		"""
		a = scraps.Attribute()
		self.assertEquals(a.__get__(None, None), None)
		a.__set__(None, 1)
		self.assertEquals(a.__get__(None, None), 1)
		a.__delete__(None)
		self.assertEquals(a.__get__(None, None), None)
		
	def test_Attribute_repeat(self):
		"""it should instanciate a repeated Attribute"""
		a = scraps.Attribute(repeat=True)
		a.__set__(None, 1)
		a.__set__(None, 2)
		self.assertEquals(a.__get__(None, None), [1,2])
	
	def test_Attribute_transform(self):
		"""	it should instanciate an Attribute that should be transformed by some
			function while is set
		"""
		a = scraps.Attribute(transform=lambda x: x*100)
		a.__set__(None, 1)
		self.assertEquals(a.__get__(None, None), 100)
	
class TestFloatAttr(unittest.TestCase):
	def test_FloatAttr(self):
		"""it should instanciate the FloatAttr class and set it with a valid string."""
		a = scraps.FloatAttr()
		a.__set__(None, '2.2')
		self.assertAlmostEqual(a.__get__(None, None), 2.2)
		
	def test_FloatAttr_int(self):
		"""it should instanciate the FloatAttr class and set it with an int."""
		a = scraps.FloatAttr()
		a.__set__(None, 2)
		self.assertAlmostEqual(a.__get__(None, None), 2.0)

	def test_FloatAttr_float(self):
		"""it should instanciate the FloatAttr class and set it with a float."""
		a = scraps.FloatAttr()
		a.__set__(None, 2.2)
		self.assertAlmostEqual(a.__get__(None, None), 2.2)

	def test_FloatAttr_decimal(self):
		"""it should instanciate the FloatAttr class and set it with a decimal."""
		from decimal import Decimal
		a = scraps.FloatAttr()
		a.__set__(None, Decimal(2.2))
		self.assertAlmostEqual(a.__get__(None, None), 2.2)
		
	def test_FloatAttr_comma(self):
		"""	it should instanciate the FloatAttr class and set it with a string
			which represents a float but uses comma as decimal separator."""
		a = scraps.FloatAttr(decimalsep=',')
		a.__set__(None, '2,2')
		self.assertAlmostEqual(a.__get__(None, None), 2.2)
	
	def test_FloatAttr_percentage(self):
		"""	it should instanciate the FloatAttr class and set it with a string
			which represents a percentage, ie, a float followed by the symbol '%'."""
		a = scraps.FloatAttr(percentage=True)
		a.__set__(None, '22 %')
		self.assertAlmostEqual(a.__get__(None, None), 22./100)
	
	def test_FloatAttr_percentage_comma(self):
		"""	it should instanciate the FloatAttr class and set it with a string
			which represents a percentage and uses comma as decimal separator."""
		a = scraps.FloatAttr(decimalsep=',', percentage=True)
		a.__set__(None, '22,5 %')
		self.assertAlmostEqual(a.__get__(None, None), 22.5/100)

	def test_FloatAttr_thousand(self):
		"""	it should instanciate the FloatAttr class and set it with a string
			which represents a float with thousand separators."""
		a = scraps.FloatAttr(thousandsep=',')
		a.__set__(None, '2,222.22')
		self.assertAlmostEqual(a.__get__(None, None), 2222.22)
		a = scraps.FloatAttr(thousandsep='.', decimalsep=',')
		a.__set__(None, '2.222,22')
		self.assertAlmostEqual(a.__get__(None, None), 2222.22)
	
	def test_FloatAttr_repeat(self):
		"""	it should instanciate the FloatAttr class and set the repeat parameter
			from Attribute."""
		a = scraps.FloatAttr(repeat=True)
		a.__set__(None, '22.5')
		a.__set__(None, '22.5')
		self.assertEquals(a.__get__(None, None), [22.5, 22.5])

	def test_FloatAttr_error(self):
		"""	it should instanciate the FloatAttr class with an invalid string."""
		a = scraps.FloatAttr()
		with self.assertRaises(Exception):
			a.__set__(None, '--')
	
class TestDatetimeAttr(unittest.TestCase):
	def test_DatetimeAttr(self):
		"""	it should instanciate the DatetimeAttr class and set it with a 
			valid string."""
		from datetime import datetime
		a = scraps.DatetimeAttr(formatstr='%Y-%m-%d')
		a.__set__(None, '2013-01-01')
		self.assertEquals(a.__get__(None, None), datetime(2013,1,1))
		
	def test_DatetimeAttr_locale(self):
		"""	it should instanciate the DatetimeAttr class and set it with a 
			valid string and locale."""
		from datetime import datetime
		a = scraps.DatetimeAttr(formatstr='%d/%b/%Y', locale='pt_BR')
		a.__set__(None, '11/Dez/2013')
		self.assertEquals(a.__get__(None, None), datetime(2013,12,11))
		# Check if locale have been restored
		a = scraps.DatetimeAttr(formatstr='%d/%b/%Y')
		a.__set__(None, '11/Dec/2013')
		self.assertEquals(a.__get__(None, None), datetime(2013,12,11))
		
class TestFetcher(unittest.TestCase):
	def test_Fetcher(self):
		"""	it should create a Fetcher."""
		class MyFetcher(scraps.Fetcher):
			name = 'test'
			url = 'http://httpbin.org/html'
			def parse(self, content):
				from bs4 import BeautifulSoup
				soup = BeautifulSoup(content)
				class MockScrap(object):
					title = soup.html.body.h1.string
				return MockScrap()
		fetcher = MyFetcher()
		ret = fetcher.fetch()
		self.assertEquals(ret.title, 'Herman Melville - Moby-Dick')

if __name__ == '__main__':
	unittest.main(verbosity=1)

