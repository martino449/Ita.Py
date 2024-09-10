import os
import re

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
        # Se il file non esiste, crea un file di output con un messaggio predefinito
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


if __name__ == "__main__":
    input_file = input("Inserisci il file di input: ")
    output_file = input("Inserisci il file di output (premi Invio per usare il nome di default): ")

    if not output_file:
        output_file = os.path.splitext(input_file)[0] + ".py"

    replace_word(input_file, output_file)

