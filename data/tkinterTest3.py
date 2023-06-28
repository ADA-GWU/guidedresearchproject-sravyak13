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
            output = subprocess.run(f'{command} {arguments}', capture_output=True, text=True, shell=True, check=True).stdout
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

def show_command_info():
    command_info_window = tk.Toplevel(root)
    command_info_window.title('Command Information')

    content_frame = ttk.Frame(command_info_window)
    content_frame.pack(padx=20, pady=20)

    command_info_label = ttk.Label(content_frame, text='Command Information:', font=('SF Pro', 12, 'bold'))
    command_info_label.pack(pady=(0, 10))

    command_info_text = tk.Text(content_frame, width=60, height=10, font=('SF Pro', 12))
    command_info_text.pack()

    for command, description in commands.items():
        command_info_text.insert(tk.END, f'{command}: {description}\n')

    command_info_text.configure(state='disabled')

root = tk.Tk()
root.title('Unix Commands GUI')

root.option_add('*TCombobox*Listbox.font', ('SF Pro', 10))
root.option_add('*TCombobox*Listbox.selectBackground', '#f2c949')
root.option_add('*TCombobox*Listbox.selectForeground', 'black')

style = ttk.Style()
style.configure('TLabel', font=('SF Pro', 12))
style.configure('TButton', font=('SF Pro', 12))
style.configure('TCombobox', font=('SF Pro', 12))

content_frame = ttk.Frame(root)
content_frame.pack(padx=20, pady=20)

command_label = ttk.Label(content_frame, text='Command:')
command_label.grid(row=0, column=0, sticky=tk.W)

command_combo = ttk.Combobox(content_frame, values=list(commands.keys()), state='readonly', width=30)
command_combo.grid(row=0, column=1, padx=5, pady=5)
command_combo.bind('<<ComboboxSelected>>', on_command_change)

arguments_label = ttk.Label(content_frame, text='Arguments:')
arguments_label.grid(row=1, column=0, sticky=tk.W)

arguments_entry = ttk.Entry(content_frame, width=30)
arguments_entry.grid(row=1, column=1, padx=5, pady=5)

run_button = ttk.Button(content_frame, text='Run', command=run_button_click)
run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

output_text = tk.Text(root, width=60, height=10, font=('SF Pro', 12))
output_text.pack(padx=20, pady=(0, 20))

command_info_button = ttk.Button(root, text='Command Info', command=show_command_info)
command_info_button.pack()

root.mainloop()
