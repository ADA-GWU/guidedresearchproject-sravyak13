import tkinter as tk
from tkinter import ttk
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

def on_command_change(event):
    selected_command = command_combo.get()
    command_description = commands[selected_command]
    arguments_entry.delete(0, tk.END)
    arguments_entry.tooltip_text = command_description

def run_button_click():
    command = command_combo.get()
    arguments = arguments_entry.get()
    output = run_command(command, arguments)
    output_text.insert(tk.END, f'$ {command} {arguments}\n')
    output_text.insert(tk.END, output + '\n')

root = tk.Tk()
root.title('Unix Commands GUI')

command_label = ttk.Label(root, text='Command:')
command_label.grid(row=0, column=0, sticky=tk.W)
command_combo = ttk.Combobox(root, values=list(commands.keys()), state='readonly')
command_combo.grid(row=0, column=1, padx=5, pady=5)
command_combo.bind('<<ComboboxSelected>>', on_command_change)

arguments_label = ttk.Label(root, text='Arguments:')
arguments_label.grid(row=1, column=0, sticky=tk.W)
arguments_entry = ttk.Entry(root)
arguments_entry.grid(row=1, column=1, padx=5, pady=5)

run_button = ttk.Button(root, text='Run', command=run_button_click)
run_button.grid(row=2, column=0, padx=5, pady=5)

output_text = tk.Text(root, width=60, height=10)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
