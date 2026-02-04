class bank:
    def __init__(self, ac_no, bal):
     self.ac_no = ac_no
     self.bal = bal

    def deposit(self):
       amt = float(input("Enter ythe amount to deposit :"))
       self.bal =  self.bal + amt 
       print("Deposited", amt)
       print("Your new balance is : ", self.bal)

    def withdrawl(self):
       wth = float(input("enter the amount to withdraw"))
       if wth <= self.bal:
          self.bal = self.bal  - wth
       else:
          print("tere account mein itne paise nhi h sale gareeb")
    
    def check_bal(self):
       print("your balnce is : ", self.bal)


ac_no = int(input("enter initial acc no: "))
bal = int(input("Enter initaial balance: "))
obj = bank(ac_no, bal)

option = 0
while option != 4:
    option = int(input("1. Deposite\n 2. Withdrawl \n 3. Check_balance \n 4. Exit\n  Please choose one option from above"))
    match option:
        case 1:
            obj.deposit()
        case 2:
            obj.withdrawl()
        case 3:
            obj.check_bal()
        case 4:
            print("thank you!!!!")
