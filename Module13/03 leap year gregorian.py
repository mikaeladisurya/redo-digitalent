year = int(input("What year? "))

if year >= 1582:
  print("Its Gregorian")
  if year % 4 == 0:
    print("and its a leap year")
  else:
    print("but its not a leap year")
else:
  print("Not gregorian bro")