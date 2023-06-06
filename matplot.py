import matplotlib.pyplot as plt

titulo = 'Digite o título do gráfico: '
legenda = 'Digite a legenda do gráfico: '
n = 10
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]

cores_barras = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'gray', 'cyan', 'magenta', 'brown']

plt.figure(figsize=(12, 6))
plt.style.use('ggplot')
plt.bar(x, y, label=f'{legenda}', color=cores_barras)
plt.xlabel('eixo X', fontsize=15)
plt.ylabel('eixo y', fontsize=15)
plt.title(f'{titulo}\n', fontsize=20)
plt.legend(fontsize=10)

plt.savefig('C:/Users/MATHEUS-COLISEU/Desktop/grafico2.png')
