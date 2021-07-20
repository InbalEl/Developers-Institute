def birthdayCake(nof_candles: int):
    candles = 'i' * nof_candles
    candles_line = '   __' + candles + '__'

    min_candle_line_len = 13
    padding = 0 if len(candles_line) <= 13 else len(candles_line) - min_candle_line_len
    
    padding = 0
    cake = f'''
       {candles_line}{'_' * padding}
       |:H:a:p:p:y:{'' * padding}|
     __|___________{'' * padding}|__ 
    |^^^^^^^^^^^^^^^^^{'' * padding}| 
    |:B:i:r:t:h:d:a:y:{'' * padding}| 
    |                 {'' * padding}|
    ~~~~~~~~~~~~~~~~~~~{'~'* padding}
    '''
    print(cake)


user1_age = 29
user2_age = 14
user3_age = 3

birthdayCake(user1_age%10)
birthdayCake(user2_age%10)
birthdayCake(user3_age%10)