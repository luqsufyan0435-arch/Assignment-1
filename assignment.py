
# Task 1: Multiplication Table

def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

multiplication_table()


# Task 2: Check Prime Number

def check_prime():
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not Prime")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime Number")
        else:
            print("Not Prime")

check_prime()



# Task 3: Reverse String

text = input("Enter a string")
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text

print("Reversed string:",reversed_text)    


# Task:4 Count the vowels and consonants in a sentance
def count_vowels_consonants(s):
        vowels = "aeiou"
        vowel_count = 0
        consonant_count = 0
        for char in s:
            if char.lower() in vowels:
                vowel_count += 1
            elif char.isalpha():
                consonant_count += 1
        return vowel_count, consonant_count
        
print(count_vowels_consonants("hello word"))

 # 5 Task Even and Odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_sum = 0

for i in numbers:
    if i % 2 == 0:
        print(i, "Even hai")
        even_sum = even_sum + i
    else:
        print(i, "Odd hai")
        odd_sum = odd_sum + i

        print("Even numbers ka sum hai:",even_sum)
        print("Odd number ka sum hai:",odd_sum)

    # Task 6: Star Pattern

n = 5
for i in range(1, n+1):
    print("*" *i)  
    





 




