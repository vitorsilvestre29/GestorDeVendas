
from etl.extracao import gerar_dados
from etl.transformacao import transformar_dados
from etl.load import carregar_dados

def executar_etl():
    df = gerar_dados()
    df = transformar_dados(df)
    carregar_dados(df)

if __name__ == '__main__':
    executar_etl()
