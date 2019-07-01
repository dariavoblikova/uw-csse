import queue
import tree


class Bank:

    def __init__(self):
        self.__requestList = queue.Queue()
        self.__acctInfoTree = tree.BinarySearchTree()


        self.transactOperations = {
            "O": self.openAccount,    
            "D": self.deposit,    
            "W": self.withdraw,    
            "T": self.transfer,    
            "H": self.history
        }

    def readTransactions(self,file):
        with open(file) as f:
            for i in f.read().split("\n"):
                buf = Transaction()
                buf.parseTransact(i)
                self.__requestList.put(buf)

    def processQueue(self):
        while not self.__requestList.empty():
            trans = self.__requestList.get()
            self.transactOperations[trans.getTransactionType()](trans)

    def displayAllAccounts(self):
        print("\nProcessing Done. Final Balances ")
        self.__acctInfoTree.Display()

    def openAccount(self,inTransaction):
        curAcctID = inTransaction.getAccountID()
        acctAvailable = self.__acctInfoTree.get(curAcctID)
        if (acctAvailable):
            print("ERROR: Account " + str(curAcctID) + " is already open. Transaction refused.")
            return False

        else:
            if (curAcctID >= 1000 and curAcctID <= 9999):
                createdAccount = Account(inTransaction.getLastName(), inTransaction.getFirstName(), inTransaction.getAccountID())
                self.__acctInfoTree.put(curAcctID,createdAccount)
                return True
            else:
                print("ERROR: Account ID is a 4 digit number. Can't open an account.")
                return False

    def deposit(self, inTransaction):
        result = False
        curAcctID = inTransaction.getAccountID()
        curFundTypeID = inTransaction.getFundTypeID()
        acctAvailable = self.__acctInfoTree.get(curAcctID)
        curAmount = inTransaction.getAmount()
        fund =  acctAvailable.getFund(curFundTypeID)
        if (acctAvailable and curAmount >= 0 and 0 <= curFundTypeID < 10):
            
            fund.deposit(curAmount)
            fund.addHistory(inTransaction)
            result = True
        else:
            if (curAmount < 0):
                inTransaction.setValidTransaction(False)
                fund.addHistory(inTransaction)
                print(f"ERROR: ${curAmount} is not possible amount to make transaction. Deposit refused. ")
            elif (curFundTypeID < 0 or curFundTypeID >= 10):
                print("ERROR: Fund ID have not been found. Deposit refused.")
            else:
                print("ERROR: Account " + str(curAcctID) + " was not found. Deposit refused. ")
        return result 

    def withdraw(self,inTransaction):
        curAcctID = inTransaction.getAccountID()
        curFundTypeID = inTransaction.getFundTypeID()
        acctAvailable = self.__acctInfoTree.get(curAcctID)
        curAmount = inTransaction.getAmount()
        fund =  acctAvailable.getFund(curFundTypeID)
        if (acctAvailable and curAmount >= 0 and 0 <= curFundTypeID < 10):
            if (fund.getBalance() < curAmount):
                if (curFundTypeID == 0 or curFundTypeID == 2):
                    sumTwoBalance = fund.getBalance() + acctAvailable.getFund(curFundTypeID + 1).getBalance()
                    remainAmount = curAmount - fund.getBalance();
                    if (sumTwoBalance < curAmount):
                        inTransaction.setValidTransaction(False)
                        fund.addHistory(inTransaction)
                        print("ERROR: Not enough funds to withdraw " + str(curAmount) + " from " + str(acctAvailable.getFirstName()) + str(acctAvailable.getLastName()) + str(fund.getFundName()))
                        return False
                    else:
                        fund.setBalance(0)
                        acctAvailable.getFund(curFundTypeID + 1).withdraw(remainAmount)
                        inTransaction.setAmount(curAmount - remainAmount)
                        fund.addHistory(inTransaction)
                        inTransaction.setAmount(remainAmount)
                        inTransaction.setFundTypeID(inTransaction.getAccountID() + 1)
                        acctAvailable.getFund(curFundTypeID + 1).addHistory(inTransaction)
                        return True
                elif (curFundTypeID == 1 or curFundTypeID == 3):
                    sumTwoBalance = fund.getBalance() + acctAvailable.getFund(curFundTypeID - 1).getBalance()
                    remainAmount = curAmount - fund.getBalance()
                    if (sumTwoBalance < curAmount):
                        inTransaction.setValidTransaction(False)
                        fund.addHistory(inTransaction)
                        print("ERROR: Not enough funds to withdraw " + str(curAmount) + " from " + str(acctAvailable.getFirstName()) + str(acctAvailable.getLastName()) + fund.getFundName())
                        return False

                    else:
                        fund.setBalance(0)
                        acctAvailable.getFund(curFundTypeID - 1).withdraw(remainAmount)
                        inTransaction.setAmount(curAmount - remainAmount)
                        fund.addHistory(inTransaction)
                        inTransaction.setAmount(remainAmount)
                        inTransaction.setFundTypeID(inTransaction.getAccountID() - 1)
                        acctAvailable.getFund(curFundTypeID - 1).addHistory(inTransaction)
                        return True

                else:
                    inTransaction.setValidTransaction(False)
                    fund.addHistory(inTransaction)
                    print(f"ERROR: Not enough funds to withdraw {curAmount} from {acctAvailable.getFirstName()} {acctAvailable.getLastName()} {fund.getFundName()}")
                    return False
            else:
                fund.withdraw(curAmount)
                fund.addHistory(inTransaction)
                return True

        else:
            if (curAmount < 0):
                inTransaction.setValidTransaction(False)
                fund.addHistory(inTransaction)
                print("ERROR: $" + str(curAmount) + " is not possible amount to make transaction. Witdraw refused. ")
                return False

            elif (inTransaction.getAccountID() < 0 or curFundTypeID >= 10):
                print("ERROR: Fund ID have not been found. Withdraw refused.")
                return False
            else:
                print("ERROR: Account " + curAcctID + " was not found. Withdraw refused. ")
                return False


    def transfer(self, inTransaction):
        curAcctID = inTransaction.getAccountID()
        curFundTypeID = inTransaction.getFundTypeID()
        curAnotherAcctID = inTransaction.getAnotherAccountID()
        curAnotherFundTypeID = inTransaction.getAnotherFundTypeID()
        curAcct = self.__acctInfoTree.get(curAcctID)
        curAmount = inTransaction.getAmount()
        AnotherAcctAvailable = self.__acctInfoTree.get(curAnotherAcctID)
        fund =  curAcct.getFund(curFundTypeID)
        remainAmount = curAmount - fund.getBalance()
        
        if (curAcct and AnotherAcctAvailable and (curAmount > 0) and (curFundTypeID >= 0)):
            if (fund.getBalance() < curAmount):
                if (curFundTypeID == 0 or curFundTypeID == 2):
                    if (remainAmount < (curAcct.getFund(curFundTypeID + 1).getBalance())):
                        fund.withdraw(curAmount - remainAmount)
                        curAcct.getFund(curFundTypeID + 1).withdraw(remainAmount)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).deposit(curAmount)
                        inTransaction.setAmount(curAmount - remainAmount)
                        fund.addHistory(inTransaction)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                        inTransaction.setAmount(remainAmount)
                        inTransaction.setMainFundTypeID(inTransaction.getAccountID() + 1)
                        curAcct.getFund(curFundTypeID + 1).addHistory(inTransaction)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                        return True

                elif (curFundTypeID == 1 or curFundTypeID == 3):
                    if ((remainAmount < (curAcct.getFund(curFundTypeID - 1).getBalance()))):
                        fund.withdraw(curAmount - remainAmount)
                        curAcct.getFund(curFundTypeID - 1).withdraw(remainAmount)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).deposit(curAmount)
                        inTransaction.setAmount(curAmount - remainAmount)
                        fund.addHistory(inTransaction)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                        inTransaction.setAmount(remainAmount)
                        inTransaction.setMainFundTypeID(inTransaction.getAccountID() - 1)
                        curAcct.getFund(curFundTypeID - 1).addHistory(inTransaction)
                        AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                        return True

                inTransaction.setValidTransaction(False)
                fund.addHistory(inTransaction)
                if (curAcctID != curAnotherAcctID):
                    AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                print("ERROR: Account ID " + str(curAcctID) + " " + str(fund.getFundName()) + " have insufficient balance to make Transfer to Account ID " + str(curAnotherAcctID) + " " + str(curAcct.getFund(curAnotherFundTypeID).getFundName()) + ". Transfer refused.")
                return False
            else:
                fund.withdraw(curAmount)
                AnotherAcctAvailable.getFund(curAnotherFundTypeID).deposit(curAmount)
                fund.addHistory(inTransaction)
                if (curAcctID != curAnotherAcctID):
                    AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                elif (curFundTypeID != curAnotherFundTypeID):
                    curAcct.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                return True
        else:
            if (curAmount < 0):
                inTransaction.setValidTransaction(False)
                fund.addHistory(inTransaction)
                if (curAcctID != curAnotherAcctID):
                    AnotherAcctAvailable.getFund(curAnotherFundTypeID).addHistory(inTransaction)
                print("ERROR: $" + str(curAmount) + " is not possible amount to make transaction. Transferal refused. ")
                return False
            elif (inTransaction.getAccountID() < 0 or inTransaction.getAnotherFundTypeID() < 0):
                print("ERROR: Fund ID have not been found. Transfer refused.")
                return False
            elif (not curAcct):
                print("ERROR: Account " + curAcctID + " was not found. Transfer refused. ")
                return False
            else:
                print("ERROR: Account " + str(curAnotherAcctID) + " was not found. Transfer refused. ")
                return False

    def history(self,inTransaction):
        curAcctID = inTransaction.getAccountID()
        curFundTypeID = inTransaction.getFundTypeID()
        curAcct = self.__acctInfoTree.get(curAcctID)
        fund =  curAcct.getFund(curFundTypeID)

        if (curAcct):
            if (curFundTypeID < 0):
                print("Transaction History for " + str(curAcct.getFirstName()) + " " + str(curAcct.getLastName()) + " by fund.")
                for j in range(curAcct.NUMBEROFFUNDS):
                    if not curAcct.getFund(j).isHistoryEmpty():
                        print(str(curAcct.getFund(j).getFundName()) + ": $" + str(curAcct.getFundBalance(j)))
                        curAcct.getFund(j).displayHistory()
                return True
            else:
                print("Transaction History for " + str(curAcct.getFirstName()) + " " + str(curAcct.getLastName()) + " " + str(fund.getFundName()) + ": $" + str(curAcct.getFundBalance(curFundTypeID)))
                fund.displayHistory()
                return True
        else:
            print("ERROR: Account " + str(curAcctID) + " was not found. Process history refused. ")
            return False

