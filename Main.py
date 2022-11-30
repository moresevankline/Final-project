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
    print("-----------------------------------------")
    print("|Enter 1 for Admin mode                 |")
    print("|Enter 2 for User mode                  |")
    print("-----------------------------------------")
    Admin_user_mode = input("Enter your mode : ")

    if Admin_user_mode == "1":  
        print("*******************************************")
        print("|                                         |")
        print("|         Welcome to admin mode           |")
        print("|                                         |")
        print("*******************************************")
        Username = input("Please enter your username : ")
        Password = input("Please enter your password : ")
        
        while True:
            if Username == "Admin" and Password == "1234":
                
                print("-----------------------------------------")
                print("|1. To manage patients                  |")
                print("|2. To manage doctors                   |")
                print("|To Exit Enter B                     |")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Pateints Management
                    print("-----------------------------------------")
                    print("|1. To add new patient                  |")
                    print("|2. Display patient                     |")
                    print("|3. Delete patient data                 |")
                    print("|4. Edit patient data                   |")
                    print("|To Exit enter B                        |")
                    print("-----------------------------------------")
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
                        print("Please enter a correct choice\n")

                elif AdminOptions == "2":
                    print("-----------------------------------------")
                    print("|1. To add new doctor                   |")
                    print("|2. To display doctor                   |")
                    print("|3. To delete doctor data               |")
                    print("|4. To edit doctor data                 |")
                    print("|To Exit enter B                  |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    
                    if Admin_choice == "1":
                        Doctor.add_doctor()

                    elif Admin_choice == "2":  
                        Doctor.display_doctor()

                    elif Admin_choice == "3":  
                        Doctor.delete_doctor()

                    elif Admin_choice == "4":  
                        Doctor.delete_doctor()

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

    elif Admin_user_mode == "2": 
        print("*******************************************")
        print("|                                         |")
        print("|         Welcome to User mode            |")
        print("|                                         |")
        print("*******************************************")

        while True:
            print("-------------------------------------------")
            print("|1. To view hospital's departments        |")
            print("|2. To view hospital's doctors            |")
            print("|3. To view patients' residents           |")
            print("|4. To view patient's details             |")
            print("|To Exit Enter B                       |")
            print("-------------------------------------------")
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1": 
                print("Hospital's departments :")
                Hospital.hospital_department()

            elif UserOptions == "2":  
                print("Hospital's doctors :")
                Hospital.hospital_doctors()

            elif UserOptions == "3":  
                Hospital.hospital_residents

            elif UserOptions == "4": 
                Patient.display_patient()

            elif UserOptions == "B":  
                break

            else:
                print("Please Enter a correct choice")

    else:
        print("Please choice just 1 or 2")