import json
import time
import datetime
class SUBJECTS():
    def __init__(self ):

        self.hall_number = str(input("please enter hall number : ") )
        with open("db/halls_db.json", "r") as file :
            self.db = json.load(file)
        self.info = self.get_period_info()

    def get_period_info(self ):
        try :
            #current_time = datetime.datetime.now().time()
            current_time = datetime.datetime.strptime("10:13" , "%H:%M").time()
            for per_info in self.db[self.hall_number] :
                start_time = datetime.datetime.strptime( self.db[self.hall_number][per_info]['time']['from'] , "%H:%M").time()
                end_time = datetime.datetime.strptime( self.db[self.hall_number][per_info]['time']['to'] , "%H:%M").time()

                if start_time <= current_time <= end_time  :
                    current_period_name = per_info
                    subject_name = self.db[self.hall_number][per_info]["subject_name"]
                    subject_doctorName = self.db[self.hall_number][per_info]["doctor_name"]
                    period_info = {"current_period_name": current_period_name ,"subject_name":subject_name  , "subject_doctorName":subject_doctorName}

                    return period_info
        except Exception as e :
            return f"hall number {e} was invalid"


# print(SUBJECTS().info)