import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
df.head() #Nesta função, pelos parênteses estarem vazios, apenas as primeiras 5 linhas da tela serão exibidas
df.info() #Descrição, por meio do Pandas, de o que a tabela selecionada possui de colunas e demais informações
df.describe() #Apresentam as informações e estáticas gerais da tabela selecionada
df.shape #Dimensão do arquivo, por meio de uma Tupla, destacando o valor de, respectivamente, as linhas e colunas do arquivo

linhas, colunas = df.shape[0] , df.shape[1]
print("Linhas: ", linhas)
print("Colunas: ", colunas)

df.columns
#Tradução das colunas de Inglês para Português
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_empregado',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)
df.columns
df["nivel_experiencia"].value_counts() #Método que calcula a frequência de cada categoria
df["tipo_emprego"].value_counts()

#Depois da renomeação das colunas, elas ficaram assim:

renomear_colunas = {
    'work_year': 'ano',
    'nivel_experiencia': 'senioridade',
    'tipo_emprego': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'moeda_salario': 'moeda',
    'salario_em_usd': 'usd',
    'residencia_empregado': 'residencia',
    'taxa_remoto': 'remoto',
    'localizacao_empresa': 'empresa',
    'tamanho_empresa': 'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)
df.columns

df["senioridade"].value_counts()
df["contrato"].value_counts()
df["remoto"].value_counts()
df["tamanho_empresa"].value_counts()

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executive',
}

df["senioridade"] = df["senioridade"].replace(senioridade)
df["senioridade"].value_counts()

contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freelance',
    'CT': 'Contrato',
}

df["contrato"] = df["contrato"].replace(contrato)
df["contrato"].value_counts()

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande',
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
df["tamanho_empresa"].value_counts()

remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto',
}

df["remoto"] = df["remoto"].replace(remoto)
df["remoto"].value_counts()

df.head() #Agora, apresentando uma tabela com todas as colunas e linhas renomeadas
df.describe(include="object") #Apresentando agora também dados categóricos


#Após executar a base do projeto, com o código da aula anterior...


df.isnull() #Apresenta todos os dados da tabela que são dispostos como nulos
df.isnull().sum() #Destaca entre as categorias das colunas onde estão dispostos os valores nulos
df["ano"].unique() #Todos os valores que são divergentes
df[df.isnull().any(axis=1)] #Apresenta todos os valores que são nulos, apresentando todas as colunas da base

import numpy as np

#Criação de um DataFrame como base de teste para usar de exemplo
df_salarios = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'salario': [4000, np.nan, 5000, np.nan, 100000],
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2)) #Calcula a média salarial e substitui os nulos pela média e arredonda os valores
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median()) #Calcula a mediana e substitui os nulos pela mediana
df_salarios

df_temperaturas = pd.DataFrame({
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'Temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill() #Usando a função ffil, os dados não numéricos são substituidos pelo valor anterior na tabela. A função bfill preenche de forma que os dados posteriores susbstituem os inválidos
df_temperaturas

df_cidades = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'cidade': ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]                      
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não Informado") #Neste novo caso, criamos um novo DataFrame com duas colunas: nome e cidade. Entretanto, criamos uma nova coluna, chamada "cidade_preenchida", à qual puxa os dados de cidade e substitui o dados inválidos com "Não Informado"
df_cidades

df_limpo = df.dropna()
df_limpo.isnull().sum()

df_limpo.head()
df_limpo.info()

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
df_limpo.info()
df_limpo.head()