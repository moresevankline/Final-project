import Read_Hospital_Excel_Sheet

Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()
Patients_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()

class Hospital:

    def hospital_department():
        for i in Doctors_DataBase:
            print(" " + Doctors_DataBase[i][0][0])

    def hospital_doctors():
        for i in Doctors_DataBase:
            print (" " + Doctors_DataBase[i][0][1] + " in " + Doctors_DataBase[i][0][0] + 
                    " department, from " + Doctors_DataBase[i][0][2])
    
    def hospital_residents():
        for i in Patients_DataBase:
            print("Patient : " + Patients_DataBase[i][2] + " in " + Patients_DataBase[i][0]
                + " department and followed by " + Patients_DataBase[i][1] + ", age : "
                + Patients_DataBase[i][3] + ", from " + Patients_DataBase[i][5] + ", Room Number : "
                + Patients_DataBase[i][6])
