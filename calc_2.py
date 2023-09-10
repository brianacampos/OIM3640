# 1 The volume of a sphere with radius r is
# What is the volume of a sphere with radius 5?
print(((4/3.0)* 3.14)* 5 **3)

#2 
bookprice = 24.95
discount = .60
shippingpriceadd = .75
shippingprice = 3.00
totalunits = 60

newbook = bookprice * discount * totalunits
shipping = shippingpriceadd * 59 + shippingprice

result = newbook + shipping

print('The total price for 60 books inclusing shipping and discount is:')
print('Total price of the books is:' + str(newbook))
print('Total shipping is:' + str(shipping))
print('The total price is:' + str(result))

#3
seconds = 1
minutes = 60 * seconds
hours = 60 * minutes

time_left_house = 6 * hours + 52 * minutes
miles_run_easy_pace = 2 * (8 * minutes + 15 * seconds)
miles_run_fast_pace = 3 * (7 * minutes + 12 * seconds)
total_time_run = miles_run_easy_pace + miles_run_fast_pace +time_left_house

hours = total_time_run // hours

part_hour = total_time_run % hours
minutes = part_hour // minutes
seconds = part_hour % minutes

print('Total tie run: {}, Hours:{}, Minutes:{}, Seconds:{}').format(total_time_run, hours, minutes, seconds)

#4
initial = 82
second = 89

print(100 * ((second-initial)/initial))