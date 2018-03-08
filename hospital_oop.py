# pylint: disable=print-statement
class Patients(object):
    def __init__(self, idnum, name, *allergies):
        self.id = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = 'none'

    def displaypatinfo(self):
        print "Patient id is {}, name is {}, allergies is/are {}, and bednum is {}.".format(self.id, self.name, self.allergies, self.bednum)
        return self

patient1 = Patients(1, 'Trey', 'peanuts', 'bees')
patient2 = Patients(2, 'Bobby', 'none')
patient3 = Patients(3, 'Lisa', 'tree nuts')
patient4 = Patients(4, 'barb', 'gluten')
patient5 = Patients(5, 'Tommy', 'stonefruit', 'peanuts')
patient6 = Patients(6, 'Cher', 'honey')
patient1.displaypatinfo()

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patientlist = []
    
    def admitp(self, patient):
        if len(self.patientlist) >= self.capacity:
            print "The hosptial is at capacity. Patient {} cannot be admitted".format(patient.name)
        else: 
            self.patientlist.append(patient)
            patient.bednum = len(self.patientlist)
            print "Admission of patient {} to bed {} is complete.".format(patient.name, patient.bednum)
        return self 

    def discharge(self, name):
        for people in self.patientlist:
            if people.name == name:
                self.patientlist.remove(people)
                people.bednum = 'none'
                print "Patient {} was discharged from the hospital.".format(people.name)
        return self

hospital1 = Hospital('Urgent Care Bellevue', 5)
hospital1.admitp(patient1).admitp(patient2).admitp(patient3).admitp(patient4).admitp(patient5).admitp(patient6).discharge('Trey').admitp(patient6)
