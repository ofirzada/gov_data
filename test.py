print("hello")
import pandas as pd

df= pd.DataFrame()


dict = {'First Name': 'Vikram', 'Last Name': 'Aruchamy', 'Country': 'India'}

df = df.append(dict, ignore_index = True)

print(df)