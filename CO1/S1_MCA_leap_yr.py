from datetime import date
todays_date = date.today()
startYear =int(todays_date.year)
print ("Enter last year")
endYear = int(input())
print ("List of leap years:")
for year in range(startYear, endYear):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)
