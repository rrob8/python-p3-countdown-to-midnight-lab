import time

def countdown(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
    print('HAPPY NEW YEAR!')       

def countdown_with_sleep(integer):
    def delay(function):
        time.sleep(3)
    delay(countdown(integer))
        

    