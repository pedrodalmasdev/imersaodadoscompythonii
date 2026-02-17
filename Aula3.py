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


#Após executar a base do projeto, com o código da segunda aula (Junção do código pra primeira + segunda aula)...


df_limpo.head()

df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição de Senioridade") #Criação de um gráfico de barras com as informações da coluna senioridade e seus atributos
#Entretanto, este gráfico foi feito apenas utilizando a biblioteca Pandas. Importando outras bibliotecas, nós podemos deixar nossos gráficos mais compreensíveis

import seaborn as sns
sns.barplot(data=df_limpo, x='senioridade', y='usd') #Criação de um gráfico de barras com a biblioteca seaborn. Entretanto, este gráfico não está ordenado e não possui titulo.

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salário Médio por Nível de Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salário Médio Anual (USD)")
plt.show() #Agora, com as bibliotecas seaborn e matplotlib, o gráfico possui nome para os eixos e título. Porém, seus dados não estão ordenados.

df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False) #Agora, utilizando a função groupby, ordenamos as informações da tabela em ordem decrescente, para que o gráfico apresente dessa forma.
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index #Varíavel que inclui a função

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order = ordem)
plt.title("Salário Médio por Nível de Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salário Médio Anual (USD)")
plt.show() #Agora, fazendo o gráfico com a varíavel ordenada, as barras agora são dispostas de forma decrescente.

plt.figure(figsize=(10, 5))
sns.histplot(data=df_limpo['usd'], bins = 50, kde=True)
plt.title("Distribuição de Salários Anuais")
plt.xlabel("Salário Médio Anual (USD)")
plt.ylabel("Frequência")
plt.show() #Este novo gráfico é um histograma. Dessa forma, além de definirmos que os dados abordados serão os salários em usd

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário Médio Anual (USD)")
plt.show() #Neste gráfico Boxplot (Distribuição de um valor numérico em certos grupos), vemos a distribuição dos salários por meio de: mínimos, primeiro quartil, mediana, terceiro quartil e máximo.

ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executive']

plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Salário Médio Anual (USD)")
plt.show() #Agora vemos a distribuição de senioridade em relação aos salários respectivos, indicando suas medianas e discrepâncias

ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executive']

plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade') #Formatamos o gráfico aplicando uma paleta de cores e em qual coluna será aplicada a distribuição de cores
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Salário Médio Anual (USD)")
plt.show()

import plotly.express as px #Biblioteca para garantir interatividade nos gráficos

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index() #Distribuição dos dados em forma decrescente

fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'}
             )

fig.show() #Gráfico interativo usando as informações do df_limpo

remoto_contagem = df_limpo['remoto'].value_counts().reset_index() #Definição de uma variável com as informações específicas de uma coluna do df_limpo
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção Tipos de Trabalho',
             )
fig.show() #Exibição de um gráfico de pizza simples

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção Tipos de Trabalho',
             hole=0.5 #Aplicação de buraco no meio do gráfico de pizza
             )
fig.show()

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção Tipos de Trabalho',
             hole=0.5
             )

fig.update_traces(textinfo='percent+label') #Distribuição dos valores dentro de cada área destacada, relevando porcentagem e título
fig.show()
