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
    except subprocess.CalledProcessError or IOError as e:
        error = str(e)
    except FileNotFoundError as e:
        error = f"Directory or file '{arguments}' not found."
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
    'clear': {
        'description': 'Clear screen',
        'template': 'clear',
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


def show_tooltip(event):
    tooltip_text = event.widget.tooltip_text
    if tooltip_text:
        tooltip_toplevel.geometry(f"+{event.x_root+10}+{event.y_root+10}")
        tooltip_label.config(text=tooltip_text)
        tooltip_toplevel.deiconify()

def hide_tooltip(event):
    tooltip_toplevel.withdraw()

def validate_arguments(command, arguments):
    if not command:
        return False, "Please select a command."

    if command not in commands:
        return False, "Invalid command selected."

    if commands[command]['requires_arguments'] and not arguments:
        return False, "This command requires arguments. Please provide them."

    if not commands[command]['requires_arguments'] and arguments:
        return False, "This command does not require arguments. Please remove them."

    return True, ""

def clear_output_window():
    output_text.configure(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.configure(state='disabled')

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
        output_text.configure(state='disabled')
        return

    if command == 'clear':
        clear_output_window()
        return

    output_text.insert(tk.END, output + '\n')
    output_text.configure(state='disabled')

def show_command_info():
    command_info_window = tk.Toplevel(root)
    command_info_window.title('Command Information')

    content_frame = ttk.Frame(command_info_window)
    content_frame.pack(padx=20, pady=20)

    command_info_label = ttk.Label(content_frame, text='How to Use the Commands:', font=('SF Pro', 12, 'bold'))
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

def show_gui_instructions():
    gui_instructions_window = tk.Toplevel(root)
    gui_instructions_window.title('GUI Instructions')

    content_frame = ttk.Frame(gui_instructions_window)
    content_frame.pack(padx=20, pady=20)

    instructions_label = ttk.Label(content_frame, text='How to Use the Unix Commands GUI:', font=('SF Pro', 14, 'bold'))
    instructions_label.pack(pady=(0, 10))

    instructions_text = tk.Text(content_frame, width=60, height=20, font=('SF Pro', 12))
    instructions_text.pack()

    instructions = (
        "Welcome to the Unix Commands GUI!\n"
        "\n1. Select a command from the drop-down list.\n"
        "2. If the selected command requires arguments, enter them in the 'Arguments' field.\n"
        "3. Click the 'Run' button to execute the command.\n"
        "4. The output will be displayed in a separate window.\n"
        "5. To get information about each command, click the 'Command Info' button.\n"
        "\nCaution:\n"
        "   - Some commands used for viewing the content of files only work properly on .txt files.\n"
        "   - Some commands can make permanent changes to your file system.\n"
        "   - Be careful while using commands like 'rm', 'mv', 'mkdir', etc.\n"
        "   - Ensure that you have a backup or are certain of the command's effect.\n"
        "\nCommand Information:\n"
        "     - Click the 'Command Info' button to view a list of available commands and their descriptions.\n" 
    )

    instructions_text.insert(tk.END, instructions)
    instructions_text.configure(state='disabled')



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
arguments_entry.bind("<Enter>", show_tooltip)
arguments_entry.bind("<Leave>", hide_tooltip)

run_button = ttk.Button(content_frame, text='Run', command=run_button_click)
run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

tooltip_toplevel = tk.Toplevel(root)
tooltip_toplevel.withdraw() 
tooltip_toplevel.overrideredirect(True) 
tooltip_toplevel.attributes('-topmost', True)  

tooltip_label = ttk.Label(tooltip_toplevel, background="#ffffe0", borderwidth=0, relief=tk.SOLID, padding=(10, 5), wraplength=400)
tooltip_label.pack()

output_window = tk.Toplevel(root)
output_window.title('Output')

output_text = tk.Text(output_window, width=60, height=40, font=('SF Pro', 12))
output_text.pack(padx=20, pady=20)
output_text.configure(state='disabled')

buttons_label = ttk.Label(root, text="To get more information about usage, click the buttons below.")
buttons_label.pack()

instructions_button = ttk.Button(root, text='GUI Instructions', command=show_gui_instructions)
instructions_button.pack()

command_info_button = ttk.Button(root, text='Command Info', command=show_command_info)
command_info_button.pack()

empty_label = ttk.Label(root, text=" ")
empty_label.pack()

root.mainloop()
