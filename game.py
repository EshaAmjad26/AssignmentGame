name = str(input("Enter Your Name\t"))
num1 = int(input("Enter your first favorite number\t"))
num2 = int(input("Enter your second favorite number\t"))
num3 = int(input("Enter your third favorite number\t"))
print(f"\nHello {name}! Let's explore your favorite numbers")
list1 : list = []
list1.append(num1)
list1.append(num2)
list1.append(num3)
new_list = []
for x in list1:
    if x%2 == 0:
        new_list.append((x, "Even"))
    else:
        new_list.append((x, "Odd"))
print(f"The number {list1[0]} is \"{new_list[0][1]}\"")
print(f"The number {list1[1]} is \"{new_list[1][1]}\"")
print(f"The number {list1[2]} is \"{new_list[2][1]}\"")
square_list = []
for y in list1:
    square_list.append((y , y*y))
print(f"The number of {list1[0]} and its square is {square_list[0][1]}")
print(f"The number of {list1[1]} and its square is {square_list[1][1]}")
print(f"The number of {list1[2]} and its square is {square_list[2][1]}")
sum = list1[0] + list1[1] + list1[2]
print(f"Amazing the sum of your favorite numbers is  : {sum}")
def prime(summ):
     for i in range(3 , int(summ**0.5)+1, 2):
         if sum % i == 0:
             return False
         else:
             return True
if prime(sum):
    print(f"Wow! {sum} is a prime number")
else: 
    print(f" Oops! {sum} is not a prime number")