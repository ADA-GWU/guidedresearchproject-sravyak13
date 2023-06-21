import PySimpleGUI as sg
import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        output = result.decode('utf-8')
        return output.strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8').strip()

layout = [
    [sg.Text('Command:'), sg.InputText(key='-COMMAND-')],
    [sg.Button('Run'), sg.Button('Exit')],
    [sg.Output(size=(60, 10))]
]

window = sg.Window('Terminal', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Run':
        command = values['-COMMAND-']
        output = run_command(command)
        print(f'$ {command}')
        print(output)

window.close()
