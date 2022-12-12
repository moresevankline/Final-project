import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

class Doctor:

    def add_doctor():
        try:  # To avoid non integer input
            doctor_ID = int("2101")
            for doctor_ID in Doctors_DataBase:
                doctor_ID += 1
            print("")
            print("Patient ID: " + str(doctor_ID))
            while doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                doctor_ID = int(input("This ID is unavailable, please try another ID : "))
            DepartmentList = ["Medicine", "Neurology", "Surgery", "Cardiology"]
            print("")
            print(f"Departments: {DepartmentList}".replace('\'','').replace('[','').replace(']','').replace(',',' / '))
            Department = input("Enter doctor department : ")
            while Department not in DepartmentList:
                print("Invalid Input")
                Department = input("Enter patient department : ")
            print("")
            Name = input("Enter doctor name       : ")
            City = input("Enter doctor city       : ")
            Doctors_DataBase[doctor_ID] = [[Department, Name, City]]
            print("")
            print(22*'-' + "Doctor added successfully" + 22*'-')
            print("")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def display_doctor():
        for key, values in Doctors_DataBase.items():
            print(f"Doctor ID: {key} | Doctor Name: {values[0][1]}")
        try:  # To avoid non integer input
            if len(Doctors_DataBase) != 0:
                doctor_ID = int(input("Enter doctor ID : "))
                while doctor_ID not in Doctors_DataBase:
                    doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                print("")
                print("Doctor name     :", Doctors_DataBase[doctor_ID][0][1])
                print("Doctor city     :", Doctors_DataBase[doctor_ID][0][2])
                print("Doctor is in " + Doctors_DataBase[doctor_ID][0][0] + " department")
            elif len(Doctors_DataBase) == 0:
                print("No available data to display")
        except:
            print("Doctor ID should be an integer number")
        

    def delete_doctor():
        for key, values in Doctors_DataBase.items():
            print(f"Doctor ID: {key} | Doctor Name: {values[0][1]} | Department: {values[0][0]} | Doctor city: {values[0][2]}")
        try:  # To avoid non integer input
            if len(Doctors_DataBase) != 0:
                doctor_ID = int(input("Enter doctor ID : "))
                while doctor_ID not in Doctors_DataBase:
                    doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                Doctors_DataBase.pop(doctor_ID)
                print("")
                print("/" + 21*'-' + "Doctor data deleted successfully" + 21*'-' + "/")
            elif len(Doctors_DataBase) == 0:
                print("No available data to be deleted")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def edit_doctor():
        print("Existing Doctors")
        for key, values in Doctors_DataBase.items():
            print(f"Doctor ID: {key} | Doctor Name: {values[0][1]} | Department: {values[0][0]} | Doctor city: {values[0][2]}")
        try:  # To avoid non integer input
            if len(Doctors_DataBase) != 0:
                while True:
                    print("")
                    doctor_ID = int(input("Enter doctor ID : "))
                    if doctor_ID not in Doctors_DataBase:
                        doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                    print("")
                    print("Doctor name     :", Doctors_DataBase[doctor_ID][0][1])
                    print("Doctor city     :", Doctors_DataBase[doctor_ID][0][2])
                    print("Doctor is in " + Doctors_DataBase[doctor_ID][0][0] + " department")
                    print("")
                    print("-----------------------------------------")
                    print("|1. To Edit doctor's department         |")
                    print("|2. To Edit doctor's name               |")
                    print("|3. To Edit doctor's city               |")
                    print("|To be Back Enter B                     |")
                    print("-----------------------------------------")
                    print("")
                    choice = input("Enter your choice : ")
                    print("")
                    if choice == "1":
                        DepartmentList = ["Medicine", "Neurology", "Surgery", "Cardiology"]
                        print(f"Departments: {DepartmentList}".replace('\'','').replace('[','').replace(']','').replace(',',' / '))
                        print("")
                        Department = input("Enter department : ")
                        while Department not in DepartmentList:
                            print("Invalid Input")
                            Department = input("Enter department : ")
                        Doctors_DataBase[doctor_ID][0][0] = Department
                        print("")
                        print("/" + 21*'-' + "Doctor's department edited successfully" + 21*'-' + "/")

                    if choice == "2":
                        Doctors_DataBase[doctor_ID][0][1] = input("Enter Doctor's Name : ")
                        print("")
                        print("/" + 21*'-' + "Doctor's name edited successfully" + 21*'-' + "/")

                    if choice == "3":
                        Doctors_DataBase[doctor_ID][0][2] = input("Enter Doctor's City : ")
                        print("")
                        print("/" + 21*'-' + "Doctor's city edited successfully" + 21*'-' + "/")

                    if choice == "B":
                        break

                    else:
                        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                        break
            elif len(Doctors_DataBase) == 0:
                print("No available data to be edited")

        except:
            print("")
            print("Invalid Doctor ID, Please try again")

    def doctor_menu():
        print("")
        print("-----------------------------------------")
        print("|1. To add new doctor                   |")
        print("|2. To display doctor                   |")
        print("|3. To delete doctor data               |")
        print("|4. To edit doctor data                 |")
        print("|To Exit enter B                        |")
        print("-----------------------------------------")

