###--- IMPORTS ---###
import os


###--- CODE ---###
turn_off = input('Wanna turn this laptop off?\n')

if turn_off == 'no':
    exit()
elif turn_off == 'yes':
    os.system('sudo shutdown /s /t 1')
else:
    print('sorry, dunno what tha means...')
