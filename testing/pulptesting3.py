import pulp
from pulp import *
import pandas as pd

data = pd.read_csv('tnn_data_1200_clicks.csv', engine='python')

clicks=1200.0

#Convert reporters from int to R#
for i in range(len(data['Reporter'])):
    data.loc[i,'Reporter']=str("R"+str(data.loc[i,'Reporter']))

article_name=[]
reporters=data['Reporter'].unique()

for i in range(len(data)):
    article_name.append(data.iloc[i]['Article'])
art_name={}
article_type={}
article_reporter={}
article_cost={}
article_clicks={}

#full x-set


for i in range(len(data)):
    art_name[data.iloc[i]['Article']]=data.iloc[i]['Article']
    article_type[data.iloc[i]['Article']]=data.iloc[i]['Type']
    article_reporter[data.iloc[i]['Article']]=data.iloc[i]['Reporter']
    article_cost[data.iloc[i]['Article']]=data.iloc[i]['Cost']
    article_clicks[data.iloc[i]['Article']]=data.iloc[i]['Clicks']
    #print(data.iloc[i]['Article'])
    #print(data.iloc[i]['Type'])


prob = LpProblem("Project_2", LpMinimize)
article_vars = LpVariable.dicts("Articles", article_name, lowBound=0, upBound=1)
reporter_vars= LpVariable.dicts("Reporter", reporters, lowBound=0)

possible_articles = [tuple(c) for c in allcombinations(article_name, len(data))]
choices = LpVariable.dicts(
    "article", possible_articles, lowBound=0, upBound=1, cat=LpInteger
)

print(x)
print(article_vars)
#Objective
prob += (
    lpSum([article_cost[i] * article_vars[i] for i in article_vars]),
    "Total Cost of articles",
)

#Constraints
prob += lpSum([article_clicks[i] * article_vars[i] for i in article_vars]) >= clicks, "Click Requirement"

for r in article_reporter:
    prob += lpSum(choices[r] for v in )

print(prob)

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)
    

for article in possible_articles:
    if x[article].value()==1.0:
        print(article)

print("Total Cost of Ingredients per can = ", value(prob.objective))