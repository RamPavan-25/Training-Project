from tools import dataentering
def cp3(conn,cur,acc_type,acc_no):
    cur.execute(f"select balance from {acc_type} where acc_no=%s",(acc_no,))
    balance=cur.fetchall()
    balance=balance[0][0]
    withdraw_amt=dataentering.amounts(cur,"withdraw",acc_type,acc_no)
    if withdraw_amt:
        query="update {} set balance = balance-%s where acc_no=%s".format(acc_type)
        data=(withdraw_amt,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
                print("Successfully withdrawn {} currency".format(withdraw_amt))
                print()
        else:
            print("couldn't update balance\n")
    else:
        print("Couldn't withdraw amount\n")