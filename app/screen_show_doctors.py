from app.screen import *
from app.navigator import *
import app

from data.storage import *

class ScreenShowDoctors(Screen):
    def display(self):
        print("{:2} {:10} {:3} {:16} {}".format("  ","Name","ID","Specialization","Time"))
        for i,item in enumerate(Storage.getDoctors()):
            print("{:2} {:10} {:3} {:16} {}".format(i,item.getName(),item.getId(),item.getSpecialization()," ".join(item.getAvailableTimeList())))
            super().wait(0.1)
        print(' ')
        
        super().waitKeyToReturn()
        NavigatorPop()       
   