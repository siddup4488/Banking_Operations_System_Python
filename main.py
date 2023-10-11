class Accounts:
    def __init__(self,name,gender,aadhar,pan,dob,phone,address,accountNo,ifscCode,accountType,password,balance):
        self.name=name
        self.gender=gender
        self.aadhar=aadhar
        self.pan=pan
        self.dob=dob
        self.phone=phone
        self.address=address
        self.accountNo=accountNo
        self.ifscCode=ifscCode
        self.accountType=accountType
        self.password=password
        self.balance=balance

    def display(self):
        print("\n")
        print("Name: "+ self.name)
        print("-----Enter The Personal Details Of The User-----")
        print("Aadhar: "+self.aadhar)
        print("PAN: "+self.pan)
        print("DOB: "+self.dob)
        print("Phone Number: "+self.phone)
        if self.gender == 1:
            print("Gender: Male")
        elif self.gender == 2:
            print("Gender: Female")
        print("Address: "+self.address)
        print("-----Account Details of the  ICICI  Banking User-----")
        print("AccountNo: "+self.accountNo)
        print("IFSC Code: "+self.ifscCode)
        if self.accountType == 1:
            print("Account Type: Savings")
        elif self.accountType == 2:
            print("Account Type: Current")
        print("Balance: "+str(self.balance))

from validate import *
from adminVerify import *

accountsData=[]

