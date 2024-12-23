print("Enter two numbers i'll divide them")
print("Type q to exit")

while True:
  first_num = input("Enter your first number: ")
  
  if first_num == "q":
    break
  second_num = input("Enter the second number: ")
  try:
    answer = int(first_num) / int(second_num)
    print(answer)
  except ZeroDivisionError:
    print("you can't divide with zero")