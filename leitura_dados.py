# Pandas para análise e manipulação de dados
import pandas as pd

# Unicodedata para normalização de strings
import unicodedata


# Função para limpar os colunas dos arquivos Excel
def limpar_colunas(df):
  # Remove espaços extras do cabecalho
  df.columns = df.columns.str.strip()

  # Remove acentos e outros caracteres do cabeçalho
  df.columns = [unicodedata.normalize('NFKD', col).encode('ascii', errors='ignore').decode('utf-8') for col in df.columns]
  return df


# Função para carregar e limpar o arquivo Entorpecentes Excel
def carregar_entorpecentes(caminho='Entorpecente_2009-a-2024.xlsx'):
  # Carregar e ler o arquivo Excel
  df = pd.read_excel(caminho)

  # Limpar
  df = limpar_colunas(df)
  return df


# Função para carregar e limpar o arquivo Crimes Violentos Excel
def carregar_crimes_violentos(caminho='CVLI_2009-2024.xlsx'):
  # Carregar e ler o arquivo Excel
  df = pd.read_excel(caminho)

  # Limpar
  df = limpar_colunas(df)
  return df

# Função para carregar e limpar o arquivo Crimes Sexuais Excel
def carregar_crimes_sexuais(caminho='Crimes-Sexuais_2009-a-2024.xlsx'):
  # Carregar e ler o arquivo Excel
  df = pd.read_excel(caminho)

  # Limpar
  df = limpar_colunas(df)
  return df
