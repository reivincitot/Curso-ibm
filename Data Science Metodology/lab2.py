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