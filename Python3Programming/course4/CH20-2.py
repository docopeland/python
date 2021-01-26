import unittest

# code provided that i need to write tests for
def lr(n): return list(range(n))

def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])

class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM


# tests for function mySum
class TestingmySum(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(mySum([]), 0)

    def testOneValList(self):
        self.assertEqual(mySum([1]), 1)

    def testPosList(self):
        self.assertEqual(mySum([1, 2, 3]), 6)

    def testNegList(self):
        self.assertEqual(mySum([-1, -2, -3]), -6)

# tests for class Student
class TestingStudent(unittest.TestCase):
    def testS1name(self):
        s1 = Student("danielle")
        self.assertEqual(s1.name,"danielle")

    def testS1years(self):
        s1 = Student("danielle")
        self.assertEqual(s1.years_UM,1)

    def testS1Knowledge(self):
        s1 = Student("danielle")
        self.assertEqual(s1.knowledge,0)

    def testS1Study(self):
        s1 = Student("danielle")
        self.assertEqual(s1.study(),None)

    def testS1StudyKnowledge(self):
        s1 = Student("danielle")
        s1.study()
        self.assertEqual(s1.knowledge,1)

    def testS1GetKnowledge(self):
        s1 = Student("danielle")
        self.assertEqual(s1.getKnowledge(),1)

    def testS1YearAtUmich(self):
        s1 = Student("danielle")
        self.assertEqual(s1.year_at_umich(),1)

    def testS2name(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.name,"emily")

    def testS2years(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.years_UM,3)

    def testS2Knowledge(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.knowledge,0)

    def testS2Study(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.study(),None)

    def testS2StudyKnowledge(self):
        s2 = Student("emily",3)
        s2.study()
        self.assertEqual(s2.knowledge,1)

    def testS2GetKnowledge(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.getKnowledge(),1)

    def testS2YearAtUmich(self):
        s2 = Student("emily",3)
        self.assertEqual(s2.year_at_umich(),3)

if __name__ == "__main__":
    unittest.main()