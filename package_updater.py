import subprocess
import pandas as pd
import re
import PySimpleGUI as sg
import os
fhandle = open(r'update.txt', 'w')
subprocess.run('pip list --outdated', shell = True, stdout = fhandle)
fhandle.close()
df1 = pd.DataFrame(columns=['Package', 'Version', 'Latest', 'Type'])
fhandle = open(r'update.txt', 'r')
AnyPackagesToUpgrade = 0
for i, line in enumerate(fhandle):
    if i not in (0, 1): #first two lines have no packages
        df1 = df1.append({
                'Package': re.findall('(.+?)\s', line)[0],
                'Version': re.findall('([0-9].+?)\s', line)[0],
                'Latest': re.findall('([0-9].+?)\s', line)[1], 
                'Type': re.findall('\s([a-zA-Z]+)', line)[0]
                }, ignore_index=True)
        AnyPackagesToUpgrade = 1 #if no packages, then don't bring up full UI later on
formlists = []  #This will be the list to be displayed on the UI
i = 0
while i < len(df1): #this is the checkbox magic that will show up on the UI
    formlists.append([sg.Checkbox(df1.iloc[i, :])])
    formlists.append([sg.Text('-'*50)])
    i += 1
layout = [
    [sg.Column(layout=[
        *formlists], vertical_scroll_only=True, scrollable=True, size=(704, 400)
    )],

    [sg.Output(size=(100, 10))],
    [sg.Submit('Upgrade'), sg.Cancel('Exit')]
]
window = sg.Window('Choose Package to Upgrade', layout, size=(800, 650))
if AnyPackagesToUpgrade == 0:
    sg.Popup('No Packages requiring upgrade found')
    fhandle.close()
    os.remove('update.txt')
    quit()
definedkey = []
while True:  # The Event Loop
    event, values = window.read()
    # print(event, values)  # debug
    if event in (None, 'Exit', 'Cancel'):
        fhandle.close()
        os.remove('update.txt')
        exit()
    elif event == 'Upgrade':
        for index, value in enumerate(values):
            if values[index] == True:
                #print(df1.iloc[index][0])
                subprocess.run('pip install --upgrade ' + df1.iloc[index][0])
                print('Upgrading', df1.iloc[index][0])
        print('Upgrading process finished.')
