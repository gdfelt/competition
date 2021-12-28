using System;

public class BankAccount
{
    private readonly object acctLock = new object();
    private decimal balance = 0.00m;
    private bool open = false;

    public void Open()
    {
        // throw new NotImplementedException("You need to implement this function.");
        open = true;
    }

    public void Close()
    {
        // throw new NotImplementedException("You need to implement this function.");
        open = false;
    }

    public decimal Balance
    {
        get
        {
            if(open){
                return balance;
            } else {
                throw new InvalidOperationException("Account is closed.");
            }
            
        }
    }

    public void UpdateBalance(decimal change)
    {
        // throw new NotImplementedException("You need to implement this function.");
        lock(acctLock){
            balance += change;
        }
    }
}
