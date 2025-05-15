from leitura_dados import (
  carregar_entorpecentes,
  carregar_crimes_violentos,
  carregar_crimes_sexuais,
)
from entorpecentes import (
  tipo_entorpecente,
  peso_entorpecente,
  municipio_entorpecente,
  ais_entorpecente,
  ano_entorpecente,
  mes_entorpecente,
  dia_semana_entorpecente,
  horario_entorpecente,
)
from crimes_violentos import (
  meio_empregado_cv,
  natureza_cv,
  genero_cv,
  raca_cv,
  idade_cv,
  escolaridade_cv,
  municipio_cv,
  ais_cv,
  ano_cv,
  mes_cv,
  dia_semana_cv,
  horario_cv,
)
from crimes_sexuais import (
  genero_cs,
  raca_cs,
  idade_cs,
  escolaridade_cs,
  municipio_cs,
  ais_cs,
  ano_cs,
  mes_cs,
  dia_semana_cs,
  horario_cs,
)

# Menu Principal
def menu():
  print("\n=== PROJETO BIG DATA - CRIMINALIDADE NO CEARÁ ===")
  print("1. Dados de Apreensão de Entorpecentes")
  print("2. Dados de Crimes Violentos")
  print("3. Dados de Crimes Sexuais")
  print("0. Sair")

# Menu de Apreensão de Entorpecentes
def menu_entorpecentes():
  print("\n=== APREENSÃO DE ENTORPECENTES ===")
  print("1. Ver os primeiros 10 dados de Apreensão de Entorpecentes")
  print("2. Gráfico: Tipos de entorpecentes")
  print("3. Gráfico: Peso")
  print("4. Gráfico: Município")
  print("5. Gráfico: Áreas Integradas de Segurança (AIS)")
  print("6. Gráfico: Ano")
  print("7. Gráfico: Mês")
  print("8. Gráfico: Dias da semana")
  print("9. Gráfico: Horários")
  print("0. Voltar")

# Menu de Crimes Violentos
def menu_crimes_violentos():
  print("\n=== CRIMES VIOLENTOS ===")
  print("1. Ver os primeiros 10 dados de Crimes Violentos")
  print("2. Gráfico: Meio empregado")
  print("3. Gráfico: Gênero")
  print("4. Gráfico: Raça")
  print("5. Gráfico: Idade")
  print("6. Gráfico: Escolaridade")
  print("7. Gráfico: Município")
  print("8. Gráfico: Áreas Integradas de Segurança (AIS)")
  print("9. Gráfico: Ano")
  print("10. Gráfico: Mês")
  print("11. Gráfico: Dias da semana")
  print("12. Gráfico: Horários")
  print("0. Voltar")

# Menu de Crimes Sexuais
def menu_crimes_sexuais():
  print("\n=== CRIMES SEXUAIS ===")
  print("1. Ver os primeiros 10 dados de Crimes Sexuais")
  print("2. Gráfico: Gênero")
  print("3. Gráfico: Raça")
  print("4. Gráfico: Idade")
  print("5. Gráfico: Escolaridade")
  print("6. Gráfico: Município")
  print("7. Gráfico: Áreas Integradas de Segurança (AIS)")
  print("8. Gráfico: Ano")
  print("9. Gráfico: Mês")
  print("10. Gráfico: Dias da semana")
  print("11. Gráfico: Horários")
  print("0. Voltar")

if __name__ == "__main__":
  df_entorpecentes = carregar_entorpecentes()
  df_crimes_violentos = carregar_crimes_violentos()
  df_crimes_sexuais = carregar_crimes_sexuais()

  while True:
    # Menu Principal
    menu()
    escolha = input("Escolha uma opção: ")
    
    # Menu de Entorpecentes
    if escolha == "1":
      while True:
        menu_entorpecentes()
        escolha_entorpecente = input("Escolha uma opção: ")

        # Escolhas do menu de Entorpecentes
        if escolha_entorpecente == "1":
          df_entorpecentes = carregar_entorpecentes()
          print(df_entorpecentes.head(10))

        elif escolha_entorpecente == "2":
          tipo_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "3":
          peso_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "4":
          municipio_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "5":
          ais_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "6":
          ano_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "7":
          mes_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "8":
          dia_semana_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "9":
          horario_entorpecente(df_entorpecentes)

        elif escolha_entorpecente == "0":
          break

        else:
          print("Opção inválida. Tente novamente.")
      
    # Menu de Crimes Violentos
    elif escolha == "2":
      while True:
        menu_crimes_violentos()
        escolha_crimes_violentos = input("Escolha uma opção: ")

        # Escolhas do menu de Crimes Violentos
        if escolha_crimes_violentos == "1":
          df_crimes_violentos = carregar_crimes_violentos()
          print(df_crimes_violentos.head(10))
        
        elif escolha_crimes_violentos == "2":
          meio_empregado_cv()

        elif escolha_crimes_violentos == "3":
          natureza_cv()

        elif escolha_crimes_violentos == "4":
          genero_cv()
        
        elif escolha_crimes_violentos == "5":
          raca_cv()

        elif escolha_crimes_violentos == "6":
          idade_cv()
        
        elif escolha_crimes_violentos == "7":
          escolaridade_cv()
        
        elif escolha_crimes_violentos == "8":
          municipio_cv()

        elif escolha_crimes_violentos == "9":
          ais_cv()
        
        elif escolha_crimes_violentos == "10":
          ano_cv()
        
        elif escolha_crimes_violentos == "11":
          mes_cv()

        elif escolha_crimes_violentos == "12":
          dia_semana_cv()
        
        elif escolha_crimes_violentos == "13":
          horario_cv()
        
        elif escolha_crimes_violentos == "0":
          break

        else:
          print("Opção inválida. Tente novamente.")
    
    # Menu de Crimes Sexuais
    elif escolha == "3":
      while True:
        menu_crimes_sexuais()
        escolha_crimes_sexuais = input("Escolha uma opção: ")

        # Escolhas do menu de Crimes Sexuais
        if escolha_crimes_sexuais == "1":
          df_crimes_sexuais = carregar_crimes_sexuais()
          print(df_crimes_sexuais.head(10))
        
        elif escolha_crimes_sexuais == "2":
          genero_cs()

        elif escolha_crimes_sexuais == "3":
          raca_cs()
        
        elif escolha_crimes_sexuais == "4":
          idade_cs()

        elif escolha_crimes_sexuais == "5":
          escolaridade_cs()
        
        elif escolha_crimes_sexuais == "6":
          municipio_cs()
        
        elif escolha_crimes_sexuais == "7":
          ais_cs()

        elif escolha_crimes_sexuais == "8":
          ano_cs()
        
        elif escolha_crimes_sexuais == "9":
          mes_cs()
        
        elif escolha_crimes_sexuais == "10":
          dia_semana_cs()

        elif escolha_crimes_sexuais == "11":
          horario_cs()

        elif escolha_crimes_sexuais == "0":
          break

        else:
          print("Opção inválida. Tente novamente.")

    elif escolha == "0":
      print("Encerrando...")
      break

    else:
      print("Opção inválida. Tente novamente.")
