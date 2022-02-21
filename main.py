# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#   print(fruit + " Pie")

# print()

#For Loop with Range
for number in range(1,10): #last number in the range won't be included in the list
  print(number)

print()

#For Loop with Range
for number in range(1,10, 3): #adding the last number at the end allows us to skip through the range
  print(number)

#This For/Range will produce the sum of 1 to 100
total = 0 
for number in range(1,101):
    total += number
print(total)