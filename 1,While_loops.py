#sum of first n terms:
n = int(input("enter your terms: "))

sum = 0
i = 1

while i<=n:
    sum = sum+i
    i = i+1
print(f"\n The sum of {n} = {sum}")
# infinity loop: # DO NOT REMOVE HASHTAGS
#i = 0
#while i<=0:
    #print("i will never end")

# armstrong number:
# number =:
num = int(input("enter a number: "))
#initilise sum:
sum = 0
# find the sum of the cube of each digit:
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp//=10
# display the result:
if num == sum:
    print(num,"is a armstrong number")
else:
    print(f"{num} is not a armstrong number")