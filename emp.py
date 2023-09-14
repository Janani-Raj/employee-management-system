import pymysql

con=pymysql.connect(host="localhost",user="root",password="janani",db="myemp")

def userExists(uid):
	cmd="select * from user where UserId='"+uid+"';"
	cursor=con.cursor()
	cursor.execute(cmd)
	row_count=0
	result=cursor.fetchall()
	row_count=cursor.rowcount
	cursor.close()
	if row_count>0:
		print("\nUserid already Exits Try Again!!!")
		exit()


def user_detail(uid):
	cmd="select * from emp_details where Uid='"+uid+"';"
	cursor=con.cursor()
	cursor.execute(cmd)
	result=cursor.fetchall()
	for x in result:
		print("Eid: ",x[1])
		print("Uid: ",x[0])
		print("Firstname: ",x[2])
		print("Lastname: ",x[3])
		print("Date of Birth: ",x[4])
		print("Gender: ",x[5])
		print("MobileNo: ",x[6])
		print("MobileNo2: ",x[7])
		print("Emailid: ",x[8])
		print("Address: ",x[9])
		print("City: ",x[10])
		print("Postalcode: ",x[11])
		print("Qualification: ",x[12])
		print("Current_Experience: ",x[13])
		print("Salary: ",x[14])
		print("Start_Date: ",x[15])
		print("End_Date: ",x[16])
		print("Emp_Department: ",x[17],"\n")
	cursor.close()

def userExists2(uid,psw):
	cmd="select * from user where Uid='"+uid+"' and Password='"+psw+"';"
	cursor=con.cursor()
	cursor.execute(cmd)
	row_count=0
	result=cursor.rowcount
	row_count=cursor.rowcount
	cursor.close()
	if row_count==0:
		print("\nUser Details not Valid. Try Again!!!")
		exit()

def detail_register(UserId):
	fn=input("Enter your Firstname: ")
	ln=input("Enter your Lastname: ")
	dob=input("Enter your Date of Birth in 2018-06-30: ")
	gen=input("Enter your Gender: ")
	mob=input("Enter your Mobileno: ")
	mob2=input("Enter your Mobileno2: ")
	em=input("Enter your Emailid: ")
	addr=input("Enter your Address: ")
	city=input("Enter your City: ")
	pc=input("Enter your Postalcode: ")
	qual=input("Enter your Qualification: ")
	exp=input("Enter your Current_Experience: ")
	sal=input("Enter your Salary amount: ")
	sd=input("Enter your Start Date in 2018-06-30: ")
	ed=input("Enter your End Date in 2018-06-30: ")
	dpt=input("Enter your Employee Department: ")
	cursor1=con.cursor()
	cmd="insert into emp_details(Uid,Fname,Lname,Date_of_Birth,Gender,Mobileno,Mobileno2,Emailid,Address,City,Postalcode,Qualification,Current_Experience,salary,Start_Date,End_Date,Emp_Department)values('"+UserId+"','"+fn+"','"+ln+"','"+dob+"','"+gen+"','"+mob+"','"+mob2+"','"+em+"','"+addr+"','"+city+"','"+pc+"','"+qual+"','"+exp+"','"+sal+"','"+sd+"','"+ed+"','"+dpt+"')";
	cursor1.execute(cmd)
	cursor1.close()

def register():
	while True:
		UserId=input("Enter your UserId: ")
		try:
			if len(str(UserId))>20 or len(str(UserId))<3:
				raise Exception('Invalid Input')
			break
		except:
			print("Please enter a chars contains only alphabets and the chars between 3 to 20 long.\n")
			continue
	userExists(UserId)
	while True:
		Username=input("Enter your Username: ")
		try:
			if len(str(UserName)) >30 or len(str(UserName)) <3:
				raise Exception('Invalid Input')
			break
		except:
			print("Please enter a chars contains only alphabets and the chars between 3 to 30 long.\n")
			continue
	while True:
		psw=input("Enter your Password: ")
		try:
			if len(str(psw)) >30 or len(str(psw)) <3:
				raise Exception('Invalid Input')
			break
		except:
			print("Please enter a chars contains only alphabets and the chars between 3 to 30 long.\n")
			continue
	while True:
		pno=input("Enter your Phoneno: ")
		try:
			if len(str(pno)) >30 or len(str(pno)) <3:
				raise Exception('Invalid Input')
			break
		except:
			print("Please enter a chars contains only alphabets and the chars between 3 to 30 long.\n")
			continue
	cursor1=con.cursor()
	cmd="insert into user values('"+UserId+"','"+Username+"','"+psw+"'+'"+pno+"')"
	cursor1.execute(cmd)
	cursor1.close()
	print("\nUser Registerd successfully!!!!!!\n Please provide Detail Info of user.")
	detail_register(UserId)

def delete(UserId,Eid):
	cursor1=con.cursor()
	cmd="delete from emp_details where Uid='%s' and Eid='%s';" %(UserId,Eid)
	cursor1.execute(cmd)
	cursor1.close()

