from app.screen import *
from app.navigator import *
import app
from data.storage import *

class ScreenReserveAppointment(Screen):
    def display(self):
        docs = Storage.getDoctors()
        patients = Storage.getPatientsList()
    
        super().print("Patients: ")
        super().print("{:2} {:10} {:3} {:3} {}".format("  ","Name","ID","Age","Phone No"))
        for i,item in enumerate(patients):
            print("{:2} {:10} {:3} {:3} {}".format(i,item.getName(),item.getId(),item.getAge(),item.getPhoneNo()))
            super().wait(0.1)
        super().print(' ')
        selected_pat = super().scanIntRange(len(patients),title="Select patient: ")
        
        
        
        super().print("\nDoctors: ")
        super().print("{:2} {:10} {:3} {:16} {}".format("  ","Name","ID","Specialization","Time"))
        for i,item in enumerate(docs):
            super().print("{:2} {:10} {:3} {:16} {}".format(i,item.getName(),item.getId(),item.getSpecialization()," ".join(item.getAvailableTimeList())))
            super().wait(0.1)
        super().print(' ')
        selected_doc = super().scanIntRange(len(patients),title="Select Doctor: ")
        
        
        
        NavigatorFlushTerminal()
        selected_pat = patients[selected_pat]
        selected_doc = docs[selected_doc]
        
        
        
        super().print("Selected Patient: ",selected_pat.getName())
        super().print("Selected Doctor: ",selected_doc.getName())
        
        super().print("Availble Time due to doctor schedule: ")
        for i,item in enumerate(selected_doc.getAvailableTimeList()):
            super().print("\t{:2} {}".format(i,item))
            super().wait(0.1)
        time_index = super().scanIntRange(len(selected_doc.getAvailableTimeList()),"Enter Time index: ")

        cost = Storage.determineCost(selected_doc,selected_pat,selected_doc.getAvailableTimeList()[time_index])
        super().print(f'The cost is {cost}, Do you wnat to reserve ?')
        super().printMenu(['Cancel','Ok'])
        cost_agree = super().scanIntRange(2)
        
        
        if cost_agree==1:
            Storage.addAppointment(selected_doc,selected_pat,selected_doc.getAvailableTimeList()[time_index])    
            Storage.addBill(selected_pat, cost, selected_doc,selected_doc.getAvailableTimeList()[time_index] )    
            super().print('')
            super().print(f"Created successfully")
        else:
            super().print('')
            super().print(f"Opeartion Canceled")

        super().waitKeyToReturn()
        NavigatorPop() 
        
    
    