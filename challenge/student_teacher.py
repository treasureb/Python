#! /usr/bin/env
#coding=utf-8

import sys
from collections import Counter

class Person(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def get_details(self):
        return self.name
    def get_grade(self):
        return sele.grade

class Student(Person):
    def __init__(self,name,branch,year,grade):
        Person.__init__(self,name,grade)
        self.brach = brach
        self.year = yaer
    def get_details(self):
        return "{} studies {} and is in {}year.".format(self.name,self.branch,self.year)
    def get_grade(self):
        c = Counter(self.grade)
        return "Pass:{},Fail:{}".format(c['A']+c['B']+c['C'],c['D'])
class Teacher(Person):
    def __init__(self,name,papaers,grade):
        Person.__init__(self,name,grade)
        self.papaers = papers
    def get_det_details(self):
        return "{} teaches {}".format(self.name,','.join(self.papaers))
    def get_grade(self):
        c = Counter(self.grade).most_common()
        s = ["{}:{}".format(x,y) for x,y in c]
        return ','.join(s)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Wrong Parameter!")
        sys.exit(1)
    if(sys.argv[1] == 'student'):
        student = Student("Kane","CSE",2016,sys.argv[2])
        print(student.get_grade())
    else:
        teacher = Teacher("jjj",['C++'],sys.argv[2])
        print(teacher.get_grade())
