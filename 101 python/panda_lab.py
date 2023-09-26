import pandas as pd
import numpy as np
# Leer un archivo csv
csv_path = "D:/Curso ibm/TopSellingAlbums.csv"

df = pd.read_csv(csv_path)
#------------------------------------------------
# Leer un archivo excel(.xlsx)
# xls_path = "D:/Curso ibm/TopSellingAlbums.xlsx"
# df = pd.read_excel(xls_path)

# print(df)
# -----------------------------------------------------------------
# Podemos acceder a la columna Length y asignarla a un nuevo dataframe
# x = df[["Length"]]
#print(x)
#------------------------------------------------------------

# Viendo Información y accediendo a información

#obtener la columna como una serie
# x = df["Length"]
# print(x)
# ------------------------------------------
# obtener columnas como un dataframe
# x= df [["Artist"]]
# print(type(x))

#Puedes hacer lo mismo con multiples columnas; solo pondremos el nombre del dataframe en este caso df y el nombre de las multiples columnas encerrados en braquets dobles, el resultado es un nuevo dataframe comprendido de las columnas especificadas
# y = df[["Artist","Length","Genre"]]
# print(y)

#------------------------------------------------------------
#una manera de obtener un unico elemento es el metodo iloc, donde puedes acceder a la primera fila de la primera columna

# print(df.iloc[0,0])
# print(df.iloc[1,0])
# print(df.iloc[0,2])
# print(df.iloc[1,2])

# Tambien puedes acceder a la columna usando el nombre tambien

# print(df.loc[0,"Artist"])
# print(df.loc[1,"Artist"])
# print(df.loc[0,"Released"])
# # print(df.loc[1,"Released"])

# Puedes hacer slice usando ambos el index y el nombre de la columna

for n in range(3):

    print(n)
