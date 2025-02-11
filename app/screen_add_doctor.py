from app.screen import *
from app.navigator import *
import app
from data.storage import *

class ScreenAddDoctors(Screen):
    def display(self):
        all_available_times = "Monday,Tuesday,Wednesday,Thursday,Friday".split(',')        
        selected_available = []
        
        name = super().scanStr("Enter Name: ")   
        specialization = super().scanStr("Enter specialization: ")
        
        super().print("All Available times: ")
        for i,j in enumerate(all_available_times):
            super().print(f"{i}  {j}")
        super().print(" ")
        
        super().print("Press nubmers on Keyboard to select your days: ")
        while True:
            super().print("\r"+", ".join(selected_available) + ' '*20,end='')
            c = super().waitKey()
            if c.isdigit():
                n = int(c)
                if n < len(all_available_times):
                    d = all_available_times[n]
                    if d in selected_available:
                        selected_available.remove(d)
                    else:
                        selected_available.append(d)
            elif c == b'\r':
                break
        
        if len(selected_available)==0:
            super().print('')
            super().print(f"failed, no time selected")           
        else:
            id = Storage.addDoctor(name,specialization,selected_available)
            
            super().print('')
            super().print(f"Created successfully with id={id}")
            
        super().waitKeyToReturn()
        NavigatorPop()