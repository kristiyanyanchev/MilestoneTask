import unittest

def main():
    print(getName(3581))

def greeting(name: str) -> str:
    return 'Hello ' + name

def getNameDigit(digit: int ) -> str:
    if digit < 0 or digit > 9 :
        raise TypeError()
    if digit == 0:
        return "zero"
    elif digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:

        return "nine"
    
def getName(number:int) -> str:
    if number > 9:
        return getName(number // 10) + ", " + getNameDigit(number % 10)
    else:
        return getNameDigit(number)


class TestNameMethods(unittest.TestCase):
    def testGetNameDigit(self):
        self.assertEqual(getNameDigit(1),"one")
        self.assertEqual(getNameDigit(2),"two")
        self.assertEqual(getNameDigit(3),"three")
        self.assertEqual(getNameDigit(4),"four")
        self.assertEqual(getNameDigit(5),"five")
        self.assertEqual(getNameDigit(6),"six")
        self.assertEqual(getNameDigit(7),"seven")
        self.assertEqual(getNameDigit(8),"eight")
        self.assertEqual(getNameDigit(9),"nine")
        self.assertEqual(getNameDigit(0),"zero")
        
        with self.assertRaises(TypeError):
            getNameDigit(-1)

    def testGetName(self):
        self.assertEqual(getName(3581),"three, five, eight, one")

        with self.assertRaises(TypeError):
            getName(-1)
        
if __name__ == "__main__":
    unittest.main()
