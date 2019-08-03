import os
import shutil
import subprocess as bash
from distutils.dir_util import copy_tree


def get_this_folder():
    return os.path.dirname(os.path.realpath(__file__))


def run_option(char):
    print('Running option',char)
    username = ''

    # Set up aliases
    if char=='1':
        if username=='':
            print('Enter your username:')
            username = input()
            print('Username:',username)
        # to do: add pw asterisks
        # to do: add ctrl+backspace
        print('Setting up jay: what distro are you running? (Type nothing to skip jay setup)')
        print('1. Ubuntu')
        print('2. OpenSuse')
        print('3. Solus')
        distro = input()

        jayname = ''
        if distro=='1':
            jayname = 'jay_ubuntu.sh'
        elif distro=='2':
            jayname = 'jay_suse.sh'
        elif distro=='3':
            jayname = 'jay_solus.sh'

        if jayname!='':
            shutil.copy(get_this_folder()+'/scripts/'+jayname,'/home/'+username+'/jay.sh')
            # to do: set jay.sh as executable
            with open('scripts/aliases.txt','r+',encoding='UTF-8') as file:
                bashrc_append(file.read(),username)
            # bash.call('source ~/.bashrc') # Reload bash aliases


    # Install fonts
    elif char=='2':
        fonts_source = get_this_folder()+'/fonts/'
        copy_tree(fonts_source,'/usr/share/fonts/')
        # to do: install ttf ms core fonts

    # Set up KDE settings
    elif char=='3':
        if username=='':
            print('Enter your username:')
            username = input()
            print('Username:',username)
        # with open('/user/'+username+'/.config/kdeglobals','w+',encoding='UTF-8') as file:
        #     lines = file.read().splitlines()
        #     for line in lines:
        #         if line.startswith('SingleClick'):
        #             line = 'SingleClick=false'
        #     file.write('\n'.join(lines))
        print('KDE settings copied')
    print('Success: option',char,'complete.')
    

def bashrc_append(newline,username):
    with open('/home/'+username+'/.bashrc','a+',encoding='UTF-8') as file:
        file.write('\n'+newline)


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

print('Reminder! Run this script as "sudo python3 setup.py"')

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
