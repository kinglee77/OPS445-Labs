#!/usr/bin/env python3
# Author ID: lbrown63

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert number to string
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade


    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if len(self.courses) == 0: #check if the student has any course
            return 'GPA of student ' + self.name + ' is 0.0' #if no course, return a GPA 0.0
        gpa = 0.0
        for course in self.courses.keys(): #pepetition in each course in student records
            gpa = gpa + self.courses[course] #add grade of each course to the GPA vareible
        return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)) #calculatte the avarage GPA by dividing the total grade by nubmer of courses


    # Return a list of courses that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed_courses = [] #initial empty list to stored passed courses
        for course in self.courses:
            if self.courses[course] > 0.0: #check if the grade is greate than 0.0
                passed_courses.append(course) #add the course to the passed courses list
        else:  #this else will execute after the for loop completes normally
            return passed_courses #return the list of passed courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())