# Game Assignment

![Python Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.unite.ai%2F10-best-python-libraries-for-machine-learning-ai%2F&psig=AOvVaw2i4LudjdEnxr6uiVdgZtN-&ust=1726226534551000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPjX6_CkvYgDFQAAAAAdAAAAABAE)

![Python Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fportswigger.net%2Fdaily-swig%2Fmalicious-python-library-ctx-removed-from-pypi-repo&psig=AOvVaw2i4LudjdEnxr6uiVdgZtN-&ust=1726226534551000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPjX6_CkvYgDFQAAAAAdAAAAABAJ)

# Break into Steps

## Step 1

### The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers.

```
name = str(input("Enter Your Name"))
num1 = int(input("Enter your first favorite number\t"))
num2 = int(input("Enter your second favorite number\t"))
num3 = int(input("Enter your third favorite number\t"))
```

## Step 2

### After gathering this information, the program should greet the user with a personalized message that includes their name.

`print(f"\nHello {name}! Let's explore your favorite numbers")`

## step 3

### The three numbers provided by the user should be stored in a list.

```
list1 : list = []
list1.append(num1)
list1.append(num2)
list1.append(num3)
```

## step 4

### The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd".

```
new_list = []
for x in list1:
    if x%2 == 0:
        new_list.append((x, "Even"))
    else:
        new_list.append((x, "Odd"))

print(f"The number {list1[0]} is \"{new_list[0][1]}\"")
print(f"The number {list1[1]} is \"{new_list[1][1]}\"")
print(f"The number {list1[2]} is \"{new_list[2][1]}\"")

```

## step 5

### Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format.Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message.

```
square_list = []
for y in list1:
    square_list.append((y , y*y))
print(f"The number of {list1[0]} and its square is {square_list[0][1]}")
print(f"The number of {list1[1]} and its square is {square_list[1][1]}")
print(f"The number of {list1[2]} and its square is {square_list[2][1]}")
sum = list1[0] + list1[1] + list1[2]
print(f"Amazing the sum of your favorite numbers is  : {sum}")

```

## step 6

### Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message.

```
def prime(sum):
     for i in range(3 , int(sum**0.5)+1, 2):
         if sum % i == 0:
             return False
         else:
             return True
if prime(sum):
    print(f"Wow! {sum} is a prime number")
else:
    print(f" Oops! {sum} is not a prime number")
```

# Goal

**Goal:**
_The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks._
