import pandas as pd
from data.models import *

class Storage:
    _id = None
    _id_file_name = "id.txt"

    _patients_list = None
    _patients_df_name = "patients.csv"
    
    _doctors_list = None
    _doctors_df_name = "doctors.csv"
    
    _appointments_list = None
    _appointments_df_name = "appointments.csv"
    
    _billing_list = None
    _billing_df_name = "billing.csv"
    
    @staticmethod
    def reload():
        Storage._id = 0
        try:
            f = open(Storage._id_file_name,'r')
            Storage._id= int(f.read())
            f.close()
        except:
            pass
        
        Storage._patients_list = []  
        try:
            df = pd.read_csv(Storage._patients_df_name)
            for index, row in df.iterrows():
                Storage._patients_list.append(PatientModel.fromSeries(row))   
        except:
            pass

        Storage._doctors_list = []  
        try:
            df = pd.read_csv(Storage._doctors_df_name)
            for index, row in df.iterrows():
                Storage._doctors_list.append(DoctorModel.fromSeries(row))   
        except:
            pass
            
        Storage._appointments_list = []  
        try:
            df = pd.read_csv(Storage._appointments_df_name)
            for index, row in df.iterrows():
                Storage._appointments_list.append(AppointmentModel.fromSeries(row))   
        except:
            pass
            
        Storage._billing_list = []  
        try:
            df = pd.read_csv(Storage._billing_df_name)
            for index, row in df.iterrows():
                Storage._billing_list.append(BillingModel.fromSeries(row))   
        except:
            pass

    @staticmethod
    def save():
        f = open(Storage._id_file_name,'w')
        f.write(str(Storage._id))
        f.close()
    
        _patients_series = []
        for item in Storage._patients_list:
            _patients_series.append(item.toSeries())
        if len(_patients_series) > 0:
            pd.DataFrame(_patients_series).to_csv(Storage._patients_df_name)
            
        _doctors_series = []
        for item in Storage._doctors_list:
            _doctors_series.append(item.toSeries())
        if len(_doctors_series) > 0:
            pd.DataFrame(_doctors_series).to_csv(Storage._doctors_df_name)

        _appointments_series = []
        for item in Storage._appointments_list:
            _appointments_series.append(item.toSeries())
        if len(_appointments_series) > 0:
            pd.DataFrame(_appointments_series).to_csv(Storage._appointments_df_name)

        _belling_series = []
        for item in Storage._billing_list:
            _belling_series.append(item.toSeries())
        if len(_belling_series) > 0:
            pd.DataFrame(_belling_series).to_csv(Storage._billing_df_name)
        
    @staticmethod
    def addPatient(name,age,phoneNo):
        new_id = Storage._id
        Storage._patients_list.append(PatientModel(name,age,new_id,phoneNo))
        Storage._id+=1
        Storage.save()
        return new_id
        
    @staticmethod
    def addDoctor(name,specialization,availableTimeList):
        new_id = Storage._id
        Storage._doctors_list.append(DoctorModel(name,new_id,specialization,availableTimeList))
        Storage._id+=1
        Storage.save()
        return new_id
        
    @staticmethod
    def addAppointment(doctorModel,paitentModel,time):
        Storage._appointments_list.append(AppointmentModel(doctorModel.getId(),paitentModel.getId(),time))
        Storage.save()
        
    @staticmethod
    def determineCost(doctorModel,paitentModel,time):
        cost = len(doctorModel.getSpecialization())*100
        cost -= len(doctorModel.getName())*30
        return cost
     
    @staticmethod
    def addBill(patientModel,money,doctorModel,time):
        Storage._billing_list.append(BillingModel(patientModel.getId(),money,doctorModel.getSpecialization(),time))
        Storage.save()
        
    @staticmethod       
    def getPatientsList():
        return Storage._patients_list
        
    @staticmethod       
    def getDoctors():
        return Storage._doctors_list
        
    @staticmethod       
    def getAppointmentsList():
        return Storage._appointments_list
        
    @staticmethod       
    def getBillsList():
        return Storage._billing_list

    @staticmethod       
    def getPatientWithId(id):
        for i in Storage._patients_list:
            if i.getId() == id:
                return i
        return None
            
    @staticmethod       
    def getDoctorWithId(id):
        for i in Storage._doctors_list:
            if i.getId() == id:
                return i
        return None
         