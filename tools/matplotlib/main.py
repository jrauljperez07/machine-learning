import matplotlib.pyplot as plt
import numpy as np

# Crear los datos
X = np.arange(0, 100)
y = X * 2
z = X ** 2

# Crear una figura
fig = plt.figure()

# Añadir ejes al canvas de la figura en la posición [0,0,1,1]
ax = fig.add_axes([0, 0, 1, 1])

# Graficar (X,y) en esos ejes
ax.plot(X, y)

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')

# Mostrar el gráfico
plt.show()