class Transaction:
    def __init__(self):
        self.__transactionType = ""
        self.__firstName = ""
        self.__lastName = ""
        self.__amount = 0
        self.__accountID = 0
        self.__anotherAccountID = 0
        self.__fundTypeID = 0
        self.__anotherFundTypeID = 0
        self.__validTransaction = True
        self.transactParsers = {
            "O": self.getOpen,    
            "D": self.getDepositAndWithdraw,    
            "W": self.getDepositAndWithdraw,    
            "T": self.getTransfer,
            "H": self.getHistory
        }

    def parseAccountID(self, fromAcctID):
        if 10000 <= fromAcctID <= 99999:
            self.__accountID = fromAcctID // 10
            self.__fundTypeID = fromAcctID % 10
        else:
            self.__accountID = fromAcctID
            self.__fundTypeID = -1

    def getOpen(self, elements):
        self.__lastName = elements[0]
        self.__firstName = elements[1]
        self.__accountID = int(elements[2])
       
    def getDepositAndWithdraw(self, elements):
        self.__amount = int(elements[1])
        fromAcctID = int(elements[0])
        self.parseAccountID(fromAcctID)
        
    def getHistory(self, elements):
        fromAcctID = int(elements[0])
        self.parseAccountID(fromAcctID)

    def getTransfer(self, elements):
        fromAcctID = int(elements[0])
        self.__amount = int(elements[1])
        toAcctID = int(elements[2])

        self.parseAccountID(fromAcctID)
        if 10000 <= toAcctID <= 99999:
            self.__anotherAccountID = toAcctID // 10
            self.__anotherFundTypeID = toAcctID % 10
        else:
            self.__anotherAccountID = toAcctID
            self.__anotherFundTypeID = -1

    def parseTransact(self, string):
        self.__transactionType = string[0]
        self.transactParsers[string[0]](string.split()[1:])


    def getTransactionType(self):
        return self.__transactionType

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccountID(self):
        return self.__accountID

    def getAnotherAccountID(self):
        return self.__anotherAccountID

    def getFundTypeID(self):
        return self.__fundTypeID

    def getAnotherFundTypeID(self):
        return self.__anotherFundTypeID

    def getAmount(self):
        return self.__amount

    def getValidTransaction(self):
        return self.__validTransaction

    def setTransactionType(self, inType):
        self.__transactionType = inType

    def setFirstName(self, inFirstName):
        self.__firstName = inFirstName

    def setLastName(self, inLastName):
        self.__lastName = inLastName

    def setAccountID(self, inAccountID):
        self.__accountID = inAccountID

    def setAnotherAccountID(self, inAccountID):
        self.__anotherAccountID = inAccountID

    def setFundTypeID(self, inFundID):
        self.__fundTypeID = inFundID

    def setAnotherFundTypeID(self, inFundID):
        self.__anotherFundTypeID = inFundID

    def setAmount(self, inAmount):
        self.__amount = inAmount

    def setValidTransaction(self, inFact):
        self.__validTransaction = inFact

    def __str__(self):
        if self.getTransactionType() == "D" or self.getTransactionType() == "W":
            return f"{self.getTransactionType()} {self.getAccountID()}{self.getFundTypeID()} {self.getAmount()}"
        elif self.getTransactionType() == "T":
            return f"T {self.getAccountID()}{self.getFundTypeID()} {self.getAmount()} {self.getAnotherAccountID()}{self.getAnotherFundTypeID()}"


