import pulp
from pulp import *
import pandas as pd

def retrieve_costs(article,data):
    costs=[]
    for i in article:
        costs.append(data.loc[data['Article'] == i]['Cost'])
    return costs

limit=1200

data = pd.read_csv('tnn_data_1200_clicks.csv', engine='python')
print(data.iloc[1])

decision_variables=[]

for row in range(len(data)):
    print(data.iloc[row][0])
    variable=data.iloc[row][0]
    variable = pulp.LpVariable(str(variable), lowBound = 0, upBound = 1, cat= 'Integer') #make variables binary
    decision_variables.append(variable)

print(decision_variables)

#Decision variables
possible_articles = [tuple(c) for c in allcombinations(decision_variables,len(data))]
#print(possible_articles)

x = pulp.LpVariable.dicts(
    "article", possible_articles, lowBound=0, upBound=1, cat=LpInteger
)
#print(x)

article_prob=LpProblem("Project_2", LpMinimize)

#[print("dingus",x[article]) for article in possible_articles]
#[print(article) for article in possible_articles]

#for article in possible_articles:
#    article_prob += pulp.lpSum()
#This is how you retieve
#data.loc[data['Article'] == art]['Cost']

#[[ print(data.loc[data['Article'] == art]['Cost']) for art in article ] for article in possible_articles]


#[print("Testing", article) for article in possible_articles]
ding=('A1','A2')
print(data['Article'])
print(data[data['Article'].isin(list(ding))])
#for articles in possible_articles:
#    print(articles)
print(type(decision_variables[1]))

#article_prob += pulp.lpSum([retrieve_costs(article,data) * x[article] for article in possible_articles])