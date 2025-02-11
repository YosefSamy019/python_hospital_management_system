import pandas as pd


class PatientModel:
    @staticmethod
    def fromSeries(series):
        return PatientModel(series['name'],series['age'],series['id'],series['phoneNo'])

    def __init__(self,name, age,id,phoneNo):
        self._name = name
        self._id = id
        self._age = age
        self._phoneNo = phoneNo
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
        
    def getId(self):
        return self._id
        
    def getPhoneNo(self):
        return self._phoneNo
        
    def toSeries(self):
        return pd.Series([self._name,self._age,self._id,self._phoneNo],['name', 'age', 'id', 'phoneNo'])
        
        
class DoctorModel:
    @staticmethod
    def fromSeries(series):
        return DoctorModel(series['name'],series['id'],series['specialization'],str(series['availableTimeList']).split('#'))

    def __init__(self,name,id,specialization,availableTimeList):
        self._name = name
        self._id = id        
        self._specialization = specialization 
        self._availableTimeList = availableTimeList
        
    def getName(self):
        return self._name
        
    def getId(self):
        return self._id
        
    def getSpecialization(self):
        return self._specialization
        
    def getAvailableTimeList(self):
        return self._availableTimeList
        
    def toSeries(self):
        return pd.Series([self._name,self._id,self._specialization,"#".join(self._availableTimeList)],\
        ['name', 'id', 'specialization', 'availableTimeList'])
            
        
class AppointmentModel:
    @staticmethod
    def fromSeries(series):
        return AppointmentModel(series['doctorId'],series['patientId'],series['time'])

    def __init__(self,doctorId,patientId,time):
        self._doctorId =doctorId
        self._patientId =patientId
        self._time =time

    def getDoctorId(self):
        return self._doctorId
        
    def getPatientId(self):
        return self._patientId
        
    def getTime(self):
        return self._time        
        
    def toSeries(self):
        return pd.Series([self._doctorId,self._patientId,self._time],\
        ['doctorId', 'patientId', 'time'])    


class BillingModel:
    @staticmethod
    def fromSeries(series):
        return BillingModel(series['patientId'],series['money'],series['specialization'],series['time'])

    def __init__(self,patientId,money,specialization,time):
        self._money =money
        self._patientId =patientId
        self._specialization =specialization
        self._time = time

    def getMoney(self):
        return self._money
        
    def getPatientId(self):
        return self._patientId
        
    def getSpecialization(self):
        return self._specialization
            
    def getTime(self):
        return self._time
    def toSeries(self):
        return pd.Series([self._patientId,self._money,self._specialization,self._time],\
        ['patientId', 'money', 'specialization','time'])    
