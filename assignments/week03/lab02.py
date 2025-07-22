# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print(f"Your balance: ${balance}")

        elif choice == "2":
            amount = float(input("Enter amout to Withdraw : "))
            if amount > balance:
                print("Insufficient amount")
            elif amount <= 0:
                print("Invalid amount.")
            else :
                balance -= amount
                print(f"Remaining balance: ${balance}")

        elif choice == "3":
            amount = float(input("Enter amout to Deposit : "))
            if amount <= 0:
                print("Invalid amount.")
            else :
                balance += amount
                print(f"New balance: ${balance}")

        elif choice == "4":
            print("Thank for use the ATM : GOODBYE")
            break

        else :
            print("Invalid option. Please choose 1-4.")

else:
    print("Invalid PIN")

