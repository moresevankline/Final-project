import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet
from datetime import date


Patients_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

class Patient:
    def age(birthdate):
        today = date.today()
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        year_difference = today.year - birthdate.year
        age = year_difference - one_or_zero
        return age

    def add_patient():
        try:  # To avoid non integer input
            patient_ID = int("1101")
            for patient_ID in Patients_DataBase:
                patient_ID += 1
            print("")
            print("Patient ID: " + str(patient_ID))
            DepartmentList = ["Medicine", "Neurology", "Surgery", "Cardiology"]
            print("")
            print(f"Departments: {DepartmentList}".replace('\'','').replace('[','').replace(']','').replace(',',' / '))
            print("")
            Department = input("Enter patient department : ")
            print("Available Doctor/s: ")
            for key, values in Doctors_DataBase.items():
                if Department in values[0][0]:
                    print(f"Doctor ID: {key} | Doctor Name: {values[0][1]}")
                    DoctorName = "Available"
                else:
                    DoctorName = "No Doctor Avaiable"
            if DoctorName != "No Doctor Available":
                DoctorName = input("Enter doctor name : ")
            elif DoctorName == "No Doctor Available":
                print(DoctorName)
            print("")
            Name = input("Enter patient name : ")
            print("")
            Year = int(input("Enter patient birth year: "))
            while len(str(Year)) != 4:
                Year = int(input("Invalid year, Please enter birth year: "))
            Month = int(input("Enter patient birth month: "))
            while len(str(Month)) > 2:
               Month = int(input("Invalid month, Please enter birth month: "))
            Day = int(input("Enter patient birth day: "))
            while len(str(Day)) > 2:
                Day = int(input("Invalid day, Please enter birth day: "))
            Age = str(Patient.age(date((Year),(Month),(Day))))
            while True:
                print("")
                print("Male or Female")
                Gender = input("Enter patient gender: ")
                if Gender == "Male" or Gender == "male":
                    Gender = "Male"
                    break
                elif Gender == "Female" or Gender == "female":
                    Gender = "Female"
                    break
                else:
                    print("Invalid Gender")
            print("")
            City = input("Enter patient city : ")
            Patients_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, City]
            print("")
            print("/" + 21*'-' + "Patient added successfully" + 21*'-' + "/")
        except:
            print("Invalid Input, Please try again")
        Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)

    def display_patient():
        for key, values in Patients_DataBase.items():
            print(f"Patient ID: {key} | Patient Name: {values[2]}")
        try:  # To avoid non integer input
            if len(Patients_DataBase) != 0:
                patient_ID = int(input("Enter patient ID : "))
                while patient_ID not in Patients_DataBase:
                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                print("\nPatient name        : ", Patients_DataBase[patient_ID][2])
                print("Patient age         : ", Patients_DataBase[patient_ID][3])
                print("Patient gender      : ", Patients_DataBase[patient_ID][4])
                print("Patient city        : ", Patients_DataBase[patient_ID][5])
                print("Patient is in " + Patients_DataBase[patient_ID][0] + " department")
                print("Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
            elif len(Patients_DataBase) == 0:
                print("No available data to display")
        except:
            print("Patient ID should be an integer number")

    def delete_patient():
        for key, values in Patients_DataBase.items():
            print(f"Patient ID: {key} | Patient Name: {values[2]} | Patient Age: {values[3]} | Patient Gender: {values[4]} | Patient city: {values[5]}")
        try:  # To avoid non integer input
            if len(Patients_DataBase) != 0:
                patient_ID = int(input("Enter patient ID : "))
                while patient_ID not in Patients_DataBase:
                    print("Patient ID not found")
                    patient_ID = int(input("Please Enter patient ID : "))
                Patients_DataBase.pop(patient_ID)
                print("")
                print("/" + 21*'-' + "Patient data deleted successfully" + 21*'-' + "/")
            elif len(Patients_DataBase) == 0:
                print("No available data to be deleted")
        except:
            print("Patient ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)

    def edit_patient():
        for key, values in Patients_DataBase.items():
            print(f"Patient ID: {key} | Patient Name: {values[2]} | Patient Age: {values[3]} | Patient Gender: {values[4]} | Patient city: {values[5]}")
        try:  # To avoid non integer input
            if len(Patients_DataBase) != 0:
                while True:
                    print("")
                    patient_ID = int(input("Enter patient ID : "))
                    if patient_ID not in Patients_DataBase:
                        patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                    print("\nPatient name        : ", Patients_DataBase[patient_ID][2])
                    print("Patient age         : ", Patients_DataBase[patient_ID][3])
                    print("Patient gender      : ", Patients_DataBase[patient_ID][4])
                    print("Patient city        : ", Patients_DataBase[patient_ID][5])
                    print("Patient is in " + Patients_DataBase[patient_ID][0] + " department")
                    print("Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
                    print("")
                    print("                ------------------------------------------")
                    print("                |1. To Edit Patient Department           |")
                    print("                |   To Edit Doctor Following case        |")
                    print("                |2. To Edit Patient Name                 |")
                    print("                |3. To Edit Patient Gender               |")
                    print("                |4. To Edit Patient City                 |")
                    print("                |To be Back Enter B                      |")
                    print("                -----------------------------------------")
                    print("")
                    Admin_choice = input("Enter your choice : ")
                    
                    if Admin_choice == "1":
                        print("")
                        DepartmentList = ["Medicine", "Neurology", "Surgery", "Cardiology"]
                        print(f"Departments: {DepartmentList}".replace('\'','').replace('[','').replace(']','').replace(',',' / '))
                        Department = input("Enter patient department : ")
                        while Department not in DepartmentList:
                            print("Invalid Input")
                            Department = input("Enter patient department : ")
                        Patients_DataBase[patient_ID][0] = Department
                        print("")
                        print("/" + 21*'-' + "Patient Department edited successfully" + 21*'-' + "/")
                        while Department not in DepartmentList:
                            print("Invalid Input")
                            Department = input("Enter patient department : ")
                        print("")
                        print("Available Doctor/s: ")
                        for key, values in Doctors_DataBase.items():
                            if Department in values[0][0]:
                                print(f"Doctor ID: {key} | Doctor Name: {values[0][1]}")
                                DoctorName = "Available"
                            if Department not in values[0][0]:
                                DoctorName = "No Doctor Available"
                                break
                        if DoctorName != "No Doctor Available":
                            DoctorName = input("Enter doctor name : ")
                        elif DoctorName == "No Doctor Available":
                            print(DoctorName)
                        Patients_DataBase[patient_ID][1] = DoctorName
                        print("")
                        print("/" + 21*'-' + "Doctor following case edited successfully" + 21*'-' + "/")

                    elif Admin_choice == "2":
                        Patients_DataBase[patient_ID][2] = input("\nEnter patient name : ")
                        print("")
                        print("/" + 21*'-' + "Patient name edited successfully" + 21*'-' + "/")

                    elif Admin_choice == "3":
                        Patients_DataBase[patient_ID][4] = input("\nEnter patient gender : ")
                        print("")
                        print("/" + 21*'-' + "Patient gender edited successfully" + 21*'-' + "/")

                    elif Admin_choice == "4":
                        Patients_DataBase[patient_ID][5] = input("\nEnter patient city : ")
                        print("")
                        print("/" + 21*'-' + "Patient city edited successfully" + 21*'-' + "/")
                        
                    if Admin_choice == "B":
                        break

                    else:
                        print("")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

            elif len(Patients_DataBase) == 0:
                print("No available data to be edited")
            
        except:
            print("Patient ID should be an integer number")

    def patient_menu():
        print("")
        print("                -----------------------------------------")
        print("                |1. To add new patient data             |")
        print("                |2. To display patient data             |")
        print("                |3. To delete patient data              |")
        print("                |4. To edit patient data                |")
        print("                |To Exit enter B                        |")
        print("                -----------------------------------------")
            
            

