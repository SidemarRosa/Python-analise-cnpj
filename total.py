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

# # Função para inserir dados em lotes
# def inserir_em_lote(tabela, dados, campos):
#     insert_query = f"""
#         INSERT INTO {tabela} ({', '.join(campos)})
#         VALUES ({', '.join(['%s'] * len(campos))})
#         ON DUPLICATE KEY UPDATE
#         {', '.join([f"{campo}=VALUES({campo})" for campo in campos])}
#     """
#     lote_tamanho = 1000
#     for i in range(0, len(dados), lote_tamanho):
#         lote = dados[i:i + lote_tamanho]
#         cursor.executemany(insert_query, lote)
#         conn.commit()

def inserir_em_lote(tabela, dados, campos):
    insert_query = f"""
        INSERT INTO {tabela} ({', '.join(campos)})
        VALUES ({', '.join(['%s'] * len(campos))})
        ON DUPLICATE KEY UPDATE
        {', '.join([f"{campo}=VALUES({campo})" for campo in campos])}
    """
    lote_tamanho = 1000
    total = len(dados)

    for i in range(0, total, lote_tamanho):
        lote = dados[i:i + lote_tamanho]
        cursor.executemany(insert_query, lote)
        conn.commit()

        # Cálculo da porcentagem
        percentual = ((i + len(lote)) / total) * 100
        print(f"Inserido {i + len(lote)} / {total} registros ({percentual:.2f}%)")

## Dividir o código em partes para facilitar a leitura e manutenção

# 1. Leitura do arquivo CSV sem cabeçalho
# df_empresas = pd.read_csv(
#     'empresas.csv',
#     sep=';',               # usa ; (tabulação) como separador
#     header=None,            # sem cabeçalho no arquivo
#     dtype=str,              # todas as colunas como string
#     encoding='latin1',      # evita erro de encoding
# )

# 1.2. Definindo os nomes das colunas manualmente
# campos_empresas = [
#     'cnpj_basico',
#     'razao_social',
#     'natureza_juridica',
#     'qualificacao_responsavel',
#     'capital_social',
#     'porte_empresa',
#     'ente_federativo_responsavel'
# ]

# 1.3. Atribuindo os nomes das colunas
# df_empresas.columns = campos_empresas

# 1.4. Preparando os dados para inserção
# dados_empresas = df_empresas.fillna('').values.tolist()
# print(f"Total de registros a serem inseridos: {len(dados_empresas)}")

# print("Inserindo dados na tabela 'empresas' agora!!!")
# 1.5. Inserção no banco
# inserir_em_lote('empresas', dados_empresas, campos_empresas)

# print("Dados inseridos na tabela 'empresas' com sucesso!")

# 2. Leitura do arquivo CSV sem cabeçalho
df_estabelecimentos = pd.read_csv(
    'estabelecimentos.csv',
    sep=';',               # usa ; como separador
    header=None,           # sem cabeçalho no arquivo
    dtype=str,             # todas as colunas como string
    encoding='latin1',     # evita erro de encoding
)

# 2.1. Definindo os nomes das colunas manualmente
campos_estabelecimentos = [
    'cnpj_basico', 'cnpj_ordem', 'cnpj_dv', 'identificador_matriz_filial', 'nome_fantasia', 
    'situacao_cadastral', 'data_situacao_cadastral', 'motivo_situacao_cadastral', 'nome_cidade_exterior',
    'pais_codigo', 'data_inicio_atividade', 'cnae_fiscal_principal', 'cnae_fiscal_secundaria', 'tipo_logradouro',
    'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'uf', 'municipio_codigo', 'ddd1', 'telefone1',
    'ddd2', 'telefone2', 'ddd_fax', 'fax', 'email', 'situacao_especial', 'data_situacao_especial'
]

# 2.2. Atribuindo os nomes das colunas
df_estabelecimentos.columns = campos_estabelecimentos

# 2.3. Preparando os dados para inserção
dados_estabelecimentos = df_estabelecimentos.fillna('').values.tolist()
print(f"Total de registros a serem inseridos: {len(dados_estabelecimentos)}")

# 2.4. Inserção no banco
print("Inserindo dados na tabela 'estabelecimentos' agora!!!")
inserir_em_lote('estabelecimentos', dados_estabelecimentos, campos_estabelecimentos)
print("Dados inseridos na tabela 'estabelecimentos' com sucesso!")


# 3. Leitura e inserção dos dados da tabela "simples"
# df_simples = pd.read_csv('simples.csv', dtype=str)
# campos_simples = [
#     'cnpj_basico', 'opcao_simples', 'data_opcao_simples', 'data_exclusao_simples', 'opcao_mei', 
#     'data_opcao_mei', 'data_exclusao_mei'
# ]
# dados_simples = df_simples[campos_simples].fillna('').values.tolist()
# inserir_em_lote('simples', dados_simples, campos_simples)
# print("Dados inseridos na tabela 'simples' com sucesso!")

