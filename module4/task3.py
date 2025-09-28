#Ask for the input from the user
num= input("Enter a number (or press Enter to quit): ")
#make a list where we can store the value for smallest and largest
number = []
#check for the conditions
while num != '':
    #convert theh num into an floating digit
    num= float(num)
    #adds each num value in number list
    number.append(num)
    num= input("Enter a number (or press Enter to quit): ")
#sort the number in descending order
number.sort(reverse=True)
#print the last number as index starts from 0 so length-1
print(f"Smallest number: {number[len(number)-1]}")
#print the first number from the index which will be the largest number
print(f"Largest number: {number[0]}")