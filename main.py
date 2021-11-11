import pandas as pd
import requests as rq
import getpass

user = getpass.getuser()
fileloc = "C:\\Users\\"+user+"\\Desktop\\data.csv"
url = 'https://en.wikipedia.org/wiki/List_of_American_films_of_2020'
html = rq.get(url).content
df_list = []
try:
    df_list = pd.read_html(html)
except ValueError:
    print('no tables found')
sizer = []
print(str(len(df_list)) + " tables found")
for i in range(len(df_list)):
    print(df_list[i])
    print('----------------------------------')
    sizer.append([len(df_list[i]), i])
    sizer.sort()

df = df_list[sizer[len(sizer)-1][1]]
df.to_csv('data.csv', index=False)
print("saved in " + fileloc)