class Fund:
    def __init__(self, inFundName = "", inBalance = 0):
        self.__fundName = inFundName
        self.__balance = inBalance
        self.__history = []

    def getFundName(self):
        return self.__fundName

    def getBalance(self):
        return self.__balance

    def setFundName(self, inFunName):
        self.__fundName = inFunName

    def setBalance(self,inBalance):
        self.__balance = inBalance

    def deposit(self, inAmount):
        self.__balance += inAmount

    def withdraw(self, inAmount):
        self.__balance -= inAmount

    def addHistory(self, inTransaction):
        self.__history.append(inTransaction)

    def displayHistory(self):
        for i in self.__history:
            print(" " + str(i))
            if not i.getValidTransaction():
                print(" (Failed)")

    def isHistoryEmpty(self):
        return not len(self.__history) > 0

    def __str__(self):
        return f"{self.getFundName()}: ${self.getBalance()}"

class Account:

    def __init__(self, inLastName = "", inFirstName = "", inID = 0):
        self.__lastName = inLastName
        self.__firstName = inFirstName
        self.__id = inID

        self.__funds = [Fund("Money Market"),
                        Fund("Prime Money Market"),
                        Fund("Long-Term Bond"),
                        Fund("Short-Term Bond"),
                        Fund("500 Index Fund"),
                        Fund("Capital Value Fund"),
                        Fund("Growth Equity Fund"),
                        Fund("Growth Index Fund"),
                        Fund("Value Fund"),
                        Fund("Value Stock Index")
                        ]
        self.NUMBEROFFUNDS = len(self.__funds)

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getID(self):
        return self.__id

    def getFund(self, fundNumber):
        return self.__funds[fundNumber]

    def getFundBalance(self, fundNumber):
        return self.__funds[fundNumber].getBalance()

    def setFirstName(self, inFirstName):
        self.__firstName = inFirstName

    def setLastName(self, inLastName):
        self.__lastName = inLastName

    def setID(self, inID):
        self.__id = inID

    def displayAllFunds(self):
        print(str(self.getFirstName()) + " " + str(self.getLastName()) + " Account ID: " + str(self.getID()))
        for i in self.__funds:
            print (f"\t {i.getFundName()}: ${i.getBalance()}")

    def displayFund(self, fundNumber):
        i = self.__funds[fundNumber]
        print(f"\t {i.getFundName()}: ${i.getBalance()}")

    def __eq__(self, rhs):
        return (self.getID() == (rhs.getID()))

    def __ne__(self, rhs):
        if self == rhs:
            return False
        else:
            return True

    def __gt__(self, rhs):
        return (self.getID() > (rhs.getID()))

    def __lt__(self, rhs):
        return (self.getID() < (rhs.getID()))

    def __str__(self):
        return str(self.getID()) + ", " + str(self.getFirstName()) + ", " + str(self.getLastName())