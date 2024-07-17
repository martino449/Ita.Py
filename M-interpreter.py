import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def sostituisci_parola(file_input, file_output):
    try:
        with open(file_input, 'r') as f_input:
            content = f_input.read()

        sostituzioni = {
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

        for parola_italiana, parola_inglese in sostituzioni.items():
            content = re.sub(r'\b' + re.escape(parola_italiana) + r'\b', parola_inglese, content)

        with open(file_output, 'w') as f_output:
            f_output.write(content)

        print(f"Sostituzione completata. Il file risultante è stato salvato come '{file_output}'.")
        messagebox.showinfo("Successo", f"Sostituzione completata. Il file risultante è stato salvato come '{file_output}'.")

    except FileNotFoundError:
        print(f"Errore: Il file '{file_input}' non è stato trovato.")
        messagebox.showerror("Errore", f"Errore: Il file '{file_input}' non è stato trovato.")
    except Exception as e:
        print(f"Errore: {e}")
        messagebox.showerror("Errore", f"Errore: {e}")

def seleziona_file():
    file_path = filedialog.askopenfilename(filetypes=[("File M", "*.M")])
    if file_path:
        file_output = file_path.replace('.M', '_interpretato.py')
        sostituisci_parola(file_path, file_output)

# Creazione della finestra principale
root = tk.Tk()
root.title("Convertitore di File .M a Python")
root.geometry("500x300")

# Applicare uno stile moderno con ttk
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)
style.configure("TFrame", padding=20)

# Creazione del frame per centralizzare i widget
frame = ttk.Frame(root)
frame.pack(expand=True)

# Creazione dei pulsanti con stile moderno
btn_seleziona_file = ttk.Button(frame, text="Seleziona File .M", command=seleziona_file)
btn_seleziona_file.pack(pady=20)

# Esecuzione della finestra principale
root.mainloop()
