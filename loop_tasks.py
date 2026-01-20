# Use for loop to print numbers 1 to 100.
print("---- for loop to print number 1 to 100----")
for i in range(1, 101):
    print(i)

# Use while loop for countdown timer.
print("---- while loop----")
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Times UP!")

#Implement break and continue.
print("---- break and continue ----")
for i in range(1,11):
    if i == 5:
        print("skip 5")
        continue
        
    if i == 9:
        print("stop if 9")
        break
        
    print(i)
    
# Iterate over string characters.
print("Iterate over string characters")
name = "shreya"
for ch in name:
    print(ch)

# Generate multiplication table.
print("Multiplication of any number")
num = int(input("enter a number to print a number: "))
for i in range(1,11):
    print(num, "x", i, "=",num * i)

# Use range with steps.
print("range with steps")
for i in range(2, 21, 2): # start from 2 to 20 and print alternate number by skiping 2
    print (i)

# Combine loop with conditions.
# Add real-world examples
balance = 50000
try: 
    while True:
        withdraw = int(input("Enter a withdrawl amount: "))
        if withdraw <=0 and withdraw > balance:
            print("Insufficient balance ")

        else:
            balance -= withdraw
            print("withdraw successfully")
            print("Remaning balance: ",balance)
        
except ValueError:
    print("Enter a numeric value only")