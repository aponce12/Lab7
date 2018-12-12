import unittest
import Lab7

class TestLab(unittest.TestCase):
    
    def test_edit_distance(self):
        string = ["Pittsburgh","Pennsylvania",
          "Tucson","Arizona",
          "Cincinnati","Ohio",
          "Albuquerque","New Mexico",
          "Culpeper","Virginia",
          "Asheville","North Carolina",
          "Worcester","Massachusetts",
          "Manhattan","New York",
          "Phoenix","Arizona",
          "Niagara Falls","New York"]
##        string1 = "Sunday"
##        string2 = "Saturday"
        for i in range (len(string)):
            if i+1==len(string):
                return
            string1=string[i]
            string2=string[i+1]
            print(string1,string2)
            Lab7.edit_distance(string1, string2, len(string1), len(string2))
        

if __name__ == '__main__':
    unittest.main()
