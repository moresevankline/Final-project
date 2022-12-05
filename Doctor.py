import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

class Doctor:

    def add_doctor():
        try:  # To avoid non integer input
            print("")
            doctor_ID = int(input("Enter doctor ID : "))
            while doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                doctor_ID = int(input("This ID is unavailable, please try another ID : "))
            Department = input("Enter Doctor department : ")
            Name = input("Enter Doctor name       : ")
            Address = input("Enter Doctor address    : ")
            Doctors_DataBase[doctor_ID] = [[Department, Name, Address]]
            print("")
            print("----------------------Doctor added successfully----------------------")
            print("")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def display_doctor():
        print("")
        print("Existing Doctors:")
        print([x.split(';')[0] for x in open("Doctors_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            doctor_ID = int(input("Enter doctor ID : "))
            while doctor_ID not in Doctors_DataBase:
                doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
            print("Doctor name    : ", Doctors_DataBase[doctor_ID][0][1])
            print("Doctor address : ", Doctors_DataBase[doctor_ID][0][2])
            print("Doctor is in " + Doctors_DataBase[doctor_ID][0][0] + " department")
        except:
            print("Doctor ID should be an integer number")
        

    def delete_doctor():
        print("")
        print("Existing Doctors:")
        print([x.split(';')[0] for x in open("Doctors_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            doctor_ID = int(input("Enter doctor ID : "))
            while doctor_ID not in Doctors_DataBase:
                doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
            Doctors_DataBase.pop(doctor_ID)
            print("")
            print("/----------------------Doctor data deleted successfully----------------------/")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def edit_doctor():
        print("")
        print("Existing Doctors:")
        print([x.split(';')[0] for x in open("Doctors_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            while True:
                doctor_ID = int(input("Enter doctor ID : "))
                if doctor_ID not in Doctors_DataBase:
                    doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                print("Doctor name    : ", Doctors_DataBase[doctor_ID][0][1])
                print("Doctor address : ", Doctors_DataBase[doctor_ID][0][2])
                print("Doctor is in " + Doctors_DataBase[doctor_ID][0][0] + " department")
                print("")
                print("-----------------------------------------")
                print("|1. To Edit doctor's department         |")
                print("|2. To Edit doctor's name               |")
                print("|3. To Edit doctor's address            |")
                print("|To be Back Enter B                     |")
                print("-----------------------------------------")
                print("")
                choice = input("Enter your choice : ")
                choice = choice.upper()
                print("")
                if choice == "1":
                    Doctors_DataBase[doctor_ID][0][0] = input("Enter Doctor's Department : ")
                    print("")
                    print("/----------------------Doctor's department edited successfully----------------------/")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                    break

                elif choice == "2":
                    Doctors_DataBase[doctor_ID][0][1] = input("Enter Doctor's Name : ")
                    print("")
                    print("----------------------Doctor's name edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                    break

                elif choice == "3":
                    Doctors_DataBase[doctor_ID][0][2] = input("Enter Doctor's Address : ")
                    print("")
                    print("----------------------Doctor's address edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                    break

                elif choice == "B":
                    break

                else:
                    print("\nPlease enter a correct choice\n")

        except:
            print("Doctor ID should be an integer number")

    def doctor_menu():
        print("")
        print("-----------------------------------------")
        print("|1. To add new doctor                   |")
        print("|2. To display doctor                   |")
        print("|3. To delete doctor data               |")
        print("|4. To edit doctor data                 |")
        print("|To Exit enter B                        |")
        print("-----------------------------------------")

