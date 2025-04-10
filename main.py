import pandas as pd


colunas = [
    "cnpj_basico", "cnpj_ordem", "cnpj_dv", "identificador_matriz_filial", "nome_fantasia",
    "situacao_cadastral", "data_situacao_cadastral", "motivo_situacao_cadastral",
    "nome_cidade_exterior", "pais", "data_inicio_atividade", "cnae_fiscal",
    "cnae_fiscal_secundaria", "tipo_logradouro", "logradouro", "numero", "complemento",
    "bairro", "cep", "uf", "municipio", "ddd_1", "telefone_1", "ddd_2", "telefone_2",
    "ddd_fax", "fax", "email", "situacao_especial", "data_situacao_especial"
]

estabelecimentos = pd.read_csv(
    'estabelecimentos.csv',
    sep=';',
    encoding='latin1',
    names=colunas,
    header=None,
    low_memory=False,
    nrows=500000  # 👉 lê só as primeiras 100 mil linhas
)

# Filtro: empresas ativas
ativas = estabelecimentos[estabelecimentos['situacao_cadastral'] == 2]

# Filtro: e que possuem email preenchido (não vazio e não nulo)
ativas_com_email = ativas[ativas['email'].notna() & (ativas['email'].str.strip() != '')]

# Selecionar colunas desejadas
colunas_selecionadas = [
    'cnpj_basico', 'nome_fantasia', 'cnae_fiscal', 'uf', 'municipio', 'email',
    'ddd_1', 'telefone_1', 'ddd_2', 'telefone_2', 'ddd_fax', 'fax'
]

ativas_reduzido = ativas_com_email[colunas_selecionadas]

# Salvar em CSV
ativas_reduzido.to_csv('ativas_com_email_e_telefones.csv', sep=';', index=False, encoding='utf-8')

