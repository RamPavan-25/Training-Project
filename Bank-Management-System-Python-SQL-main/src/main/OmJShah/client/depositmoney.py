from tools import dataentering
def cp2(conn,cur,acc_type,acc_no):
    deposit_amt=int(input("Enter amount to deposit: "))
    if deposit_amt:
        query2="update {} set balance = balance+%s where acc_no = %s".format(acc_type)
        data2=(deposit_amt,acc_no)
        done2=dataentering.tableupdate(conn,cur,query2,data2)
        if done2:
            print("Deposit of {} currency successful".format(deposit_amt))
            print()
        else:
            print("Error while trying to add amount to balance.\n")
    else: 
        pass