import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

Patients_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()

class Patient:
    
    def add_patient():
        try:  # To avoid non integer input
            patient_ID = int(input("Enter patient ID : "))
            while patient_ID in Patients_DataBase:  # if Admin entered used ID
                patient_ID = int(input("This ID is unavailable, please try another ID : "))
            print("")
            Department = input("Enter patient department : ")
            DoctorName = input("Enter name of doctor following the case : ")
            Name = input("Enter patient name : ")
            Age = input("Enter patient age : ")
            Gender = input("Enter patient gender : ")
            Address = input("Enter patient address : ")
            RoomNumber = input("Enter patient room number : ")
            Patients_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address, 
                                            RoomNumber]
            print("")
            print("----------------------Patient added successfully----------------------")
            print("")
        except:
            print("Patient ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)

    def display_patient():
        print("")
        print("Existing Patients:")
        print([x.split(';')[0] for x in open("Patients_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            patient_ID = int(input("Enter patient ID : "))
            while patient_ID not in Patients_DataBase:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
            print("\nPatient name        : ", Patients_DataBase[patient_ID][2])
            print("Patient age         : ", Patients_DataBase[patient_ID][3])
            print("Patient gender      : ", Patients_DataBase[patient_ID][4])
            print("Patient address     : ", Patients_DataBase[patient_ID][5])
            print("Patient room number : ", Patients_DataBase[patient_ID][6])
            print("Patient is in " + Patients_DataBase[patient_ID][0] + " department")
            print("Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
        except:
            print("Patient ID should be an integer number")

    def delete_patient():
        print("")
        print("Existing Patients:")
        print([x.split(';')[0] for x in open("Patients_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            patient_ID = int(input("Enter patient ID : "))
            while patient_ID not in Patients_DataBase:
                print("Patient ID not found")
                patient_ID = int(input("Please Enter patient ID : "))
            Patients_DataBase.pop(patient_ID)
            print("")
            print("----------------------Patient data deleted successfully----------------------")
        except:
            print("Patient ID should be an integer number")
        Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)

    def edit_patient():
        print("")
        print("Existing Patients:")
        print([x.split(';')[0] for x in open("Patients_DataBase.csv").readlines()])
        print("")
        try:  # To avoid non integer input
            while True:
                patient_ID = int(input("Enter patient ID : "))
                if patient_ID not in Patients_DataBase:
                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                print("\nPatient name        : ", Patients_DataBase[patient_ID][2])
                print("Patient age         : ", Patients_DataBase[patient_ID][3])
                print("Patient gender      : ", Patients_DataBase[patient_ID][4])
                print("Patient address     : ", Patients_DataBase[patient_ID][5])
                print("Patient room number : ", Patients_DataBase[patient_ID][6])
                print("Patient is in " + Patients_DataBase[patient_ID][0] + " department")
                print("Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
                print("")
                print("------------------------------------------")
                print("|1. To Edit Patient Department           |")
                print("|2. To Edit Doctor Following case        |")
                print("|3. To Edit Patient Name                 |")
                print("|4. To Edit Patient Age                  |")
                print("|5. To Edit Patient Gender               |")
                print("|6. To Edit Patient Address              |")
                print("|7. To Edit Patient RoomNumber           |")
                print("|To be Back Enter B                      |")
                print("-----------------------------------------")
                print("")
                Admin_choice = input("Enter your choice : ")
                Admin_choice = Admin_choice.upper()

                if Admin_choice == "1":
                    Patients_DataBase[patient_ID][0] = input("\nEnter patient department : ")
                    print("")
                    print("----------------------Patient Department edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "2":
                    Patients_DataBase[patient_ID][1] = input("\nEnter Doctor follouing case : ")
                    print("")
                    print("----------------------Doctor follouing case edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "3":
                    Patients_DataBase[patient_ID][2] = input("\nEnter patient name : ")
                    print("")
                    print("----------------------Patient name edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "4":
                    Patients_DataBase[patient_ID][3] = input("\nEnter patient Age : ")
                    print("")
                    print("----------------------Patient age edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "5":
                    Patients_DataBase[patient_ID][4] = input("\nEnter patient gender : ")
                    print("")
                    print("----------------------Patient gender edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "6":
                    Patients_DataBase[patient_ID][5] = input("\nEnter patient address : ")
                    print("")
                    print("----------------------Patient address edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "7":
                    Patients_DataBase[patient_ID][6] = input("\nEnter patient RoomNumber : ")
                    print("")
                    print("----------------------Patient RoomNumber edited successfully----------------------")
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
                    break

                elif Admin_choice == "B":
                    break

                else:
                    print("Please Enter a correct choice")
        except:
            print("Patient ID should be an integer number")

    def patient_menu():
        print("")
        print("-----------------------------------------")
        print("|1. To add new patient                  |")
        print("|2. Display patient                     |")
        print("|3. Delete patient data                 |")
        print("|4. Edit patient data                   |")
        print("|To Exit enter B                        |")
        print("-----------------------------------------")
        
        

