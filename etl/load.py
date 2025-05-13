from sqlalchemy import create_engine
import logging
from transform import transformar_dados

# Configuração do log
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

string_conexao = "mssql+pyodbc://Vitor/db_teste?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(string_conexao, fast_executemany=True)

def carregar_dados(df):
    try:
        df.to_sql('vendas', con=engine, if_exists='append', index=False)
        logging.info(f'Dados carregados com sucesso, {len(df)} registros inseridos.')
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise

if __name__ == '__main__':
    df = transformar_dados()
    carregar_dados(df)
