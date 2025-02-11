from app.screen import *
from app.navigator import *
import app
from data.storage import *

class ScreenAddPatients(Screen):
    def display(self):
        name = super().scanStr("Enter Name: ")   
        age = super().scanInt("Enter Age: ")   
        phoneNo = super().scanInt("Enter Phone: ")
        
        id = Storage.addPatient(name,age,phoneNo)
        
        super().print('')
        super().print(f"Created successfully with id={id}")
        
        super().waitKeyToReturn()
        NavigatorPop()