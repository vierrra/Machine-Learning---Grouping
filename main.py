import pandas as pd 
from sklearn.cluster import KMeans

csv = pd.read_csv('dados.csv', sep=(','))
data      = csv.values
attributes = data[:,4:]

model = KMeans(3)
model.fit(attributes)

print('Informe os dados da postagem para que seja dito o grupo vinculado!')
numberComments = int(input('Número de comentários: '))
numberShares   = int(input('Número de compartilhamentos: '))
numberLikes    = int(input('Número de Likes: '))
numberLoves    = int(input('Número de Loves: '))
numberWows     = int(input('Número de Wows: '))
numberHahas    = int(input('Numero de risos: '))
numberSads     = int(input('Número de Carinha Triste: '))
numberAngrys   = int(input('Número de raiva: '))

valuesModel = model.predict([
    [numberComments, numberShares, numberLikes, numberLoves, numberWows, numberHahas, numberSads, numberAngrys]
])

print('Grupo', int(valuesModel))