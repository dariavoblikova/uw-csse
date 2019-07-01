import tree
import bank

jollyBank = bank.Bank()
jollyBank.readTransactions("BankTransIn.txt")
jollyBank.processQueue()
jollyBank.displayAllAccounts()