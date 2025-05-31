from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Rahul'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    # allergies: Optional[List[str]] = None   # make it Optional
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]    # Defining the length of list item
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("inserted")

# Patient_info = {'name': 'nitish', 'age':30, 'weight': '75.2', 'married':True, 'allergies': ['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone': '35367744'}}

Patient_info = {'name': 'nitish','email':'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/22554', 'age':30, 'weight': 75.2, 'contact_details':{'phone': '35367744'}}         # without allergies and married

Patient1 = Patient(**Patient_info)

insert_patient_data(Patient1)
