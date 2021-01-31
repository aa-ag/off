###--- IMPORTS ---###
import os


###--- FUNCTIONS ---###
def turn_device_off():
    '''
     user has 3 attempts to turn laptop off.
     if user says "n" or "no", loop breaks
     if user says "y" or "yes", command is executed and device is turned off
     else, the loop starts over 2 more times
    '''
    attempts = 0
    while attempts < 3:
        question = '🤖: wanna turn this laptop off? '
        turn_off = input(question)
        if turn_off == 'no' or turn_off == 'n':
            print('🤖: oh, ok -- bye!')
            exit()
        elif turn_off == 'yes' or turn_off == 'y':
            print('🤖: coolio, enter your password and i\'ll do the rest.')
            os.system('sudo shutdown -r now')
        else:
            print('🤖: sorry, dunno what tha means...')
            attempts += 1
    print('🤖: i\'m bored... see ya!')


###--- DRIVER CODE ---###
if __name__ == '__main__':
    turn_device_off()
