import unittest

class simpleTest2(unittest.TestCase):
    def setUp(self):
        self.a=10
        self.b=20
        name=self.shortDescription()
        if name=="Add":
            self.a=10
            self.b=20
            print (name, self.a, self.b)

        if name=="sub":
            self.a=50
            self.b=60
            print (name, self.a, self.b)

    def tearDown(self):
        print ('\nend of test',self.shortDescription())

#    @unittest.skip("reason for skipping")
    def testadd(self):
        """Add"""
        result=self.a+self.b
        self.assertTrue(result==30)

    def testsub(self):
        """sub"""
        result=self.a-self.b
        self.assertTrue(result==-10)

#if __name__ == '__main__':
#    unittest.main()

# Store the detailed report in the file#
fh=open("TestReport.txt",'w')
suite = unittest.TestLoader().loadTestsFromTestCase(simpleTest2)
unittest.TextTestRunner(stream=fh,verbosity=2).run(suite)
fh.close()

