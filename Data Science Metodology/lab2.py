# Importamos la librearía para leer el dataframe
import pandas as pd


pd.set_option('display.max_columns',None)

download_recipes = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%202/recipes.csv"

download_recipes.to_csv("recipes.csv")
recipes_df = 'E:/Curso-ibm/Data Science Metodology/recipes.csv'


print(" Data read into dataframe!")

x = recipes_df.head()
print(x)

y = recipes_df.shape
print

# Nuestro data set consiste en 57.691 recetas, Cara fila representa una receta, y por cada receta su correspondiente cocina es documentada también con 384 ingredientes existentes en las recetas o no. Comienza con almendras y termina con zucchini

# Ahora que la recolección de información esta completa, data science usan estadísticas descriptivas y técnicas de visualización para entender de mejor manera la información y familiarizarse con ella. Data scientist, explora la información para:

# 1. Entender su contenido.
# 2. Verificar su calidad.
# 3. Encontrar un punto de vista interesante de forma preliminar
# 4. Determinar si información necesaria es requerida o rellenar cualquier falta de información 