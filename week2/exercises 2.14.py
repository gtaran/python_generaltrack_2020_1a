# exercise 1
k = str("All ")
b = str("work ")
c = str("And ")
d = str("no ")
e = str("play ")
f = str("makes ")
g = str("Jack ")
h = str("a ")
i = str("dull ")
j = str("boy. ")
print(k+b+c+d+e+f+g+h+i+j)

# exercise 5 part 1
principal_amount = float(5000)
nominal_interest = float(0.05)
pay_out_times = float(4)
years = int(15)
cash_money = principal_amount * (1 + nominal_interest / pay_out_times)**(pay_out_times * years)
int_cash_money = int(cash_money)
print("After", years, "years of saving up, I now have around", int_cash_money, "euro")

# exercise 5 part 2
principal_amount = float(input("What's your principal amount of money?"))
nominal_interest = float(input("What's the annual interest rate?"))
pay_out_times = int(input("how often do they pay out interest per year?"))
years = int(input("For how many years have you had this account?"))
cash_money = principal_amount * (1 + (nominal_interest/pay_out_times)) ** (pay_out_times * years)
int_cash_money = int(cash_money)
print("After", years, "years of saving up, I now have around", int_cash_money, "euro")

# exercise 7
excess_hours = 51 % 24
days = 51 // 24
time_b = 2 + excess_hours
print("My alarm goes of at", time_b, "PM in", days, "days")

# exercise 8
current_time = input("What time is it now?")
hours_till_ring = input("In how many hours will your alarm ring?")
excess_hours_two = int(hours_till_ring) % 12
days = int(hours_till_ring) // 24
time_b = int(current_time) + excess_hours_two
print("My alarm goes of at", time_b, "hours in", days, "days")

# assignment 2 handout week 2
distance_kilometres = int(input("How far is your destination in kilometres?"))

speed_bike_kmh = int(input("How fast do you bike in km/h?"))
get_going_bike = int(input("How many minutes does it take before you start biking?"))

speed_walk_kmh = int(input("How fast do you walk in km/h?"))
get_going_walk = int(input("How many minutes does it take before you start walking?"))

speed_drive_kmh = int(input("How fast do you drive in km/h?"))
get_going_drive = int(input("How many minutes does it take before you start driving?"))

time_bike = distance_kilometres//speed_bike_kmh + get_going_bike//60
excess_bike = distance_kilometres % speed_bike_kmh + get_going_bike % 60

time_walk = distance_kilometres//speed_walk_kmh + get_going_walk//60
excess_walk = distance_kilometres % speed_walk_kmh + get_going_walk % 60

time_drive = distance_kilometres//speed_drive_kmh + get_going_drive//60
excess_drive = distance_kilometres % speed_drive_kmh + get_going_drive % 60

print("You will take", time_bike, "hours and", excess_bike, "minutes to your destination by bike,", time_walk,
      "hours and", excess_walk, "minutes if you walk and", time_drive, "hours and", excess_drive, "minutes " 
                                                                                                  "if you go by car.")
