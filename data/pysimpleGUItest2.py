import PySimpleGUI as sg

# define the layout of the GUI
layout = [
    [sg.Text('Unix Commands GUI')],
    [sg.Text('Command Selection Menu')],
    [sg.Listbox(values=['Test Command 1', 'Test Command 2', 'Test Command 3'], size=(20, 4), key='-COMMAND-')],
    [sg.Text('Enter Command Number:')],
    [sg.Input(key='-COMMAND_NUMBER-')],
    [sg.Text('Argument Input Section')],
    [sg.Text('Enter Argument 1:')],
    [sg.Input(key='-ARGUMENT_1-')],
    [sg.Text('Enter Argument 2:')],
    [sg.Input(key='-ARGUMENT_2-')],
    [sg.Text('Enter Argument 3:')],
    [sg.Input(key='-ARGUMENT_3-')],
    [sg.Button('Execute')],
    [sg.Text('Output Display')],
    [sg.Text('Command executed successfully!')],
    [sg.Multiline(size=(40, 8), key='-OUTPUT-', disabled=True)]
]

window = sg.Window('Unix Commands GUI', layout)
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'Execute':
        command_number = values['-COMMAND_NUMBER-']
        argument_1 = values['-ARGUMENT_1-']
        argument_2 = values['-ARGUMENT_2-']
        argument_3 = values['-ARGUMENT_3-']
        
        # execute the command and capture the output
        output = f'Command {command_number} executed with arguments: {argument_1}, {argument_2}, {argument_3}'
        
        window['-OUTPUT-'].update(output) #update the output display with the output variable

window.close()
