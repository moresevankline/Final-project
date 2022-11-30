import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

class Doctor:

    def add_doctor():
        try:  # To avoid non integer input
            Doctor_ID = int(input("Enter doctor ID : "))
            while Doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
            Department = input("Enter Doctor department : ")
            Name = input("Enter Doctor name       : ")
            Address = input("Enter Doctor address    : ")
            Doctors_DataBase[Doctor_ID] = [[Department, Name, Address]]
            print("----------------------Doctor added successfully----------------------")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def display_doctor():
        try:  # To avoid non integer input
            Doctor_ID = int(input("Enter doctor ID : "))
            while Doctor_ID not in Doctors_DataBase:
                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
            print("Doctor name    : ", Doctors_DataBase[Doctor_ID][0][1])
            print("Doctor address : ", Doctors_DataBase[Doctor_ID][0][2])
            print("Doctor is in " + Doctors_DataBase[Doctor_ID][0][0] + " department")
        except:
            print("Doctor ID should be an integer number")
        

    def delete_doctor():
        try:  # To avoid non integer input
            Doctor_ID = int(input("Enter doctor ID : "))
            while Doctor_ID not in Doctors_DataBase:
                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
            Doctors_DataBase.pop(Doctor_ID)
            print("/----------------------Doctor data deleted successfully----------------------/")
        except:
            print("Doctor ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

    def edit_doctor():
        try:  # To avoid non integer input
            Doctor_ID = input("Enter doctor ID : ")
            while Doctor_ID not in Doctors_DataBase:
                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
            while True:
                print("-----------------------------------------")
                print("|1. To Edit doctor's department         |")
                print("|2. To Edit doctor's name               |")
                print("|3. To Edit doctor's address            |")
                print("|To be Back Enter B                     |")
                print("-----------------------------------------")
                choice = input("Enter your choice : ")
                choice = choice.upper()
                if choice == "1":
                    Doctors_DataBase[Doctor_ID][0][0] = input("Enter Doctor's Department : ")
                    print("/----------------------Doctor's department edited successfully----------------------/")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

                elif choice == "2":
                    Doctors_DataBase[Doctor_ID][0][1] = input("Enter Doctor's Name : ")
                    print("----------------------Doctor's name edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

                elif choice == "3":
                    Doctors_DataBase[Doctor_ID][0][2] = input("Enter Doctor's Address : ")
                    print("----------------------Doctor's address edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

                elif choice == "B":
                    break

                else:
                    print("\nPlease enter a correct choice\n")

        except:
            print("Doctor ID should be an integer number")

