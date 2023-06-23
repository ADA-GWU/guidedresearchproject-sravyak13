import PySimpleGUI as sg
import subprocess
import os

def run_command(command, arguments):
    output = ''
    try:
        if command == 'cd':
            os.chdir(arguments)
        else:
            output = subprocess.run([command, arguments], capture_output=True, text=True, shell=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        output = str(e)
    return output.strip()

commands = {
    'ls': 'List files and directories',
    'cd': 'Change directory',
    'mkdir': 'Create directory',
    'cp': 'Copy file or directory',
    'mv': 'Move file or directory',
    'rm': 'Remove file or directory'
}

layout = [
    [sg.Text('Unix Commands GUI')],
    [sg.Text('Command Selection Menu')],
    [sg.Text('Command:'), sg.Combo(list(commands.keys()), key='-COMMAND-', enable_events=True)],
    [sg.Text('Argument Input Section')],
    [sg.Text('Arguments:'), sg.InputText(key='-ARGUMENTS-')],
    [sg.Button('Run'), sg.Button('Exit')],
    [sg.Output(size=(60, 10))]
]

window = sg.Window('Terminal', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == '-COMMAND-':
        selected_command = values['-COMMAND-']
        command_description = commands[selected_command]
        window['-ARGUMENTS-'].update('')
        window['-ARGUMENTS-'].set_tooltip(command_description)
    elif event == 'Run':
        command = values['-COMMAND-']
        arguments = values['-ARGUMENTS-']
        output = run_command(command, arguments)
        print(f'$ {command} {arguments}')
        print(output)

window.close()
