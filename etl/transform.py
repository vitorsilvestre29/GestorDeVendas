import pandas as pd
import logging

# Configuração do log
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validar_dados(df):
    # Validação de dados: verificar se há valores nulos
    if df.isnull().any().any():
        logging.warning("Há valores nulos nos dados transformados.")
    else:
        logging.info("Todos os dados transformados são válidos (sem nulos).")

    # Verificar tipos de dados
    if not pd.api.types.is_numeric_dtype(df['quantidade']):
        logging.warning("A coluna 'quantidade' deve ser numérica.")
    
    # Validação de valores negativos (exemplo de validação)
    if (df['quantidade'] < 0).any():
        logging.warning("Há valores negativos na coluna 'quantidade'.")

def transformar_dados():
    try:
        df = pd.read_excel('data/vendas.xlsx')
        df["preco_total"] = df["quantidade"] * df["preco_unitario"]
        df['data'] = pd.to_datetime(df['data'])
        
        # Chamar a função de validação
        validar_dados(df)

        logging.info(f'Dados transformados com sucesso, {len(df)} registros.')
        return df
    except Exception as e:
        logging.error(f"Erro ao transformar dados: {e}")
        raise

if __name__ == "__main__":
    df = transformar_dados()
    logging.info(df.head())
