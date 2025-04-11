import pandas as pd
import mysql.connector

# Conexão
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="receitafederal",
    port=3306
)

cursor = conn.cursor()
print("Conexão com MySQL estabelecida com sucesso!")

# Leitura do CSV
df = pd.read_csv('ativas.csv', sep=';', dtype=str, low_memory=False)

# Montar o CNPJ completo
df['cnpj'] = (
    df['cnpj_basico'].str.zfill(8) +
    df['cnpj_ordem'].str.zfill(4) +
    df['cnpj_dv'].str.zfill(2)
)

# Dados para inserção
dados = df[[  
    'cnpj', 'nome_fantasia', 'cnae_fiscal', 'cnae_fiscal_secundaria',
    'data_inicio_atividade', 'uf', 'municipio', 'email',
    'ddd_1', 'telefone_1', 'ddd_2', 'telefone_2'
]].fillna('').values.tolist()

# Query de inserção
insert_query = """
    INSERT INTO empresas_ativas (
        cnpj, nome_fantasia, cnae_fiscal, cnae_fiscal_secundaria,
        data_inicio_atividade, uf, municipio, email,
        ddd_1, telefone_1, ddd_2, telefone_2
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

# Inserção em lotes
lote_tamanho = 1000
for i in range(0, len(dados), lote_tamanho):
    lote = dados[i:i + lote_tamanho]
    cursor.executemany(insert_query, lote)
    conn.commit()

cursor.close()
conn.close()
print("Dados inseridos com sucesso!")