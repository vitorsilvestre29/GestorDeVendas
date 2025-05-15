
import pandas as pd
import random
import logging
from datetime import datetime, timedelta
import faker

logging.basicConfig(filename='logs/etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

fake = faker.Faker()

produtos = ['Smartphone', 'Notebook', 'Tablet', 'Smartwatch', 'Fone de Ouvido']

def gerar_dados(n=50):
    try:
        dados = []
        for i in range(n):
            dados.append({
                'id_venda': i + 1,
                'data': fake.date_between(start_date='-30d', end_date='today'),
                'cliente': fake.name(),
                'produto': random.choice(produtos),
                'quantidade': random.randint(1, 5),
                'preco_unitario': round(random.uniform(100.0, 5000.0), 2)
            })

        df = pd.DataFrame(dados)
        logging.info(f'{n} registros gerados com sucesso.')
        return df
    except Exception as e:
        logging.error(f"Erro ao gerar dados: {e}")
        raise
