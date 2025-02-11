from app.screen import *
from app.navigator import *
import app

from data.storage import *

class ScreenShowBills(Screen):
    def display(self):
        print("{:2} {:15} {:10} {:5} {:15} {}".format("  ","Patient","patient ID","Cost","Type", "Time"))
        for i,item in enumerate(Storage.getBillsList()):
            pat_name = Storage.getPatientWithId(item.getPatientId())
            if pat_name == None:
                pat_name = 'undefined'
            else:
                pat_name=pat_name.getName()
        
            print("{:2} {:15} {:10} {:5} {:15} {}".format(i,pat_name,item.getPatientId(),item.getMoney(),item.getSpecialization(),item.getTime()))
            super().wait(0.1)
        print(' ')
   
        super().waitKeyToReturn()
        NavigatorPop()