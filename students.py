import json

class STUDENTS() :
    def __init__(self):
        self.student_db_path = "db/students_db.json"
        self.students = {}

    def sync_db(self):
        with open(self.student_db_path , "r") as studentFile:
            student_db = json.load(studentFile)
        self.students = student_db

    def addStudent(self , student_id , subjects:list , units:int):
        self.sync_db()
        try :
            self.students[student_id]={"subjects":subjects , "units":units}
            with open(self.student_db_path , "w") as file :
                json.dump(self.students , file , indent= 4)
            return "Student added successfully"
        except Exception as e:
            return "Failed to add " , e

    def get_students(self):
        self.sync_db()
        return self.students


# obj = STUDENTS()
# student1 = obj.addStudent("42018113315" , [] , 90)

