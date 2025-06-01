from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump()    # to convert the existing pydantic model into dict
# temp = patient1.model_dump(include=['name', 'gender'])    # to convert the existing pydantic model into dict
# temp = patient1.model_dump(exclude=['name', 'gender'])    # to convert the existing pydantic model into dict
# temp = patient1.model_dump(exclude={'address':['state']})    # to convert the existing pydantic model into dict
temp = patient1.model_dump(exclude_unset=True)    # to convert the existing pydantic model into dict
# temp = patient1.model_dump_json()   # to convert the existing pydantic model into Json

print(temp)
print(type(temp))
