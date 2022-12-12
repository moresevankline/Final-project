from Hospital import*
from Patient import*
from Doctor import*

print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Hospital Management System                     *")
print("*                                                                          *")
print("****************************************************************************")

tries = 0
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
        print("")  
        print("                *******************************************")
        print("                |                                         |")
        print("                |          Welcome to admin mode          |")
        print("                |                                         |")
        print("                *******************************************")
        print("")
        Username = input("Please enter your username : ")
        Password = input("Please enter your password : ")
        
        while True:
            if Username == "Admin" and Password == "1234":
                print("")
                print("------------------------------------------")
                print("| 1. To manage patients                  |")
                print("| 2. To manage doctors                   |")
                print("| To Exit Enter B                        |")
                print("------------------------------------------")
                print("")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Patients Management
                    
                    while True:
                        Patient.patient_menu()
                        print("")
                        Admin_choice = input("Enter your choice : ")
                        Admin_choice = Admin_choice.upper()
                        if Admin_choice == "1":
                            Patient.add_patient()

                        elif Admin_choice == "2":
                            Patient.display_patient()

                        elif Admin_choice == "3":   
                            Patient.delete_patient()

                        elif Admin_choice == "4":  
                            Patient.edit_patient()
                                         
                        elif Admin_choice == "B": 
                            break

                        else:
                            print("")
                            print("Please enter a correct choice\n")

                elif AdminOptions == "2":

                    while True:
                        Doctor.doctor_menu()
                        print("")
                        Admin_choice = input("Enter your choice : ")
                        Admin_choice = Admin_choice.upper()
                        
                        if Admin_choice == "1":
                            Doctor.add_doctor()

                        elif Admin_choice == "2":  
                            Doctor.display_doctor()

                        elif Admin_choice == "3":  
                            Doctor.delete_doctor()

                        elif Admin_choice == "4":  
                            Doctor.edit_doctor()

                        elif Admin_choice == "B":  
                            break

                        else:
                            print("\nPlease enter a correct choice\n")
                
                elif AdminOptions == "B":
                    break

                else:
                    print("Please choose only 1 or 2")

            elif Username != "Admin" and Password == "1234":
                if tries < 2:
                    print("\nIncorrect details, please try again\n")
                    Username = input("Please enter your username : ")
                    Password = input("Please enter your password : ")
                    tries += 1

                else:
                    print("\nIncorrect details, no more tries\n")
                    print("Program shutting down")
                    tries_flag = "Close the program"
                    break
            
            elif Username == "Admin" and Password != "1234":
                if tries < 2:
                    print("\nIncorrect details, please try again\n")
                    Username = input("Please enter your username : ")
                    Password = input("Please enter your password : ")
                    tries += 1

                else:
                    print("\nIncorrect details, no more tries\n")
                    print("Program shutting down")
                    tries_flag = "Close the program"
                    break

            elif Username != "Admin" and Password != "1234":
                if tries < 2:
                    print("\nIncorrect details, please try again\n")
                    Username = input("Please enter your username : ")
                    Password = input("Please enter your password : ")
                    tries += 1

                else:
                    print("\nIncorrect details, no more tries\n")
                    print("Program shutting down")
                    tries_flag = "Close the program"
                    break

    elif Admin_mode == "2": 
        print("")
        print("                *******************************************")
        print("                |                                         |")
        print("                |         Welcome to User mode            |")
        print("                |                                         |")
        print("                *******************************************")

        while True:
            Hospital.hospital_menu()
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1": 
                print("Hospital's departments :")
                Hospital.hospital_department()

            elif UserOptions == "2":  
                print("Hospital's doctors :")
                Hospital.hospital_doctors()

            elif UserOptions == "3":  
                Hospital.hospital_residents()

            elif UserOptions == "4": 
                Patient.display_patient()

            elif UserOptions == "B":  
                break

            else:
                print("Please Enter a correct choice")

    elif Admin_mode == "3":
        print("")
        print("Program shutting down........")
        break
    
    else:
        print("Please choice just 1 or 2")