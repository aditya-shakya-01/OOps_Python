
# Doctor And Patient

class Doctor:
    def __init__(self,name,specialization):
        self.name=name
        self.specialization=specialization

class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self,doctor):
        print(f"Patient Name : {self.name}")
        print(f"Patient Age : {self.age}")
        print(f"Doctor Name : {doctor.name}")
        print(f"Specialization : {doctor.specialization}")

doctor=Doctor("Tarun Mittal","Neuro Surgeon")
patient=Patient("Vinay",49)

patient.show(doctor)