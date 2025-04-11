import pandas as pd

colunas = [
    "cnpj_basico", "cnpj_ordem", "cnpj_dv", "identificador_matriz_filial", "nome_fantasia",
    "situacao_cadastral", "data_situacao_cadastral", "motivo_situacao_cadastral",
    "nome_cidade_exterior", "pais", "data_inicio_atividade", "cnae_fiscal",
    "cnae_fiscal_secundaria", "tipo_logradouro", "logradouro", "numero", "complemento",
    "bairro", "cep", "uf", "municipio", "ddd_1", "telefone_1", "ddd_2", "telefone_2",
    "ddd_fax", "fax", "email", "situacao_especial", "data_situacao_especial"
]

chunksize = 100000
resultados = []

for chunk in pd.read_csv(
    'estabelecimentos.csv',
    sep=';',
    encoding='latin1',
    names=colunas,
    header=None,
    low_memory=False,
    chunksize=chunksize
):
    # Filtro: empresas ativas
    ativas = chunk[chunk['situacao_cadastral'] == 2]

    # Filtro: com email preenchido
    ativas_com_email = ativas[ativas['email'].notna() & (ativas['email'].str.strip() != '')]

    # Conversão da data
    ativas_com_email.loc[:, 'data_inicio_atividade'] = pd.to_datetime(
        ativas_com_email['data_inicio_atividade'].astype(str), format='%Y%m%d', errors='coerce'
    )

    # Filtro: empresas iniciadas a partir de 2020
    ativas_recente = ativas_com_email[ativas_com_email['data_inicio_atividade'].dt.year >= 2020]

    # Seleção final
    colunas_selecionadas = [
        'cnpj_basico', 'cnpj_ordem', 'cnpj_dv', 'nome_fantasia', 'cnae_fiscal',
        'cnae_fiscal_secundaria', 'data_inicio_atividade', 'uf', 'municipio', 'email',
        'ddd_1', 'telefone_1', 'ddd_2', 'telefone_2'
    ]
    resultados.append(ativas_recente[colunas_selecionadas])

# Junta tudo
df_final = pd.concat(resultados)

# Salvar no CSV
df_final.to_csv('ativas.csv', sep=';', index=False, encoding='utf-8')

print("CSV gerado com sucesso com todos os chunks!")
