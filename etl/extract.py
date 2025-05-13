import pandas as pd
import logging

# Configuração do log
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extrair_dados():
    try:
        caminho_arquivo = 'data/vendas.xlsx'
        df = pd.read_excel(caminho_arquivo)
        logging.info(f'Dados extraídos com sucesso, {len(df)} registros.')

        return df
    except Exception as e:
        logging.error(f"Erro ao extrair dados: {e}")
        raise

if __name__ == '__main__':
    extrair_dados()
