#Password Game Using While loop
'''
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess==secret_number:
        print('You Won!')
        break
else:
    print('You Lost!')
'''
#Car Game using While loop
command=''
started=False
while True:
    command=input('>').lower()
    if command=='start':
        if started:
            print('Car is already started')
        else:
            started=True
            print('Car started...')
    elif command=='stop':
        if not started:
            print('Car is already stopped!')
        else:
            started=False
            print('Car stopped.')
    elif command=='help':
        print("""
start - to start the car
stop - to stop the car
quit- to quit""")
    elif command=='quit':
        break
    else:
        print("Sorry I Can't understand!")






















#Weight Pounds To Kilos and vice-versa.
'''
weight_lbs=int(input("enter your weight in lbs:"))#Pounds to Kilos
weight_kg=weight_lbs*0.45
print('My weight is',weight_kg,'Kg')
weight_kg=int(input('enter your weight in kg:'))#Kilos to Pounds
weight_lbs=weight_kg/0.45
print('My weight in lbs is',weight_lbs,'pounds')
'''
#Weight converter
'''
weight=int(input('Weight: '))
unit=input('(L)bs or (K)g:')
if unit.upper()=='L':
    converted=weight*0.45
    print(f'Your {converted} Kilos')
else:
    converted=weight/0.45
    print(f'Your {converted} Pounds')
'''
#If-elif-else
'''
is_hot=False
is_cold=False
if is_hot:
    print('Its a hot day')
    print('Plenty of water')
elif is_cold:
    print('Its a cold day')
    print('Wear warm clothes')
else:
    print('Its a lovely day')
print('Enjoy your day')
'''
#Buying a House
'''
price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f'down_payment:{down_payment}')
'''
#Eligible for loan-->use of logical operator
'''
has_high_income=True
has_good_credit=True
has_criminal_record=True
if has_high_income and has_good_credit and not has_criminal_record:#using and operator
    print('Eligible for loan')
else:
    print('Not Eligible for loan')
#if has_good_credit or has_high_income:#using or operator
#    print('Eligible for loan')
'''
#Temperatur status-->use of comparison operator
'''
temp=35
if temp != 30:
    print('Its a hot day')
elif temp <= 30:
    print('Its a cold day')
else:
    print('Its a normal day')
'''
#Use of comparison operator
'''
name='Rohit'
if len(name) < 3:
    print("Name must be at least 3 character long")
elif len(name) > 50:
    print('Name must be maximum of 50 character')
else:
    print("Name looks good!")
'''