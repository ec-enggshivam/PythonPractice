import unittest

def add(x,y):
    return x+y

def sub(x,y):
        return x-y

class SimpleTest(unittest.TestCase):
        def testadd1(self):
                self.assertEqual(add(4,5),9)

        def testsub1(self):
                self.assertEqual(sub(9, 5), 4)

        def test_upper(self):
                self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
                self.assertTrue('FOO'.isupper())
                self.assertFalse('Foo'.isupper())

        def test_split(self):
                s = 'hello world'
                self.assertEqual(s.split(), ['hello', 'world'])
                # check that s.split fails when the separator is not a string
                with self.assertRaises(TypeError):
                        s.split(2)

#if __name__ == '__main__':
#        unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
unittest.TextTestRunner(verbosity=2).run(suite)