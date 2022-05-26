from secrets import choice
import sys

print("PrimeNumbersfind.Start")
print("Do you like to get the prime numbers in a Range or in a number?")
choice = input("R/N:")
if(choice == R):
    

#Make Files ready
def makeFileReady():
    
    nameOfFile = input("Enter the name of the file: ")
    nameOfFile += ".csv"

    try:
        file = open(nameOfFile, "w")
    except:
        print("error Programm Stop")
        sys.exit(0)


    