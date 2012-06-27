import unittest
import pymock
import FizzBuzz
"""
Q5. Write the psuedocode for the test_repport method, such that it uses PyMock
    mock objects to test the report method of FizzBuzz. [5 pts]
"""
class TestFizzBuzzMocked(pymock.PyMockTestCase):
        
    def setUp(self):
        super(TestFizzBuzzMocked, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setUp TestFizzBuzzMocked"

    def tearDown(self):
        super(TestFizzBuzzMocked, self).tearDown()
        self.fb = None

    def test_report(self):

        #mock the file handle  
        MockInter = self.mock() 
        MockFile = self.mock()       
        self.expectAndReturn(MockInter.open('c:/temp/fizzbuzz_report.txt', 'w'), MockFile)   
        MockFile.write("3 fizz \n")       
        MockFile.close()       

        #replay       
        self.replay()   

        #call API      
        self.fb.report(numbers, FileOpener=MockInter.open)        

        # verify        
        self.verify()

if __name__ == "__main__":
    unittest.main()
