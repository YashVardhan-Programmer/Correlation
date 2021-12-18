import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
  coffee = []
  week = []

  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
      coffee.append(float(row['Coffee in ml']))
      week.append(float(row['sleep in hours']))
  
  return{
      'x': coffee,
      'y': week,
  }

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource['x'],datasource['y'])
  print(correlation[0,1])
def setup():
  data_path = 'data.csv'
  datasource = getDataSource(data_path)
  findCorrelation(datasource)

setup()

with open('data.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = 'sleep in hours', y = 'Coffee in ml')
    fig.show()