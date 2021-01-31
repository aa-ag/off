###--- IMPORTS ---###
import os


###--- FUNCTIONS ---###
def turn_device_off():
    turn_off = input('Wanna turn this laptop off?\n')

    if turn_off == 'no':
        exit()
    elif turn_off == 'yes':
        os.system('sudo shutdown -r now')
    # else:
    #     print('sorry, dunno what tha means...')


###--- DRIVER CODE ---###
if __name__ == '__main__':
    turn_device_off()