# 4. Leitura do arquivo CSV sem cabeçalho
# df_socios = pd.read_csv(
#     'socios.csv',
#     sep=';',               # usa ; como separador
#     header=None,           # sem cabeçalho no arquivo
#     dtype=str,             # todas as colunas como string
#     encoding='latin1',     # evita erro de encoding
# )

# # 4.1. Definindo os nomes das colunas manualmente
# campos_socios = [
#     'cnpj_basico', 
#     'identificador_socio', 
#     'nome_socio_razao_social', 
#     'cpf_cnpj_socio', 
#     'qualificacao_socio',
#     'data_entrada_sociedade', 
#     'pais_codigo', 
#     'representante_legal_cpf', 
#     'nome_representante_legal', 
#     'qualificacao_representante_legal', 
#     'faixa_etaria'
# ]

# # 4.2. Atribuindo os nomes das colunas
# df_socios.columns = campos_socios

# # 4.3. Preparando os dados para inserção
# dados_socios = df_socios.fillna('').values.tolist()
# print(f"Total de registros a serem inseridos: {len(dados_socios)}")

# # 4.4. Inserção no banco
# print("Inserindo dados na tabela 'socios' agora!!!")
# inserir_em_lote('socios', dados_socios, campos_socios)
# print("Dados inseridos na tabela 'socios' com sucesso!")

# 5. Leitura e inserção dos dados da tabela "paises"
# df_paises = pd.read_csv(
#     'paises.csv', 
#     dtype=str, 
#     header=None, 
#     names=['codigo', 'descricao'],
#     encoding='latin1',
#     sep=';' 
# )
# campos_paises = ['codigo', 'descricao']
# dados_paises = df_paises[campos_paises].fillna('').values.tolist()
# inserir_em_lote('paises', dados_paises, campos_paises)
# print("Dados inseridos na tabela 'paises' com sucesso!")

# 6. Leitura e inserção dos dados da tabela "municipios"
# df_municipios = pd.read_csv(
#     'municipios.csv', 
#     dtype=str, 
#     header=None, 
#     names=['codigo', 'descricao'],
#     encoding='latin1',
#     sep=';' 
# )
# campos_municipios = ['codigo', 'descricao']
# dados_municipios = df_municipios[campos_municipios].fillna('').values.tolist()
# inserir_em_lote('municipios', dados_municipios, campos_municipios)
# print("Dados inseridos na tabela 'municipios' com sucesso!")

# 7. Leitura e inserção dos dados da tabela "qualificacoes_socios"
# df_qualificacoes_socios = pd.read_csv(
#     'qualificacoes_socios.csv', 
#     dtype=str, 
#     header=None, 
#     names=['codigo', 'descricao'],
#     encoding='latin1',
#     sep=';' 
# )
# campos_qualificacoes_socios = ['codigo', 'descricao']
# dados_qualificacoes_socios = df_qualificacoes_socios[campos_qualificacoes_socios].fillna('').values.tolist()
# inserir_em_lote('qualificacoes_socios', dados_qualificacoes_socios, campos_qualificacoes_socios)
# print("Dados inseridos na tabela 'qualificacoes_socios' com sucesso!")

# 8. Leitura e inserção dos dados da tabela "naturezas_juridicas"
# df_naturezas_juridicas = pd.read_csv(
#     'naturezas_juridicas.csv', 
#     dtype=str, 
#     header=None, 
#     names=['codigo', 'descricao'],
#     encoding='latin1',
#     sep=';' 
# )
# campos_naturezas_juridicas = ['codigo', 'descricao']
# dados_naturezas_juridicas = df_naturezas_juridicas[campos_naturezas_juridicas].fillna('').values.tolist()
# inserir_em_lote('naturezas_juridicas', dados_naturezas_juridicas, campos_naturezas_juridicas)
# print("Dados inseridos na tabela 'naturezas_juridicas' com sucesso!")

# 9. Leitura e inserção dos dados da tabela "cnaes"
# df_cnaes  = pd.read_csv(
#     'cnaes.csv', 
#     dtype=str, 
#     header=None, 
#     names=['codigo', 'descricao'],
#     encoding='latin1',
#     sep=';' 
# )
# campos_cnaes = ['codigo', 'descricao']
# dados_cnaes = df_cnaes[campos_cnaes].fillna('').values.tolist()
# inserir_em_lote('cnaes', dados_cnaes, campos_cnaes)
# print("Dados inseridos na tabela 'cnaes' com sucesso!")


# Fechar a conexão
cursor.close()
conn.close()
print("Conexão com o banco de dados fechada!")
