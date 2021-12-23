from datetime import datetime

now = datetime.now()

print("***********************************************")
print(now)
print("Welcome to Payroll Report") 
print("***********************************************")

def init():
    try:
        name = input("Please enter your name: ")
        print('Welcome %s' %name)
        
        try: 
            hours = float(input("How many hours did you work this week? : "))
        except ValueError:
            print("Your input is invalid")
            init()
        
        try:
            regwage = float(input("What is your hourly wage?: $"))
        except ValueError:
            print("Your input is invalid.")
            init()

    except ValueError:
        print("Your input is invalid.")
        init()


    def pay():
        print("For employee %s \n" %name)
        print("You worked %.2f hours during this pay period \n" %hours)

        if 0 < hours < 40:
            grosspay = hours * regwage
            print("Your gross pay is $ %.2f \n" %grosspay)

        elif hours >  40:
            regularpay = 40 * regwage
            print("Your gross regular pay is $ %.2f \n" %regularpay)
            regpayovertime = (hours - 40) * 1.5 * regwage 
            print("Your gross over time pay is $ %.2f \n" %regpayovertime)
            grosspay = regularpay + regpayovertime

        else:
            print("You have selected invalid option")
            pay()
        
        #fed tax 10%
        fedtax = grosspay * 0.1
        #state tax 6%
        statetax = grosspay * 0.06
        #FICA 3%
        fica = grosspay * 0.03

        netpay = grosspay - fedtax - statetax - fica 

        print("Your Fed Tax is $ %.2f \n" %fedtax)
        print("Your State Tax is $ %.2f \n" %statetax)
        print("Your Fica is $ %.2f \n" %fica)
        print("Your net pay is $ %.2f \n" %netpay)
        exit()

    pay()

init()


