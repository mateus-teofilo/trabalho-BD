# Matplotlib para criar gráficos e visualizações básicas
import matplotlib.pyplot as plt

# Seaborn para criar gráficos estatísticos com estilo bonito e fácil
import seaborn as sns

# Importar dados de Crimes Sexuais Excel
from leitura_dados import carregar_crimes_sexuais


# Carregar os dados de Crimes Sexuais
df = carregar_crimes_sexuais()

# Funções para criar gráficos
def genero_cs():
  print("Gráfico: Gênero Crimes Sexuais")

def raca_cs():
  print("Gráfico: Raça Crimes Sexuais")

def idade_cs():
  print("Gráfico: Idade Crimes Sexuais")

def escolaridade_cs():
  print("Gráfico: Escolaridade Crimes Sexuais")

def municipio_cs():
  print("Gráfico: Município Crimes Sexuais")

def ais_cs():
  print("Gráfico: Áreas Integradas de Segurança (AIS) Crimes Sexuais")

def ano_cs():
  print("Gráfico: Ano Crimes Sexuais")

def mes_cs():
  print("Gráfico: Mês Crimes Sexuais")

def dia_semana_cs():
  print("Gráfico: Dias da Semana Crimes Sexuais")

def horario_cs():
  print("Gráfico: Horários Crimes Sexuais")