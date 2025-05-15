from sqlalchemy import create_engine
import logging
from etl.transformacao import transformar_dados

# Configuração do log
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ✅ String de conexão corrigida com TrustServerCertificate
string_conexao = (
    "mssql+pyodbc://Vitor/db_teste?"
    "trusted_connection=yes&"
    "driver=ODBC+Driver+18+for+SQL+Server&"
    "TrustServerCertificate=yes"
)

engine = create_engine(string_conexao, fast_executemany=True)

def carregar_dados(df):
    try:
        df.to_sql('vendas', con=engine, if_exists='append', index=False)
        logging.info(f'Dados carregados com sucesso, {len(df)} registros inseridos.')
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise

if __name__ == '__main__':
    from etl.extracao import gerar_dados
    df = transformar_dados(gerar_dados())
    carregar_dados(df)
