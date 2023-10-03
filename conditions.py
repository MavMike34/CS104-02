#CS104
#Mike Montulet
#conditions.py

howMany = int(input("How many times would you like to try the program? "))
currentTry = 0

while (currentTry < howMany):
    temp = int(input("Please enter the current temperature: "))

    if(temp > 90):
        print("Wear shorts")
    elif(temp > 70):
        print("Short sleeves are fine")
    elif(temp > 50):
        print("Wear a jacket")
    elif(temp > 32):
        print("Wear a heavy coat")
    else:
        print("Stay inside")
    currentTry += 1

print("Program is completed.")
