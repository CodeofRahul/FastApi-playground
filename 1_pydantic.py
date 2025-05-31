from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("inserted")

Patient_info = {'name': 'nitish', 'age':30}

Patient1 = Patient(**Patient_info)

insert_patient_data(Patient1)