def start():
    flag=True
    while(flag):
        print("\n")
        print("---------Welcome To The ICICI India Banking Management System --------")
        print("choose")
        print("1. Bank Employee")
        print("2. Account Holder")
        print("3. Close The System")
        choice=int(input("Enter Your Choice: "))
        print("\n")
        
        if choice==1:
            
            print("--------Admin Login into the ICICI India Banking --------")
            username=input("Username: ")
            password=input("Password: ")
            if verifyAdminAccount(username,password):
                print("Login Successful")
                while True:
                    print("\n")
                    print("What do you want to do in the ICICI Banking?")
                    print("1. Open A Bank Account With ICICI")
                    print("2. Diaplay All The Accounts in ICICI")
                    print("3. Close An Account of the User in ICICI")
                    print("4. Update Account Details of the user in ICICI")
                    print("5. Get Details of a specific Account in ICICI")
                    print("6. Add Money in an Account")
                    print("7. Exit")
                    choice=int(input("Enter Your Choice: "))
                    print("\n")
                    if choice == 1:
                        print("-------------Account Opening Application Form-------------")
                        while True:
                            accountType=int(input("Select Account Type: 1.Savings ; 2.Current : "))
                            if not verifyAccountType(accountType):
                                print("Invalid AccountType! Please Enter It Again.")
                            else:
                                break
                        while True:
                            name=input("Enter User Name: ")
                            if not verifyName(name):
                                print("Invalid Name! Please Enter It Again.")
                            else:
                                break
                        while True:
                            gender=int(input("Select gender: 1.Male ; 2.Female : "))
                            if not verifyGender(gender):
                                print("Invalid! Please Enter It Again.")
                            else:
                                break
                        while True:
                            DOB=input("Enter DOB: ")
                            if not verifyDOB(DOB):
                                print("Invalid DOB! Please Enter It Again.")
                            else:
                                break
                        while True:
                            PAN=input("Enter PAN: ")
                            if not verifyPAN(PAN):
                                print("Invalid PAN! Please Enter It Again.")
                            else:
                                break
                        while True:
                            aadhar=input("Enter Aadhar: ")
                            if not verifyAadhar(aadhar):
                                print("Invalid Aadhar! Please Enter It Again.")
                            else:
                                break
                        while True:
                            phone=input("Enter Phone Number: ")
                            if not verifyPhone(phone):
                                print("Invalid Phone Number! Please Enter It Again.")
                            else:
                                break
                        print("Enter the address:")
                        houseNo=input("House: ")
                        city=input("City: ")
                        state=input("State: ")
                        address=houseNo + " , " + city + " , " + state
                        account=Accounts(name,gender,aadhar,PAN,DOB,phone,address,generateAccountNo(city,state,accountType),generateIFSC(city,state),accountType,generatePassword(PAN,phone),balance=0)
                        accountsData.append(account)
                        print("\n")
                        print("-------------Account Opened Successfully Thank You !!!-------------")
                        account.display()
                        
                    elif choice==2:
                        print("All the accounts in the Database:")
                        for i in accountsData:
                            i.display()
                    
                    elif choice==3:
                        accountNo=input("Enter The Account No. To Close in ICICI: ")
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                accountsData.remove(i)
                        print("-------------Account Closed Successfully!!-------------")
                    
                    elif choice==4:
                        accountNo=input("Enter The Account No. of the account you want to update: ")
                        print("Choose what do you want to update.")
                        print("1. Name")
                        print("2. DOB")
                        choice=int(input("Enter your choice: "))
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                if choice==1:
                                    while True:
                                        name=input("Enter Name: ")
                                        if not verifyName(name):
                                            print("Invalid Name! Please Enter It Again.")
                                        else:
                                            i.name=name
                                            print("Account Details Updated Successfully! Thank You !!!")
                                            break
                                elif choice==2:
                                    while True:
                                        DOB=input("Enter DOB: ")
                                        if not verifyDOB(DOB):
                                            print("Invalid DOB! Please Enter It Again.")
                                        else:
                                            i.DOB=DOB
                                            print("Account Details Updated Successfully! Thank You ")
                                            break
                        
                    elif choice==5:
                        print("Search ICICI Account Based on:")
                        print("1. Name")
                        print("2. AccountNo")
                        while True:
                            choice=int(input("Enter your choice: "))
                            if choice==1:
                                name=input("Enter The Name of The Account Holder: ")
                                for i in accountsData:
                                    if i.name==name:
                                        i.display()
                                        break
                            elif choice==2:
                                accountNo=input("Enter The AccountNo of The Account Holder: ")
                                for i in accountsData:
                                    if i.accountNo==accountNo:
                                        i.display()
                                        break
                            else:
                                print("Invalid choice!")
                            break
                                
                        
                    elif choice==6:
                        accountNo=input("Enter The Account No. of the User: ")
                        amount=int(input("Enter The amount to be deposited: "))
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                i.balance=i.balance+amount
                                print("Account Balance Updated Successfully! Thank You!!!!!")
                                break
                    
                    elif choice==7:
                        print("Thank You!")
                        break
                        
                    else:
                        print("Invalid Choice")
            
            else:
                print("Invalid Username/Password")
        
        elif choice==2:
            print("-------Customer Account Login into ICICI Banking Management System -------")
            print(" ** Password Hint: First 4 letters of PAN followed by last 4 number of the mobile number **")
            username=input("Account No.: ")
            password=input("Password : ")
            check=False
            for i in accountsData:
                if i.accountNo==username and i.password==password:
                    print("Login Successful")
                    check=True
                    while True:
                        print("\n")
                        print("What do you want to do?")
                        print("1. Update Account Details")
                        print("2. Withdaw")
                        print("3. Transfer")
                        print("4. Balance Enquiry")
                        print("5. Exit")
                        choice=int(input("Enter Your Choice: "))
                        print("\n")
                        
                        if choice==1:
                            print("Choose what do you want to update.")
                            print("1. Name")
                            print("2. DOB")
                            choice=int(input("Enter your choice: "))
                            if choice==1:
                                while True:
                                    name=input("Enter Name: ")
                                    if not verifyName(name):
                                        print("Invalid Name! Please Enter It Again.")
                                    else:
                                        i.name=name
                                        print("Account Details Updated Successfully! Thank You !!!")
                            elif choice==2:
                                while True:
                                    DOB=input("Enter DOB: ")
                                    if not verifyDOB(DOB):
                                        print("Invalid DOB! Please Enter It Again.")
                                    else:
                                        i.dob=DOB
                                        print("Account Details Updated Successfully!")
                                    
                        elif choice==2:
                            amount=int(input("Enter the amount you want to withdraw: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                print("Windraw Successfully done")
                                print("Updated balance is "+str(i.balance))
                            else:
                                print("insufficient balance")
                        
                        elif choice==3:
                            accountNoT=input("Enter The Account No. you want to transfer: ")
                            amount=int(input("Enter the Amount you want to Transfer: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                for j in accountsData:
                                    if j.accountNo==accountNoT:
                                        j.balance=j.balance+amount
                                        print("Transfer Successful")
                                        print("Updated balance is "+str(i.balance))
                            else:
                                print("insufficient balance")
                        
                        elif choice==4:
                            print("Account Balance: "+str(i.balance))
                            
                        elif choice==5:
                            print("Thank You!")
                            break
                        else:
                            print("Invalid Choice")
                    break
            if(check==False):
                print("Invalid Username/Password")
            
            
        elif choice==3:
            flag=False
            print("Thank You!")
        else:
            print("Invalid Choice")
   
start()