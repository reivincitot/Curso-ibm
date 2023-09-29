# From Understanding to Preparation

# Introducción
# En este lab, continuaremos aprendiendo acerca de Data science methodology , y nos enfocaremos en el Entendimiento de la información y de la preparación de los datos o de la información

# En el lab 2 (De requisitos a Recopilación) aprendimos que la información que necesitamos para responder la pregunta desarrollada en la etapa de compresión del negocio, es decir ¿podemos automatizar el proceso de determinar la cocina de la receta dada?, están fácilmente disponible. Un investigador llamado Yong-Yeol recopiló miles de recetas de alimentos ( cocinas e ingredientes) de tres sitios web diferentes, a saber: www.menupan.com, www.epicurious.com, www.allrecepies.com

# Para mas información sobre Yong-Yeol Ahn y sus recetas, puedes leer su paper en http://yongyeol.com/papers/ahn-flavornet-2011.pdf


# Nota importante: Por favor nota que no se espera que sepas como programar en python el siguiente código busca ilustrar la etapa de la información recolectada, así que esta totalmente bien si no comprendes cada linea del código.

import re  # importando expresiones regulares
import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)

recipes = pd.read_csv("E:/Curso-ibm/Data Science Metodology/recipes.csv")

print("Data read into dataframe!")

# Mostramos las primeras lineas del dataframe

print(recipes.head())

# Obtenemos la dimensión del dataframe

print(recipes.shape)

# Nuestro dataset consiste de 57.691 recetas. Cada fila representa una receta, y por cada receta, su correspondiente cocina es documentada ademas de 384 ingredients existentes en las recetas o no, comenzando con almendras y terminando con zucchini.

# Sabemos que una receta básica de sushi incluye estos ingredientes:
# Arroz
# salsa de soja
# wasabi
# algunos pescados/vegetales

# Revisemos que los ingredientes existan en nuestro dataframe:

ingredients = list(recipes.columns.values)

print([match.group(0) for ingredient in ingredients for match in [
      (re.compile(".*(rice).*")).search(ingredient)] if match])
print([match.group(0) for ingredient in ingredients for match in [
      (re.compile(".*(wasabi).*")).search(ingredient)] if match])
print([match.group(0) for ingredient in ingredients for match in [
      (re.compile(".*(soy).*")).search(ingredient)] if match])

# Si, existen!!
# Arroz como rice
# wasabi como wasabi
# soja como soy_sauce.

# Asi que si la receta contiene los 3 ingredientes: arroz,salsa de soja y wasabi entonces podemos decir confiadamente que la receta es de la cocina japonesa, mantengamos esto en mente!

# Data preparation

# En esta sección, prepararemos la información para la siguiente etapa en Data science methodology, la cual es el modelado. Esta etapa implica explorar la información mas profundamente y asegurarse de que se encuentra en el formato correcto para el algoritmo de machine learning que seleccionamos en la etapa del acercamiento analítico. el cual es decision trees

# Primero, mirar la información para ver si necesita ser limpiada.

print(recipes["country"].value_counts())

# Al mirar la tabla de arriba, podemos realizar las siguientes observaciones:

# 1. La columna de cocinas esta rotulada como país, lo cual no es preciso.
# 2. Los nombres de las cocinas no son consistentes ya que no todos comienzan con una mayúscula.
# 3. Algunas cocinas están duplicadas como variación del nombre del país, tal como Vietnam y Vietnamita.
# 4. Algunas cocinas tiene muy pocas recetas.

# Vamos a arreglar estos problemas.
# Arreglar los nombres mostrando la cocina.
column_names = recipes.columns.values
column_names[0] = "cuisine"
recipes.columns = column_names

print(recipes)

# Cambiar todas las cocinas a minúsculas

recipes["cuisine"] = recipes["cuisine"].str.lower()

print(recipes["cuisine"])

# Hacer que el nombre de las cocinas sea consistente.
recipes.loc[recipes["cuisine"] == "austria", "cuisine"] = "austrian"
recipes.loc[recipes["cuisine"] == "belgium", "cuisine"] = "belgian"
recipes.loc[recipes["cuisine"] == "china", "cuisine"] = "chinese"
recipes.loc[recipes["cuisine"] == "canada", "cuisine"] = "canadian"
recipes.loc[recipes["cuisine"] == "netherlands", "cuisine"] = "dutch"
recipes.loc[recipes["cuisine"] == "france", "cuisine"] = "french"
recipes.loc[recipes["cuisine"] == "germany", "cuisine"] = "german"
recipes.loc[recipes["cuisine"] == "india", "cuisine"] = "indian"
recipes.loc[recipes["cuisine"] == "indonesia", "cuisine"] = "indonesian"
recipes.loc[recipes["cuisine"] == "iran", "cuisine"] = "iranian"
recipes.loc[recipes["cuisine"] == "italy", "cuisine"] = "italian"
recipes.loc[recipes["cuisine"] == "japan", "cuisine"] = "japanese"
recipes.loc[recipes["cuisine"] == "israel", "cuisine"] = "israeli"
recipes.loc[recipes["cuisine"] == "korea", "cuisine"] = "korean"
recipes.loc[recipes["cuisine"] == "lebanon", "cuisine"] = "lebanese"
recipes.loc[recipes["cuisine"] == "malaysia", "cuisine"] = "malaysian"
recipes.loc[recipes["cuisine"] == "mexico", "cuisine"] = "mexican"
recipes.loc[recipes["cuisine"] == "pakistan", "cuisine"] = "pakistani"
recipes.loc[recipes["cuisine"] == "philippinese", "cuisine"] = "philippine"
recipes.loc[recipes["cuisine"] == "scandinavia", "cuisine"] = "scandinavian"
recipes.loc[recipes["cuisine"] == "spain", "cuisine"] = "spanish_portuguese"
recipes.loc[recipes["cuisine"] == "portugal", "cuisine"] = "spanish_portuguese"
recipes.loc[recipes["cuisine"] == "switzerland", "cuisine"] = "swiss"
recipes.loc[recipes["cuisine"] == "thailand", "cuisine"] = "thai"
recipes.loc[recipes["cuisine"] == "turkey", "cuisine"] = "turkish"
recipes.loc[recipes["cuisine"] == "vientam", "cuisine"] = "vietnamese"
recipes.loc[recipes["cuisine"] == "uk-and-ireland", "cuisine"] = "uk-and-irish"
recipes.loc[recipes["cuisine"] == "irish", "cuisine"] = "uk-and-irish"
print(recipes)

