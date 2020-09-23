# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:50:24 2020

@author: Niranch
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstname,lastname,idnumber,*scores):
        self.Scores=scores
        #Person.__init__(self, firstname,lastname,idnumber)
        super().__init__(firstname,lastname,idnumber)
        
    def calculate(self):
        return sum(self.Scores)/len(self.Scores)
    
stuobj=Student("Nir","Raj",10,80,90,95,100)
print(stuobj.calculate())