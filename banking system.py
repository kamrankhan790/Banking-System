#Banking Management System
acountNo=0
CusName=" "
Bcode=""
Mobile=0
Bal=0
def createAcount():
    global acountNo
    global CusName
    global Bcode
    global Mobile
    global Bal
    acountNo=int(input("enter account Number:"))
    CusName=input("enter name")
    Bcode=input("enter Branch Code")
    Mobile=int(input("enter Mobile"))
    Bal=int(input("enter current Balance"))
    
def ShowAcntDetails():
    print("AcountNO:",acountNo)
    print("customerName:",CusName)
    print("Bcode",BCode)
    print("mobile:",Mobile)
    
def Deposit(amount):
    global Bal
    Bal= Bal+amount
    chckbalance()
    
def Withdraw(amount):
    global Bal
    Bal= Bal-amount
    chckbalance()
    
def chckbalance():
    print("current Balance:",Bal)
    
ch1='y'    
while(ch1=='y'):    
    print("1.Create account\n 2.Withdraw \n 3.deposit \n 4.check balance")
    ch=int(input("select any option"))
    if(ch==1):
        createAcount()
    elif(ch==2):
        amnt=int(input("enter amount to Withdraw"))
        Withdraw(amnt)
    elif ch==3:
        amnt=int(input("enter amount to Deposit"))
        Deposit(amnt)
    elif ch==4:
        chckbalance()
    else:
        print("please slect any 4 option available above")
    print("do you want to continue..press y")
    ch1=input()      
