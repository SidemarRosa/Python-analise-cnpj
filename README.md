# 📊 Análise de Estabelecimentos Ativos - Receita Federal (CNPJs)

Este projeto tem como objetivo analisar dados públicos de estabelecimentos registrados na Receita Federal, filtrando os **CNPJs ativos com email** e salvando em uma nova base com informações essenciais.

## ✅ Objetivos

- Carregar a base de dados da Receita Federal (CSV)
- Filtrar apenas empresas com **situação cadastral ativa (código 2)**
- Selecionar apenas empresas com **email preenchido**
- Manter informações de **contato**, como DDDs e telefones (mesmo que vazios)
- Gerar nova tabela `ativas_com_email_e_telefones.csv` com os dados filtrados

## 🛠️ Requisitos

- Python 3.10 ou superior
- Pandas

## Estrutura
📂 Python-analise-cnpj/ <br>
├── estabelecimentos.csv                -- Coloque o arquivo da receita federal <br>
├── main.py                            -- Script principal da análise <br>
├── ativas_com_email_e_telefones.csv  -- Resultado gerado pelo script <br>
└── README.md                          -- Este arquivo
<br>


### Instalação do Pandas:

```bash
pip install pandas
```

### clone o projeto
git clone https://github.com/SidemarRosa/Python-analise-cnpj.git
cd Python-analise-cnpj

### Cole o arquivo da receita federal, como pro exemplo (estabelecimentos.csv)

### Execute o script
python main.py

### Resultado das empresas filtradas ficam no arquivo gerado "ativas_com_email_e_telefones.csv"

Projeto desenvolvido por Sidemar Rosa, com foco em aprendizado prático de análise de dados com Python, a partir de dados públicos da Receita Federal.
