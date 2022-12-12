from Hospital import Hospital
from Patient import Patient
from Doctor import Doctor

hospital = Hospital
patient = Patient
doctor = Doctor

def admin_mode():
    print("")  
    print("                *******************************************")
    print("                |                                         |")
    print("                |          Welcome to Admin mode          |")
    print("                |                                         |")
    print("                *******************************************")
    print("")
    while True:
        print("")
        print("                ------------------------------------------")
        print("                | 1. To manage patients                  |")
        print("                | 2. To manage doctors                   |")
        print("                | To Exit Enter B                        |")
        print("                ------------------------------------------")
        print("")
        AdminOptions = input("Enter your choice : ")

        if AdminOptions == "1":  # Admin mode --> Patients Management
            
            while True:
                patient.patient_menu()
                print("")
                Admin_choice = input("Enter your choice : ")
                if Admin_choice == "1":
                    patient.add_patient()

                elif Admin_choice == "2":
                    patient.display_patient()

                elif Admin_choice == "3":   
                    patient.delete_patient()

                elif Admin_choice == "4":  
                    patient.edit_patient()
                                    
                elif Admin_choice == "B": 
                    break

                else:
                    print("")

        elif AdminOptions == "2":

            while True:
                doctor.doctor_menu()
                print("")
                Admin_choice = input("Enter your choice : ")
                print("")
                
                if Admin_choice == "1":
                    doctor.add_doctor()

                elif Admin_choice == "2":  
                    doctor.display_doctor()

                elif Admin_choice == "3":  
                    doctor.delete_doctor()

                elif Admin_choice == "4":  
                    doctor.edit_doctor()

                elif Admin_choice == "B":  
                    break

                else:
                    print("")
        
        elif AdminOptions == "B":
            break

        else:
            print("")

def user_mode():
    print("")
    print("                *******************************************")
    print("                |                                         |")
    print("                |         Welcome to User mode            |")
    print("                |                                         |")
    print("                *******************************************")

    while True:
        hospital.hospital_menu()
        UserOptions = input("Enter your choice : ")

        if UserOptions == "1": 
            print("Hospital's department/s with doctors:")
            hospital.hospital_department()

        elif UserOptions == "2":  
            print("Hospital's doctors :")
            hospital.hospital_doctors()

        elif UserOptions == "3":  
            hospital.hospital_residents()

        elif UserOptions == "4": 
            patient.display_patient()

        elif UserOptions == "B":  
            break

        else:
            print("")

def main_menu():

    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Welcome Hospital Management System                     *")
    print("*                                                                          *")
    print("****************************************************************************")

    tries_flag = ""

    while tries_flag != "Close the program":
        print("                 -----------------------------------------")
        print("                 |         Enter 1 for Admin mode        |")
        print("                 |         Enter 2 for User mode         |")
        print("                 |         Enter 3 to Exit               |")
        print("                 -----------------------------------------")
        print("")
        Admin_mode = input("Enter your mode : ")
        if Admin_mode == "1":
            admin_mode()
            
        elif Admin_mode == "2": 
            user_mode()

        elif Admin_mode == "3":
            print("")
            print("Program shutting down........")
            break

        else:
            print("")

if __name__ == "__main__":
    main_menu()