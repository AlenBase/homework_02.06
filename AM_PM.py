hour=int(input('Enter hour: ' ))
Time_of_day=input('am or pm: ' )
Time_forward=int(input('How many hours forward: ' ))

new_hour=(hour+Time_forward)%12
if new_hour==0:
    new_hour=12
if Time_of_day == "am" and hour + Time_forward >=12:
    Time_of_day = "pm"
elif Time_of_day == "pm" and hour + Time_forward >=12:
    Time_of_day = "am"
    

print(new_hour,Time_of_day)