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
    'niente': 'None'
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

