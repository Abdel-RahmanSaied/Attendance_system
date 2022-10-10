import os

from students import STUDENTS
from subjects import SUBJECTS
import datetime
import csv

instractions = '''
##########################
** end -> for end session 
** add -> for add new user 
########################
'''
print(instractions)

session_info = SUBJECTS().get_period_info()
period_name = session_info["current_period_name"]
subject_name = session_info["subject_name"]
subject_doctorName = session_info["subject_doctorName"]

students_attendance = {}

session_inprogress = True

while session_inprogress :
    time = datetime.datetime.now().time()
    student_id = str(input("enter student id : "))
    if student_id == "end" :
        file_name = subject_name + " " + period_name + " " + subject_doctorName + ".csv"
        with open(file_name, "w") as csv_file:
            wr = csv.DictWriter(csv_file, fieldnames=["Student Name", "Enter Time"])
            wr.writeheader()
            for student in students_attendance.keys():
                studentID = student
                entering_time = students_attendance[studentID]
                wr.writerow({"Student Name": studentID, "Enter Time": entering_time})
            session_inprogress = False

    elif student_id == "add" :
        student_ID =  str(input("enter student id to register : "))
        subjects_count = int(input("enter count of subjects  : "))
        subjects = []
        for i in range(subjects_count) :
            subject =  input(f"please enter  subject {i} : ")
            subjects.append(subject)
        units =  int(input("enter the units : "))
        print(STUDENTS().addStudent(student_ID,subjects, units))
        print("*"*50)

    else:
        students_attendance[student_id] = time





