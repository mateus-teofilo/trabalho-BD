# Matplotlib para criar gráficos e visualizações básicas
import matplotlib.pyplot as plt

# Seaborn para criar gráficos estatísticos com estilo bonito e fácil
import seaborn as sns

# Importar dados de Entorpecentes Excel
from leitura_dados import carregar_entorpecentes


# Carregar os dados de Entorpecentes
df = carregar_entorpecentes()

# Funções para criar gráficos
def tipo_entorpecente(df):
  plt.figure(figsize=(10, 6))
  sns.countplot(data=df, y='Tipo de Entorpecente', order=df['Tipo de Entorpecente'].value_counts().index)
  plt.title('Total de Apreensões por Tipo de Entorpecente')
  plt.xlabel('Quantidade')
  plt.ylabel('Tipo de Entorpecente')
  plt.tight_layout()
  plt.show()

def peso_entorpecente(df):
  plt.figure(figsize=(10, 6))
  sns.histplot(df['Quantidade (Kg)'], bins=30, kde=True)
  plt.title('Distribuição de Peso das Apreensões')
  plt.xlabel('Peso (Kg)')
  plt.ylabel('Frequência')
  plt.tight_layout()
  plt.show()

def municipio_entorpecente(df):
  top_municipios = df['Municipio'].value_counts().head(10)
  plt.figure(figsize=(10, 6))
  sns.barplot(x=top_municipios.values, y=top_municipios.index)
  plt.title('Top 10 Municípios com Mais Apreensões de Entorpecentes')
  plt.xlabel('Quantidade')
  plt.ylabel('Município')
  plt.tight_layout()
  plt.show()

def ais_entorpecente(df):
  plt.figure(figsize=(10, 6))
  sns.countplot(data=df, y='AIS', order=df['AIS'].value_counts().index)
  plt.title('Apreensões por Área Integrada de Segurança (AIS)')
  plt.xlabel('Quantidade')
  plt.ylabel('AIS')
  plt.tight_layout()
  plt.show()

def ano_entorpecente(df):
  df['Ano'] = df['Data'].dt.year
  plt.figure(figsize=(10, 6))
  sns.countplot(data=df, x='Ano')
  plt.title('Apreensões por Ano')
  plt.xlabel('Ano')
  plt.ylabel('Quantidade')
  plt.tight_layout()
  plt.show()

def mes_entorpecente(df):
  df['Mês'] = df['Data'].dt.month
  plt.figure(figsize=(10, 6))
  sns.countplot(data=df, x='Mês')
  plt.title('Apreensões por Mês')
  plt.xlabel('Mês')
  plt.ylabel('Quantidade')
  plt.tight_layout()
  plt.show()

def dia_semana_entorpecente(df):
    dias_ordem = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Dia da Semana', order=dias_ordem)
    plt.title('Apreensões por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def horario_entorpecente(df):
    df['Hora'] = df['Hora'].astype(str)
    df['Hora'] = df['Hora'].str[:2]
    df['Hora'] = df['Hora'].astype(int)
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Hora', order=sorted(df['Hora'].unique()))
    plt.title('Apreensões por Hora do Dia')
    plt.xlabel('Hora (24h)')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()