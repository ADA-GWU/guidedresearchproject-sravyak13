import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

def run_command(command, arguments):
    output = ''
    error = ''
    try:
        if command == 'cd':
            os.chdir(arguments)
        else:
            completed_process = subprocess.run(f'{command} {arguments}', capture_output=True, text=True, shell=True, check=True)
            output = completed_process.stdout
            error = completed_process.stderr
    except subprocess.CalledProcessError as e:
        error = str(e)
    return output.strip(), error.strip()


commands = {
    'ls': {
        'description': 'List files and directories',
        'template': 'ls',
        'requires_arguments': False
    },
    'cd': {
        'description': 'Change directory',
        'template': 'cd <directory>',
        'requires_arguments': True
    },
    'mkdir': {
        'description': 'Create directory',
        'template': 'mkdir <directory>',
        'requires_arguments': True
    },
    'cp': {
        'description': 'Copy file or directory',
        'template': 'cp <source> <destination>',
        'requires_arguments': True
    },
    'mv': {
        'description': 'Move file or directory',
        'template': 'mv <source> <destination>',
        'requires_arguments': True
    },
    'rm': {
        'description': 'Remove file or directory',
        'template': 'rm <file>',
        'requires_arguments': True
    },
    'pwd': {
        'description': 'Print working directory',
        'template': 'pwd',
        'requires_arguments': False
    },
    'cat': {
        'description': 'Concatenate and display files',
        'template': 'cat <file>',
        'requires_arguments': True
    },
    'more': {
        'description': 'View file content one screen at a time',
        'template': 'more <file>',
        'requires_arguments': True
    },
    'head': {
        'description': 'Display the beginning of a file',
        'template': 'head <file>',
        'requires_arguments': True
    },
    'tail': {
        'description': 'Display the end of a file',
        'template': 'tail <file>',
        'requires_arguments': True
    }
}

def on_command_change(event):
    selected_command = command_combo.get()
    command_description = commands[selected_command]['description']
    command_template = commands[selected_command]['template']
    arguments_entry.delete(0, tk.END)
    arguments_entry.tooltip_text = f"{command_description}\n\nTemplate: {command_template}"

def validate_arguments(command, arguments):
    if not command:
        return False, "Please select a command."

    if command not in commands:
        return False, "Invalid command selected."

    if commands[command]['requires_arguments'] and not arguments:
        return False, "This command requires arguments. Please provide them."

    return True, ""

def run_button_click():
    command = command_combo.get()
    arguments = arguments_entry.get()

    is_valid, error_message = validate_arguments(command, arguments)

    if not is_valid:
        messagebox.showerror("Error", error_message)
        return

    output, error = run_command(command, arguments)

    output_text.configure(state='normal')
    output_text.insert(tk.END, f'$ {command} {arguments}\n')

    if error:
        messagebox.showerror("Error", f"Error: {error}")
        return

    output_text.insert(tk.END, output + '\n')
    output_text.configure(state='disabled')




def show_command_info():
    command_info_window = tk.Toplevel(root)
    command_info_window.title('Command Information')

    content_frame = ttk.Frame(command_info_window)
    content_frame.pack(padx=20, pady=20)

    command_info_label = ttk.Label(content_frame, text='Command Information:', font=('SF Pro', 12, 'bold'))
    command_info_label.pack(pady=(0, 10))

    command_info_text = tk.Text(content_frame, width=60, height=40, font=('SF Pro', 12))
    command_info_text.pack()

    for command, data in commands.items():
        description = data['description']
        template = data['template']
        command_info_text.insert(tk.END, f'{command}\n')
        command_info_text.insert(tk.END, f'Description: {description}\n')
        command_info_text.insert(tk.END, f'Template: {template}\n\n')

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

output_window = tk.Toplevel(root)
output_window.title('Output')

output_text = tk.Text(output_window, width=60, height=40, font=('SF Pro', 12))
output_text.pack(padx=20, pady=20)
output_text.configure(state='disabled')

command_info_button = ttk.Button(root, text='Command Info', command=show_command_info)
command_info_button.pack()

root.mainloop()
