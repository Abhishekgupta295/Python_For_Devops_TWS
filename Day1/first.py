print("Hello Abhishek here !")

x = 20
y = 10
z = x + y
print(z)

env = input("Enter your assign environment: ")

print("Your assign environment is: " , env)

if env == "prd":
    print("Dont deploy on Friday")
elif env == "stg":
    print("Take Backuup and test well")
else :
    print("You can deploy on any day")  

for i in range(10):
    print(i)      