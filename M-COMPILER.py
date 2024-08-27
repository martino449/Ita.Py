import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Dictionary of substitutions as a constant
SUBSTITUTIONS = {
    'stampa': 'print',
    'se': 'if',
    'altrimenti': 'else',
    'altrimentise': 'elif',
    'definisci': 'def',
    'classe': 'class',
    'falso': 'False',
    'vero': 'True',
    'importa': 'import',
    'e': 'and',
    'stop': 'break',
    'mentre': 'while',
    'continua': 'continue',
    'perogni': 'for',
    'in': 'in',
    'ritorna': 'return',
    'prova': 'try',
    'eccetto': 'except',
    'finalmente': 'finally',
    'alza': 'raise',
    'con': 'with',
    'nonlocale': 'nonlocal',
    'globale': 'global',
    'lambda': 'lambda',
    'asincrono': 'async',
    'attendi': 'await',
    'non': 'not',
    'o': 'or',
    'è': 'is',
    'passa': 'pass',
    'aspetta': 'await',
    'asserisci': 'assert',
    'elimina': 'del',
    'nessuno': 'None'
}

def replace_word(input_file, output_file):
    """
    Replaces Italian keywords in a file with corresponding English keywords.

    Args:
        input_file (str): The path of the input file.
        output_file (str): The path of the output file.
    """
    try:
        with open(input_file, 'r') as f_input:
            content = f_input.read()

        for italian_word, english_word in SUBSTITUTIONS.items():
            content = re.sub(r'\b' + re.escape(italian_word) + r'\b', english_word, content)

        with open(output_file, 'w') as f_output:
            f_output.write(content)

        print(f"Replacement completed. The resulting file has been saved as '{output_file}'.")
        messagebox.showinfo("Success", f"Replacement completed. The resulting file has been saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        messagebox.showerror("Error", f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error: {e}")

def select_file():
    """
    Opens a file dialog to select a .M file and starts the word replacement process.
    """
    file_path = filedialog.askopenfilename(filetypes=[("M Files", "*.M")])
    if file_path:
        output_file = file_path.replace('.M', '_interpreted.py')
        replace_word(file_path, output_file)

def create_interface():
    """
    Creates and configures the application's graphical interface.
    """
    # Create the main window
    root = tk.Tk()
    root.title("M File to Python Converter")
    root.geometry("500x300")

    # Apply a modern style with ttk
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14), padding=10)
    style.configure("TFrame", padding=20)

    # Create a frame to centralize the widgets
    frame = ttk.Frame(root)
    frame.pack(expand=True)

    # Create buttons with modern style
    btn_select_file = ttk.Button(frame, text="Select .M File", command=select_file)
    btn_select_file.pack(pady=20)

    # Run the main window
    root.mainloop()

if __name__ == "__main__":
    create_interface()
