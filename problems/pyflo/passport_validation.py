'''
This problem is depicted in https://pyflo.net/what-is-python/ as
'To check the passport of US citizen is valid or not' 
'''
import time

current_year = int(time.strftime('%Y'))
receiver_year = int(input('What year did you get your passport? '))
if receiver_year + 10 < current_year:
    print('You should go and get a new passport')
else:
    print('You may use your current passport')