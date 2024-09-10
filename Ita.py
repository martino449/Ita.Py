import os
import re
import subprocess

# Dizionario di sostituzioni come costante
SUBSTITUTIONS = {
    'stampa': 'print',
    'se': 'if',
    'altrimenti': 'else',
    'altrimentise': 'elif',
    'definisci': 'def',
    'classe': 'class',
    'Falso': 'False',
    'Vero': 'True',
    'importa': 'import',
    '__nome__': '__name__'
    '__principale__": '__main__'
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
    'asincrono': 'async',
    'attendi': 'await',
    'non': 'not',
    'o': 'or',
    'è': 'is',
    'ignora': 'pass',
    'elimina': 'del',
    'vuota': 'None',
    'apri': 'open'
}

def replace_word(input_file, output_file="convertito.py"):
    """
    Sostituisce le parole chiave italiane in un file con le corrispondenti parole chiave inglesi.
    Se il file di input non esiste, crea un file di output con un messaggio predefinito.

    Args:
        input_file (str): Il percorso del file di input.
        output_file (str): Il percorso del file di output.
    """
    if not os.path.exists(input_file):
        with open(output_file, 'w') as f_output:
            f_output.write("# Questo file è stato creato perché l'input non è stato trovato.\n")
        print(f"Il file di input '{input_file}' non esiste. Un file di output vuoto è stato creato come '{output_file}'.")
        return

    try:
        with open(input_file, 'r') as f_input:
            content = f_input.read()

        for italian_word, english_word in SUBSTITUTIONS.items():
            content = re.sub(r'\b' + re.escape(italian_word) + r'\b', english_word, content)

        with open(output_file, 'w') as f_output:
            f_output.write(content)

        print(f"Sostituzione completata. Il file risultante è stato salvato come '{output_file}'.")

    except Exception as e:
        print(f"Errore: {e}")

def validate_syntax(file_path):
    """
    Convalida la sintassi del file Python convertito.
    Args:
        file_path (str): Il percorso del file da validare.
    """
    try:
        subprocess.check_call(["python", "-m", "py_compile", file_path])
        print("Nessun errore di sintassi rilevato.")
    except subprocess.CalledProcessError:
        print("Errore di sintassi nel file convertito.")

def compile_and_run(input_file):
    """
    Compila il file e lo esegue.
    Args:
        input_file (str): Il percorso del file di input da convertire, compilare ed eseguire.
    """
    output_file = os.path.splitext(input_file)[0] + "_convertito.py"

    # Sostituzione delle parole chiave
    replace_word(input_file, output_file)

    # Convalida sintattica
    validate_syntax(output_file)

    # Esecuzione del file convertito
    try:
        subprocess.run(["python", output_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del file: {e}")

if __name__ == "__main__":
    input_file = input("Inserisci il file di input: ")
    compile_and_run(input_file)












#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.
