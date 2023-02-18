 # This program has a defined function
# When the function is called the program calculates # # regular or regular plus OT pay based on the user's # # input of hours and rate

# Defined function and print statement
def computepay(hours,rate):
  print('In computepay '
        'Hours: ', hours, 'Rate: ', rate)
# Request for user's input. Then convert input to a # #decimal
  
  worked = input('Enter hours worked: ')
  per = input('Enter pay rate: ')
  hours = float(worked)
  rate = float(per)

# conditional statement for inputted housrs over 40
  
  if hours <= 40:
    pay = hours * rate
    
  else:
    hours > 40
    reg = hours * rate
    ot = (hours - 40) * 1.5
    pay = ot + reg
    
  print('Pay this Period: $', pay)
  computepay(hours,rate)
