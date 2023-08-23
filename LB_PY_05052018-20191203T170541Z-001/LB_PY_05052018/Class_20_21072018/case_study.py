import unittest
from pathlib import Path
from src_mod import *

def CheckConfig(src,str):
    fileobj = open(src, "r")
    val=str+'\n'
    for line in fileobj:
        if(line == val):
            fileobj.close()
            return True
    return False

CONFIG_FILE_DEFAULT="C:\\Users\\mavin\\Desktop\\config_file"
CONFIG_FILE="C:\\Users\\mavin\\Desktop\\Test\\config_file"

class configtest(unittest.TestCase):
    def setUp(self):
        name = self.shortDescription()
        if name == "CopyConfig":
            fileobj=open(CONFIG_FILE_DEFAULT,"w+")
            fileobj.write("#This is a configuration file\n")
            fileobj.write("CONFIG_ENABLE=False\n")
            fileobj.write("CONFIG_DATA1=100\n")
            fileobj.write("CONFIG_DATA2=150\n")
            fileobj.close()

    def tearDown(self):
        name = self.shortDescription()
        if name == "CopyConfig":
            os.remove(CONFIG_FILE_DEFAULT)

    def testcopyconfig(self):
        """CopyConfig"""
        CopyConfig(CONFIG_FILE_DEFAULT,CONFIG_FILE)
        result=Path(CONFIG_FILE).is_file()
        self.assertTrue(result==True)

    def testenableconfig(self):
        """EnableConfig"""
        ChangeConfig(CONFIG_FILE,"CONFIG_ENABLE","False","True")
        result=CheckConfig(CONFIG_FILE,"CONFIG_ENABLE=True")
        self.assertTrue(result==True)

    def testupdateconfig(self):
        """UpdateConfig"""
        ChangeConfig(CONFIG_FILE, "CONFIG_DATA1", "100", "50")
        result = CheckConfig(CONFIG_FILE, "CONFIG_DATA1=50")
        self.assertTrue(result == True)

    def testappendconfig(self):
        """AppendConfig"""
        AppendConfig(CONFIG_FILE,"CONFIG_DATA3=350")
        result = CheckConfig(CONFIG_FILE, "CONFIG_DATA3=350")
        self.assertTrue(result == True)

    def testdeleteconfig(self):
        """DeleteConfig"""
        DeleteConfig(CONFIG_FILE,"CONFIG_DATA2=150")
        result = CheckConfig(CONFIG_FILE, "CONFIG_DATA2=150")
        self.assertTrue(result == False)

#if __name__ == '__main__':
#    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(configtest)
unittest.TextTestRunner(verbosity=2).run(suite)
