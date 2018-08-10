import pandas as pd
family_name=pd.Series(['Vega','Tina','Anita'])
family_age=pd.Series([47,54,35])
my_family=pd.DataFrame({'family name':family_name,'family age':family_age})
print(type(my_family[1:]))
print(my_family[1:])
pd.read_csv