def update(UserId,Eid):
	print("Enter your Choice to update data: ")
	print("1 => First Name\n""2 => Last Name\n""3 => Date of Birth\n""4 => Gender\n""5 => Mobile Number\n""6 => Mobile Number2\n""7 => Emailid\n""8 => Address\n""9 => City\n""10 => Postalcode\n"
"11 => Qualification\n""12 => Current_Experience\n""13 => Salary\n""14 => Start_Date\n""15 => End_Date\n""16 => Emp_Department\n")
	op=int(input("Enter the choice: "))
	if op not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
		print("\nNot a valid option. Try Again !!!")
	if(op==1):
		cursor1=con.cursor()
		fn=input("Enter your Firstname: ")
		cmd="update emp_details set Fname='%s' where Uid='%s' and Eid='%s'" %(fn,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==2):
		cursor1=con.cursor()
		ln=input("Enter your Lastname: ")
		cmd="update emp_details set Lname='%s' where Uid='%s' and Eid='%s'" %(ln,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==3):
		cursor1=con.cursor()
		dob=input("Enter your Date of Birth in 2018-06-30: ")
		cmd="update emp_details set Date_of_Birth='%s' where Uid='%s' and Eid='%s'" %(dob,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==4):
		cursor1=con.cursor()
		gen=input("Enter your Gender: ")
		cmd="update emp_details set Gender='%s' where Uid='%s' and Eid='%s'" %(gen,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==5):
		cursor1=con.cursor()
		mob=int(input("Enter your Mobileno: "))
		cmd="update emp_details set MobileNo='%s' where Uid='%s' and Eid='%s'" %(mob,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==6):
		cursor1=con.cursor()
		mob2=int(input("Enter your Mobileno2: "))
		cmd="update emp_details set MobileNo2='%s' where Uid='%s' and Eid='%s'" %(mob2,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==7):
		cursor1=con.cursor()
		em=input("Enter your Emailid: ")
		cmd="update emp_details set Emailid='%s' where Uid='%s' and Eid='%s'" %(em,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==8):
		cursor1=con.cursor()
		addr=input("Enter your Address: ")
		cmd="update emp_details set Address='%s' where Uid='%s' and Eid='%s'" %(addr,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==9):
		cursor1=con.cursor()
		city=input("Enter your City: ")
		cmd="update emp_details set City='%s' where Uid='%s' and Eid='%s'" %(city,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==10):
		cursor1=con.cursor()
		pc=int(input("Enter your Postalcode: "))
		cmd="update emp_details set Postalcode='%s' where Uid='%s' and Eid='%s'" %(pc,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==11):
		cursor1=con.cursor()
		qual=input("Enter your Qualification: ")
		cmd="update emp_details set Qualification='%s' where Uid='%s' and Eid='%s'" %(qual,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==12):
		cursor1=con.cursor()
		exp=int(input("Enter your Current_Experience: "))
		cmd="update emp_details set Current_Experience='%s' where Uid='%s' and Eid='%s'" %(exp,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==13):
		cursor1=con.cursor()
		sal=int(input("Enter your Salary: "))
		cmd="update emp_details set Salary='%s' where Uid='%s' and Eid='%s'" %(sal,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==14):
		cursor1=con.cursor()
		sd=input("Enter your Start Date in 2018-06-30: ")
		cmd="update emp_details set Start_Date='%s' where Uid='%s' and Eid='%s'" %(sd,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==15):
		cursor1=con.cursor()
		ed=input("Enter your End Date in 2018-06-30: ")
		cmd="update emp_details set End_Date='%s' where Uid='%s' and Eid='%s'" %(ed,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
	if(op==16):
		cursor1=con.cursor()
		dpt=input("Enter your Employee Department: ")
		cmd="update emp_details set Emp_Department='%s' where Uid='%s' and Eid='%s'" %(dpt,UserId,Eid)
		cursor1.execute(cmd)
		cursor1.close()
		exit()

def operation2(UserId,op):
	if(op==1):
		user_detail(UserId)
	if(op==2):
		user_detail(UserId)
		d_Eid=input("\nProvide the Eid of the row item to be Updated: ")
		update(UserId,d_Eid)
		print("\n")
		user_detail(UserId)
		print("\n Updated Successfully")
	if(op==3):
		detail_register(UserId)
		print("\n 1Row Inserted Successfully")
	if(op==4):
		user_detail(UserId)
		d_Eid=input("\nProvide the Eid of the row item to be Deleted: ")
		delete(UserId,d_Eid)
		print("\n")
		user_detail(UserId)
		print("\n Deleted Successfully")
	if(op==5):
		print("Exit Success !Thank You!")

def operation(op):
	if(op==1):
		print("\t\t\t***** Login Page *****\t\t\t")
		print("Please Enter the below details")
		login()
	if(op==2):
		print("\t\t\t******** Registration Page ********\t\t\t")
		print("Please Enter the below details")
		register()

def login():
	UserId=input("Enter your UserID:  ")
	passw=input("Enter your Password: ")
	userExists2(UserId,passw)
	print("User Logged In successfully!!!!!!\n\n\n")
	print("Please choose any of the below options!\n\n\n")
	print("1.\t View Details\n 2.\t Edit Details\n 3.\t Add Details\n 4.\t Delete Details\n 5.\t Exit")
	option1=int(input("\nEnter the option:  "))
	if option1 not in [1,2,3,4,5]:
		print("Not a valid option. Try Again !!!")
		exit()
	operation2(UserId,option1)

print("\t\t\t******** Personal Address Book Register ********\t\t\t")
print("1.\t Login\n2.\t Signup\n3.\t Exit")
option=int(input("Enter the option:  "))
if option not in [1,2,3]:
	print("\nNot a valid option. Try Again !!!")
	exit()
operation(option)
con.commit()
con.close()