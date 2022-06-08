
#%%
import pandas as pd

path = r"C:\Users\csucuogl\Documents\GitHub\WebThings\Project.xls"
df = pd.read_excel( path )
df

#%%

df.to_json(
    r"C:\Users\csucuogl\Documents\GitHub\WebThings\Project_Test.json",
    orient='records'
)
