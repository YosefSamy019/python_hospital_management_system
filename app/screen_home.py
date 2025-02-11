from app.screen import *
from app.navigator import *
import app
import app.screen_add_doctor
import app.screen_add_patient
import app.screen_reserve_appointment
import app.screen_settings
import app.screen_show_appointments
import app.screen_show_bills
import app.screen_show_doctors
import app.screen_show_patients

class ScreenHome(Screen):
    def display(self):
    
        intro = '''
Name:         Youssef Samy Youssef
Supervisior:  DEPI
Comapny:      CLS
Group:        QAL2_AIS2_S1
Date:         28/12/2024'''
        super().print(intro,'\n')

        f = []
        f.append('add patient')
        f.append('add doctor')
        f.append('reserve appointment')
        f.append('show patients')
        f.append('show doctors')
        f.append('show appointments')
        f.append('show bills')        
        f.append('settings')
        f.append('exit')
        super().printMenu(f)
        
        num = super().scanIntRange(len(f))
        
        if num == 0:
          NavigatorPush(app.screen_add_patient.ScreenAddPatients())
        elif num == 1:
          NavigatorPush(app.screen_add_doctor.ScreenAddDoctors())        
        elif num == 2:
          NavigatorPush(app.screen_reserve_appointment.ScreenReserveAppointment())        
        elif num == 3:
          NavigatorPush(app.screen_show_patients.ScreenShowPatients())        
        elif num == 4:
          NavigatorPush(app.screen_show_doctors.ScreenShowDoctors())        
        elif num == 5:
          NavigatorPush(app.screen_show_appointments.ScreenShowAppointment())        
        elif num == 6:
          NavigatorPush(app.screen_show_bills.ScreenShowBills())        
        elif num == 7:
          NavigatorPush(app.screen_settings.ScreenSettings())        
        elif num == 8:
          exit(0)    
   