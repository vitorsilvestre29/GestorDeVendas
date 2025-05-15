import time
import subprocess
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def agendar_etl(intervalo_minutos=30):
    while True:
        logging.info("Executando pipeline ETL agendado")
        subprocess.run(['python', 'auto_etl.py'], check=True)
        logging.info(f"Pipeline ETL finalizado, aguardando {intervalo_minutos} minutos para próxima execução")
        time.sleep(intervalo_minutos * 60)

if __name__ == "__main__":
    agendar_etl()
