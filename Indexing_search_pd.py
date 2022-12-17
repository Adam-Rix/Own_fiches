import pandas as pd

x = int(input())
data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
   'rank': [4, 1, 3, 5, 2, 6]
}

df = pd.DataFrame(data, index = data['name'])

print(df)
print('=========')

print(df['name'][df['rank'] == x]) #If we`ve erase the ['name'] we will have a table of trigger indexes true\false