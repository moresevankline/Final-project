def Read_Patients_DataBase() :

	myfile = open("Patients_DataBase.txt","r")

	Patients_Dict = dict()
	Patient_ID = ""
	Department = ""
	Doctor_Name = ""
	Patient_Name = ""
	Patient_Age = ""
	Patient_Gender = ""
	Patient_City = ""
	flag = 0
	text = myfile.read()
		
	for i in text :
		if flag == 0 :
						if i != ";" :
							Patient_ID = Patient_ID + i
						elif i == ";" :
							flag = 1
							
		elif flag == 1 :
						if i != ";" :
							Department = Department + i
						elif i == ";" :
							flag = 2
							
		elif flag == 2 :
						if i != ";" :
							Doctor_Name = Doctor_Name + i
						elif i == ";" :
							flag = 3
							
		elif flag == 3 :
						if i != ";" :
							Patient_Name = Patient_Name + i
						elif i == ";" :
							flag = 4
							
		elif flag == 4 :
						if i != ";" :
							Patient_Age = Patient_Age + i
						elif i == ";" :
							flag = 5
							
		elif flag == 5 :
						if i != ";" :
							Patient_Gender = Patient_Gender + i
						elif i == ";" :
							flag = 6
							
		elif flag == 6 :
						if i != "\n" :
							Patient_City = Patient_City + i
						elif i == "\n" :
							Patients_Dict[int(Patient_ID)]=[Department,Doctor_Name,Patient_Name,Patient_Age,Patient_Gender,Patient_City]
							Patient_ID = ""
							Department = ""
							Doctor_Name = ""
							Patient_Name = ""
							Patient_Age = ""
							Patient_Gender = ""
							Patient_City = ""
							flag = 0
							
		
	myfile.close()
	return Patients_Dict
			
def Read_Doctors_DataBase () :

	myfile = open ("Doctors_DataBase.txt","r")

	Doctors_Dict = dict()
	Doctor_ID = ""
	Department = ""
	Doctor_Name = ""
	Doctor_City = ""
	Patient_ID = ""
	flag = 0

	
	text = myfile.read()

	while text.count(";;") :
		text=text.replace(";;",";")
	
	for i in text :
		if flag == 0 :
					if i != ";" :
						Doctor_ID = Doctor_ID + i
					elif i == ";" :
						flag = 1
				
		elif flag == 1 :
					if i != ";" :
						Department = Department + i
					elif i == ";" :
						flag = 2
				
		elif flag == 2 :
					if i != ";" :
						Doctor_Name = Doctor_Name + i
					elif i == ";" :
						flag = 3
				
		elif flag == 3 :
					if i != ";" :
						Doctor_City = Doctor_City + i
					elif i == ";" :
						flag = 4
						Doctor_Data_List = [Department,Doctor_Name,Doctor_City]
						Doctors_Dict[int(Doctor_ID)]=[Doctor_Data_List]
						
		elif flag == 4 :
					if i != ";" and i != "\n" :
						Patient_ID = Patient_ID + i
					elif i == ";" :
						flag = 5
					elif i == "\n" :
						flag = 0
						Doctor_ID = ""
						Department = ""
						Doctor_Name = ""
						Doctor_City = ""

	myfile.close()
	return Doctors_Dict

