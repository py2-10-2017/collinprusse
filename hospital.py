class patient(object):
    idnum = 1
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.idnum = patient.idnum
        patient.idnum += 1



class hospital(object):
    def __init__(self, hosname, capacity):
        self.patients = []
        self.hosname = hosname
        self.capacity = capacity
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            for i in range(1, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_number = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} was admitted to bed #{}".format(patient.idnum, patient.bed_number)

        else:
            print "Hospital is at capacity"



    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.idnum == patient_id:

                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_number:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                print "Patient #{} sucessfully discharged.".format(patient.idnum)
            else:
                print "Patient not found"


patient1 = patient("Gary", "Morphine")
hos1 = hospital("Fancy Hospital", 5)
hos1.admit(patient1)
hos1.discharge(1)
