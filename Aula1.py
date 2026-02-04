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