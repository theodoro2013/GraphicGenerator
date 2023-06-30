import pandas as pd
import matplotlib.pyplot as plt

'''
conhece_zap = planilha['plataforma_conhece1']
conhece_gsuite = planilha['plataforma_conhece2']
conhece_face = planilha['plataforma_conhece3']
conhece_insta = planilha['plataforma_conhece4']
conhece_moodle = planilha['plataforma_conhece5']
conhece_trello = planilha['plataforma_conhece6']
conhece_ms365 = planilha['plataforma_conhece7']
conhece_jamboard = planilha['plataforma_conhece8']
conhece_kahoot = planilha['plataforma_conhece9']
conhece_poliedro = planilha['plataforma_conhece10']
conhece_aude = planilha['plataforma_conhece11']
conhece_plurall = planilha['plataforma_conhece12']
conhece_yt = planilha['plataforma_conhece13']
conhece_mec = planilha['plataforma_conhece14']
conhece_nenhuma = planilha['plataforma_conhece15']
'''
planilha = 'C:\REPOSITORIOS\Yasmine\GraphicGenerator\DadosYasmine.xlsx'
df = pd.read_excel(planilha)

# Lista das colunas desejadas
colunas = ['plataforma_conhece1', 'plataforma_conhece2', 'plataforma_conhece3', 'plataforma_conhece4', 'plataforma_conhece5', 'plataforma_conhece6', 'plataforma_conhece7', 'plataforma_conhece8', 'plataforma_conhece9', 'plataforma_conhece10', 'plataforma_conhece11', 'plataforma_conhece12', 'plataforma_conhece13', 'plataforma_conhece14', 'plataforma_conhece15']

# Converter as colunas em strings
df[colunas] = df[colunas].astype(str)

# Converter os valores "Sim" para 1 e "Não" para 0
df[colunas] = df[colunas].replace({"Sim": 1, "Não": 0})

# Plotar o gráfico de barras comparando as 15 colunas
df[colunas].sum().plot(kind='bar')
plt.title('Comparação das Informações')
plt.xlabel('Colunas')
plt.ylabel('Quantidade')
plt.show()