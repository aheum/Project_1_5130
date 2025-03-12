import pulp
from pulp import *
import pandas as pd

def costs(articles,data):
    """
    pull out the cost from a list of articles
    """
    value=0
    for i in articles:
        value = value+int(data.loc[data['Article']==i, 'Cost'])  
    return (value)

def clicks(articles,data):
    """
    pull out the clicks from a list of articles
    """
    value=0
    for i in articles:
        value = value+int(data.loc[data['Article']==i, 'Clicks'])
        #print(data.loc[data['Article']==i, 'Clicks'])
    return (value)

data = pd.read_csv('tnn_data_1200_clicks.csv', engine='python')

#clicks=1200.0

for i in range(len(data['Reporter'])):
    data.loc[i,'Reporter']=str("R"+str(data.loc[i,'Reporter']))

#print(data)

data_article=[]
data_type=[]
data_reporter=[]
data_cost=[]
data_clicks=[]
for i in range(len(data)):
    data_article.append(data.loc[i,'Article'])
    data_type.append(data.loc[i,'Type'])
    data_reporter.append(data.loc[i,'Reporter'])
    data_cost.append(data.loc[i,'Cost'])
    data_clicks.append(data.loc[i,'Clicks'])

possible_articles = [tuple(c) for c in allcombinations(data_article, len(data))]
x = LpVariable.dicts(
    "articles", possible_articles, lowBound=0, upBound=1, cat=LpInteger
)

prob = LpProblem("Wedding Seating Model", LpMinimize)

#objective function
prob += lpSum([costs(table,data) * x[table] for table in possible_articles])


#constraints
prob += lpSum([clicks(table,data) * x[table] for table in possible_articles]) >= 1200

prob.solve()
for articles in possible_articles:
    if x[articles].value() == 1.0:
        print(articles)