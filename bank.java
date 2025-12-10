import java.util.Scanner;
class bank
{ 
    int balance=0,num,pn,Anum;
    String na,type,ad;
    void NewAcc()
    { Scanner sc=new Scanner(System.in);
        System.out.println("Enter Account Holder Name: ");
        na=sc.nextLine();
        System.out.println("Enter Account Number: ");
        num=sc.nextInt();
        System.out.println("Enter Account Type: ");
        type=sc.nextLine();
        System.out.println("Enter Inital Deposit: ");
        balance=sc.nextInt();
        System.out.println("Enter Phone Number: ");
        pn=sc.nextInt();
        System.out.println("Enter Address: ");
        ad=sc.nextLine();
        System.out.println("Enter Adhaar number: ");
        Anum=sc.nextInt();
        
    }
     
    void details()
    {     
        System.out.println("ACCOUNT DETAILS");
        System.out.println("Account Holder Name: "+ na);
        System.out.println("Account Number: "+ num);
        System.out.println("Account Type: "+ type);
        System.out.println("Inital Deposit: "+ balance);
        System.out.println("Phone Number: "+ pn);
        System.out.println("Address: "+ ad);
        System.out.println("Adhaar number: "+ Anum);
         
        
    }
    
   void deposit()
    {   int amount;
        System.out.println("Enter amount to be deposited");
        Scanner sc=new Scanner(System.in);
        amount=sc.nextInt();
        if(amount>0)
        { 
            balance=balance+amount;
            System.out.println("Deposited"+ amount + "Successfully");
            System.out.println("New balance is: "+ balance);
        }
        else
             System.out.println("Invalid deposit amount");
    }
    
    void withdraw()
    {   int amount;
        
        System.out.println("Enter amount to be withdrawn");
        Scanner sc=new Scanner(System.in);
        amount=sc.nextInt();
        if(amount>0)
        {
            if(balance >= amount)
            { balance=balance-amount;
                System.out.println(amount + "Withdrawn Successfully");
                 System.out.println("New balance is: "+ balance);
                }
        else 
        { System.out.println("Insufficient balance!");
        }}
        else
        {
            System.out.println("Invalid amount. Enter a positive value");

        }
    }


    void balance()
    {
        System.out.println("Current Balance is: "+ balance);

    }
public static void main()
    { Scanner sc=new Scanner(System.in);
        int choice;
    System.out.println("          WELCOME           ");
    System.out.println("1. Create new account ");
     System.out.println("2. Display account details ");
      System.out.println("3. Deposit money ");
       System.out.println("4. Withdraw money " );
        System.out.println("5. Check balance " );
         System.out.println("6. Exit " );
    System.out.println("Enter choice: ");
    choice=sc.nextInt();
    bank obj = new bank();
    switch(choice)
    { 
        case 1: 
            obj.NewAcc();
            break;
        case 2:
            obj.details();
             break;
        case 3:
            obj.deposit();
             break;
        case 4:
            obj.withdraw();
             break;
        case 5:
            obj.balance();
             break;
        case 6:
            System.out.println("Thank you for banking with us");
             break;
        default:
            System.out.println("Wrong Choice");
    }
}}
