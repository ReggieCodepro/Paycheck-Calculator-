
name = raw_input("Name of employee: " )

print("hello " + name)
def main():
    hours, rate = inputData()
    normal_hours, overtime_hours, overtime = computePay (hours, rate)
    regular, total_pay = preovertime_hours (hours, rate, overtime)
    displayPay("", "", "", "", "", hours * rate)
    

def inputData():
   
    
    
    while True:
        try:
            paycheckCal = open("MypaycheckCal.txt", "w")
            hours = float (input("Now enter the hours worked please:"))
            
            
            
            break
        except ValueError:
            pass
    rate = float (input("Now enter the pay rate:"))
    return hours, rate

def computePay (hours, rate):
    overtime_rate = 1.5 + rate 
    normal_hours = min(hours, 40)
    overtime_hours = max(hours - 40, 0)
    overtime = overtime_hours * overtime_rate
    return normal_hours, overtime_hours, overtime

def preovertime_hours (hours, rate, overtime):
    regular = hours * rate 
    total_pay = regular
    return regular, total_pay

def displayPay (rate, normal_hours, overtime_hours, regular, overtime, total_pay):
    paycheckCal = open("MypaycheckCal.txt", "w")
    paycheckCal.write("Hello!! " + name+ ", Thanks for using our paycheck calculator. \n" )
    paycheckCal.write("The amount to be paid to your checkings account is $:" + format(total_pay, ".2f"))
   
    
    paycheckCal.close()
    
    print("The amount to be paid to in this period is $:" + format(total_pay, ".2f"))
main()
