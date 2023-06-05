'''
import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3']
valores = [20, 35, 15]
cores = ['blue', 'green', 'red']

# Criando o gráfico de barras
plt.bar(categorias, valores, color=cores)

# Adicionando legenda ao gráfico com as cores
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Criando a legenda com as cores
legendas = ['Legenda 1', 'Legenda 2', 'Legenda 3']
handles = [plt.Rectangle((0,0),1,1, color=cor) for cor in cores]
plt.legend(handles, legendas)

# Exibindo o gráfico
plt.savefig('C:/Users/MATHEUS-COLISEU/Desktop/grafico.png')

'''
import matplotlib.pyplot as plt

titulo = 'Digite o título do gráfico: '
legenda = 'Digite a legenda do gráfico: '
n = 10
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]


fp = '.'
tp = 40

plt.figure(figsize=(12, 6))
plt.style.use('ggplot')
plt.scatter(x, y, label=f'{legenda}', color='k', s=tp, marker=f'{fp}')
plt.xlabel('eixo X', fontsize=15)
plt.ylabel('eixo y', fontsize=15)
plt.title(f'{titulo}\n', fontsize=20)
plt.legend(fontsize=10)

plt.savefig('C:/repositorios/yasmine/graphicgenerator/grafico.png')