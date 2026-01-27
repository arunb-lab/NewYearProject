# Pizza Order Program - Learn elif statements!

print("Welcome to Python Pizza! ")
print("-" * 35)

# Get pizza size
print("\nWhat size pizza would you like?")
print("S = Small")
print("M = Medium")
print("L = Large")

size = input("Enter your choice (S/M/L): ").upper()

# Calculate price based on size using elif
if size == 'S':
    price = 10
    print("\nYou ordered a Small pizza for $10")
elif size == 'M':
    price = 15
    print("\nYou ordered a Medium pizza for $15")
elif size == 'L':
    price = 20
    print("\nYou ordered a Large pizza for $20")
else:
    price = 0
    print("\n❌ Invalid choice! Please run the program again.")

# Add toppings if valid size
if price > 0:
    print("\n🧀 Would you like extra cheese?")
    cheese = input("Enter Y for Yes or N for No: ").upper()
    
    if cheese == 'Y':
        price += 3
        print("Added extra cheese (+$3)")
    elif cheese == 'N':
        print("No extra cheese")
    else:
        print("Invalid input, skipping cheese")
    
    # Final bill
    print("\n" + "=" * 35)
    print(f"💰 Your total bill is: ${price}")
    print("=" * 35)
    print("Thank you for ordering! Enjoy your pizza! 🍕")
