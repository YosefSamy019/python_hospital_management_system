from app.screen import *
from app.navigator import *
import app

from data.storage import *

class ScreenShowPatients(Screen):
    def display(self):
        print("{:2} {:10} {:3} {:3} {}".format("  ","Name","ID","Age","Phone No"))
        for i,item in enumerate(Storage.getPatientsList()):
            print("{:2} {:10} {:3} {:3} {}".format(i,item.getName(),item.getId(),item.getAge(),item.getPhoneNo()))
            super().wait(0.1)
        print(' ')
   
        super().waitKeyToReturn()
        NavigatorPop()