from app.screen import *
from app.navigator import *
import app

from data.storage import *

class ScreenShowAppointment(Screen):
    def display(self):
        print("{:2} {:10} {:10} {:15} {}".format("  ","Doctor ID","Patient ID","Type","Time"))
        for i,item in enumerate(Storage.getAppointmentsList()):
            doc_name = Storage.getDoctorWithId(item.getDoctorId())
            if doc_name == None:
                doc_name = 'undefined'
                doc_type='undefined'
            else:
                doc_type=doc_name.getSpecialization()
                doc_name = doc_name.getName()
        
            pat_name = Storage.getPatientWithId(item.getPatientId())
            if pat_name == None:
                pat_name = 'undefined'
            else:
                pat_name = pat_name.getName()
                
            print("{:2} {:10} {:10} {:15} {}".format(i,doc_name,pat_name,doc_type,item.getTime()))
            super().wait(0.1)
        print(' ')
        
        super().waitKeyToReturn()
        NavigatorPop()    