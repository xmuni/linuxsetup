import os
import subprocess as bash

def get_this_folder():
    return os.path.dirname(os.path.realpath(__file__))

def run_option(char):
    print('Running option',char)
    filename = options[char]['filename']
    with open(filename,'r+',encoding='UTF-8') as file:
        for line in file.read().strip().splitlines():
            if not line.startswith('#') and len(line)>1:
                bash_call(line)
    # bash_run('bash '+filename)

# Runs a command such as "cp -r ~/Documents ~/DocBackup"
def bash_call(command):
    print(command)
    # bash.call(command.split(), stdout=bash.PIPE)

##### MAIN #####

options = {
    '1': {
        'label': 'Set up bash',
        'done': False,
        'filename': 'scripts/bash.txt'
    },
    '2': {
        'label': 'Install fonts',
        'done': False,
        'filename': 'scripts/install.txt'
    },
    '3': {
        'label': 'Set up KDE settings',
        'done': False,
        'filename': 'scripts/kde.txt'
    }
}

while True:
    for (key,value) in options.items():
        symbol = '[X]' if value['done']==True else '[ ]'
        print(symbol, key+'.', value['label'])
    print('0. Close setup')
    selection = input()
    for char in selection:
        if char=='0':
            print('Closing setup.')
            exit()
        elif char in options:
            run_option(char)
            options[char]['done'] = True
        else:
            print('Option not recognized:',selection)
