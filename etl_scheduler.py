import subprocess
import os

# Caminho absoluto ou relativo da pasta onde estão os scripts
etl_dir = os.path.join(os.getcwd(), 'etl')

# Lista dos scripts para executar
scripts = ['extract.py', 'transform.py', 'load.py']

# Executar os scripts
for script in scripts:
    script_path = os.path.join(etl_dir, script)
    print(f"Executando {script_path}")
    subprocess.run(['python', script_path], check=True)
