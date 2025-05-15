
import pandas as pd
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validar_dados(df):
    if df.isnull().any().any():
        logging.warning("Dados contêm valores nulos.")
    if not pd.api.types.is_numeric_dtype(df['quantidade']):
        logging.warning("Coluna 'quantidade' deve ser numérica.")
    if (df['quantidade'] < 0).any():
        logging.warning("Valores negativos em 'quantidade'.")

def transformar_dados(df):
    try:
        df['preco_total'] = df['quantidade'] * df['preco_unitario']
        df['data'] = pd.to_datetime(df['data'])
        validar_dados(df)
        logging.info(f'{len(df)} registros transformados com sucesso.')
        return df
    except Exception as e:
        logging.error(f"Erro na transformação: {e}")
        raise
