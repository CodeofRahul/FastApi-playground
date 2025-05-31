from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("updated")

Patient_info = {'name': 'nitish','email':'abc@icici.com', 'age':65, 'weight': '75.2', 'married':True, 'allergies': ['pollen', 'dust'], 'contact_details':{ 'phone': '35367744', 'emergency':'345464645'}}

patient1 = Patient(**Patient_info)

update_patient_data(patient1)