def Write_Patients_DataBase (Patients_Database) :
	myfile = open("Patients_DataBase.txt","w")
	for i in Patients_Database :
		myfile.write(str(i)+";"+Patients_Database[i][0]+";"+Patients_Database[i][1]+";"+Patients_Database[i][2]+";"+Patients_Database[i][3]+";"+Patients_Database[i][4]+";"+Patients_Database[i][5]+"\n")
	myfile.close()
	
	
	
def Write_Doctors_DataBase (Doctors_DataBase) :
	myfile = open("Doctors_DataBase.txt","w")	
	for i in Doctors_DataBase :
		myfile.write(str(i)+";")
		for j in Doctors_DataBase[i] :
			myfile.write(j[0]+";"+j[1]+";"+j[2]+";")
		myfile.write("\n")
	
	myfile.close()