# Remover cocinas con menos de 50 recetas.
recipes_count = recipes["cuisine"].value_counts()
cuisines_indices = recipes_count > 50

cuisines_to_keep = list(np.array(recipes_count.index.values)[
                        np.array(cuisines_indices)])

row_before = recipes.shape[0]
print(f"Numero de filas originales en el dataframe son {row_before}")

recipes = recipes.loc[recipes["cuisine"].isin(cuisines_to_keep)]

row_after = recipes.shape[0]
print(f"Numero de filas del dataframe procesado es {row_after}")
print(f"{row_before-row_after} filas removidas")

# Convertir todos los Yes a 1 y todos los No a 0
recipes = recipes.replace(to_replace="Yes", value=1)
recipes = recipes.replace(to_replace="No", value=0)

# Vamos a analizar la información un poco mas para aprender de mejor manera la información y ver alguna observación preliminar de interés
# Usemos el siguiente código para obtener la receta que contenga rice, soy, wasabi y seaweed.

print(recipes.head())

check_recipes = recipes.loc[
    (recipes["rice"]==1) &
    (recipes["soy_sauce"]==1) &
    (recipes["wasabi"]==1) &
    (recipes["seaweed"]==1)
]

print(check_recipes)

print("\nBasado en los resultados del código de arriba, podemos clasificar las recetas que contentan rice, soy, wasabi y seaweed como recetas japonesas? por que?\n")

print("No, porque otras recetas como la Asiática y la del Este de Asia también contienen estos ingredientes\n")

# Vamos a contar los ingredientes a traves de cada receta

ing = recipes.iloc[:,1:].sum(axis=0)
print(ing)

# Define cada columna como una serie de pandas

ingredient= pd.Series(ing.index.values, index=np.arange(len(ing)))
count = pd.Series(list(ing), index = np.arange(len(ing)))

# Crear el dataframe
ing_df = pd.DataFrame(dict(ingredient = ingredient, count = count))
ing_df = ing_df[["ingredient","count"]]
print(ing_df.to_string())

# Ahora que tenemos un dataframe de ingredientes y so conteo total a traves de las recetas. Vamos a ordenar esto de forma descendiente.

ing_df.sort_values(["count"], ascending=False, inplace=True)
ing_df.reset_index(inplace=True, drop=True)

print(ing_df)

# Como sea, nota que hay un problema con la tabla de arriba. hay 40.000 recetas americanas en nuestro dataset, lo que significa que la data esta sesgada referente a los ingredientes Americanos

# Por lo tanto, calculemos un resumen más objetivo de los ingredientes observando los ingredientes por cocina.

# Vamos a crear un perfil para cada cocina.
# En otras palabras, vamos a tratar de encontrar que ingredientes los Chinos típicamente usan, y que es la comida Canadiense

cuisines = recipes.groupby("cuisine").mean()

print(cuisines.head())

# Como se muestra arriba, hemos creado un dataframe donde cada fila es una cocina de cada columna(excepto a la primera columna) es un ingrediente, y el valor de la fila representa el porcentaje de cada ingrediente en la correspondiente cocina.

# Por ejemplo:

# almond esta presente a traves del 15.65% de todas las recetas Africanas
# butter esta presente a traves del 38.11% de todas las recetas Canadiense

# Imprimamos el perfil de cada cocina mostrando los cuatro ingredientes principales en cada una.

num_ingredients = 4 # Define el numero máximo de ingredientes a imprimir

# defina la función que imprimira los ingredientes top de cada cocina.
def print_top_ingredients(row):
    print(row.name.upper())
    row_sorted = row.sort_values(ascending = False)*100
    top_ingredients = list(row_sorted.index.values)[0:num_ingredients]
    row_sorted = list(row_sorted)[0:num_ingredients]

    for ind, ingredient in enumerate(top_ingredients):
        print("%s (%d%%)" % (ingredient, row_sorted[ind]),end=" ")
    print("\n")

# Aplica la función al dataframe cuisine

create_cuisines_profiles = cuisines.apply(print_top_ingredients,axis=1)

# A este punto, sentimos que emos entendido la información y la información esta lista y esta en el formato correcto para modelar