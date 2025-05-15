import pandas as pd

# Matplotlib para criar gráficos e visualizações básicas
import matplotlib.pyplot as plt

# Seaborn para criar gráficos estatísticos com estilo bonito e fácil
import seaborn as sns

# Importar dados de Crimes Violentos Excel
from leitura_dados import carregar_crimes_violentos

# Carregar os dados de Crimes Violentos
df = carregar_crimes_violentos()

# Funções para criar gráficos
def meio_empregado_cv():
  plt.figure(figsize=(10,6))
  sns.countplot(y='Meio Empregado', data=df, order=df['Meio Empregado'].value_counts().index)
  plt.title('Distribuição dos Meios Empregados')
  plt.xlabel('Quantidade')
  plt.ylabel('Meio Empregado')
  plt.show()

def natureza_cv():
  plt.figure(figsize=(10,6))
  sns.countplot(y='Natureza', data=df, order=df['Natureza'].value_counts().index)
  plt.title('Natureza dos Crimes Violentos')
  plt.xlabel('Quantidade')
  plt.ylabel('Natureza')
  plt.show()

def genero_cv():
  plt.figure(figsize=(8,6))
  sns.countplot(x='Gênero', data=df, order=df['Gênero'].value_counts().index)
  plt.title('Gênero das Vítimas')
  plt.xlabel('Gênero')
  plt.ylabel('Quantidade')
  plt.show()

def raca_cv():
  plt.figure(figsize=(8,6))
  sns.countplot(x='Raça da Vítima', data=df, order=df['Raça da Vítima'].value_counts().index)
  plt.title('Raça das Vítimas')
  plt.xlabel('Raça')
  plt.ylabel('Quantidade')
  plt.show()

def idade_cv():
  plt.figure(figsize=(10,6))
  sns.countplot(y='Idade da Vítima', data=df, order=df['Idade da Vítima'].value_counts().index)
  plt.title('Idade das Vítimas')
  plt.xlabel('Quantidade')
  plt.ylabel('Idade')
  plt.show()

def escolaridade_cv():
  plt.figure(figsize=(10,6))
  sns.countplot(y='Escolaridade da Vítima', data=df, order=df['Escolaridade da Vítima'].value_counts().index)
  plt.title('Escolaridade das Vítimas')
  plt.xlabel('Quantidade')
  plt.ylabel('Escolaridade')
  plt.show()

def municipio_cv():
  plt.figure(figsize=(12,10))
  top_municipios = df['Município'].value_counts().head(20)
  sns.barplot(x=top_municipios.values, y=top_municipios.index)
  plt.title('Top 20 Municípios com Mais Crimes Violentos')
  plt.xlabel('Quantidade')
  plt.ylabel('Município')
  plt.show()

def ais_cv():
  plt.figure(figsize=(10,6))
  sns.countplot(y='AIS', data=df, order=df['AIS'].value_counts().index)
  plt.title('Distribuição por Áreas Integradas de Segurança (AIS)')
  plt.xlabel('Quantidade')
  plt.ylabel('AIS')
  plt.show()

def ano_cv():
  df['Ano'] = pd.to_datetime(df['Data'], errors='coerce').dt.year
  plt.figure(figsize=(10,6))
  sns.countplot(x='Ano', data=df, order=sorted(df['Ano'].dropna().unique()))
  plt.title('Quantidade de Crimes por Ano')
  plt.xlabel('Ano')
  plt.ylabel('Quantidade')
  plt.xticks(rotation=45)
  plt.show()

def mes_cv():
  df['Mês'] = pd.to_datetime(df['Data'], errors='coerce').dt.month
  plt.figure(figsize=(10,6))
  sns.countplot(x='Mês', data=df, order=range(1,13))
  plt.title('Quantidade de Crimes por Mês')
  plt.xlabel('Mês')
  plt.ylabel('Quantidade')
  plt.show()

def dia_semana_cv():
  plt.figure(figsize=(10,6))
  dias_ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
  sns.countplot(x='Dia da Semana', data=df, order=dias_ordem)
  plt.title('Quantidade de Crimes por Dia da Semana')
  plt.xlabel('Dia da Semana')
  plt.ylabel('Quantidade')
  plt.show()

def horario_cv():
  df['Hora'] = pd.to_datetime(df['Hora'], errors='coerce').dt.hour
  plt.figure(figsize=(10,6))
  sns.countplot(x='Hora', data=df)
  plt.title('Distribuição dos Crimes por Horário')
  plt.xlabel('Hora do Dia')
  plt.ylabel('Quantidade')
  plt.show()
