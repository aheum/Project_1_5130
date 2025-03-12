import pulp
from pulp import *
import pandas as pd

def costs(articles,data):
    """
    pull out the cost from a list of articles
    """
    value=0
    for i in articles:
        x=data.loc[data['Article']==i,'Cost']
        #print('X cost',x.iloc[0])
        #value = value+int(data.loc[data['Article']==i,'Cost'])
        value = value+x.iloc[0]
    return (value)

def clicks(articles,data):
    """
    pull out the clicks from a list of articles
    """
    value=0
    for i in articles:
        x=data.loc[data['Article']==i,'Clicks']
        value = value+x.iloc[0]
        #print(data.loc[data['Article']==i, 'Clicks'])
    return (value)



data = pd.read_csv('tnn_data_1200_clicks.csv', engine='python')
click_number=int(os.path.basename('tnn_data_1200_clicks.csv').split("_")[2])
print(click_number)

#clicks=1200.0

for i in range(len(data['Reporter'])):
    data.loc[i,'Reporter']="R"+str(data.loc[i,'Reporter'])

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
data_reporter=set(data_reporter)
data_type=set(data_type)



possible_articles = [tuple(c) for c in allcombinations(data_article, len(data))]
x = LpVariable.dicts(
    "articles", possible_articles, lowBound=0, upBound=1, cat=LpInteger
)

#print(possible_articles)

prob = LpProblem("Project 2", LpMinimize)

#objective function
#prob += lpSum([costs(articles,data) * x[articles] for articles in possible_articles])

#Modified problem solution to account for articles
prob += lpSum([costs(articles,data) * x[articles] for articles in possible_articles])



#Constraints:
#C1: Each reporter is assigned at least once
for reporter in data_reporter:
    #print(lpSum([x[articles] for articles in possible_articles if data.loc[data['Article'].isin(articles)]['Reporter'].str.contains(reporter).any()]) >= 1)
    prob += (
        
        lpSum([x[articles] for articles in possible_articles if data.loc[data['Article'].isin(articles)]['Reporter'].str.contains(reporter).any()]) >= 1,
        f"Must_include_{reporter}"
    )

#C2: Clicks is above 1200
prob += lpSum([clicks(articles,data) * x[articles] for articles in possible_articles]) >= click_number



#Temp Constraint
#prob += (
#        lpSum([x[articles] for articles in possible_articles if len(articles) >=len(data_type)]) == 1,
#        f"Just to eliminate the earlier instances/combinations that aren't getting selected correctly."
#)



#C3: Each article type is assigned at least once
for type in data_type:
    prob += (
        lpSum([x[articles] for articles in possible_articles if data.loc[data['Article'].isin(articles)]['Type'].str.contains(type).any()] ) >= 1,
        f"Must_include_{type}."
    )
    
   
#C4: No article type greater than half the number of articles chosen
for type in data_type:
    prob +=(
        lpSum([x[articles] for articles in possible_articles if sum(data.loc[data['Article'].isin(articles)]['Type'].str.count(type)) <= (len(articles)/2)]) ==1,
        f"Type must be <= number of articles{type}."
    )

#C5: If more than one article per reporter, Cost+=100 for each article

for reporter in data_reporter:
    #print(lpSum([x[articles] for articles in possible_articles if data.loc[data['Article'].isin(articles)]['Reporter'].str.contains(reporter).any()]) >= 1)
    prob += (
        
        lpSum([(costs(articles,data) + (sum(data.loc[data['Article'].isin(articles)]['Reporter'].str.count(reporter)))*100) * x[articles] for articles in possible_articles]),
        f"Pay_{reporter}_Plus_100_For_Each_Article_Past_First"
    )

#prob += lpSum([(costs(articles,data) + (sum(data.loc[data['Article'].isin(articles)]['Reporter'].str.count(reporter))-1)*100) * x[articles] for articles in possible_articles])

#Ensure 

#print([x[articles].value() for articles in possible_articles])
prob.solve()
#print([x[articles].value() for articles in possible_articles])
prob.solve()
for articles in possible_articles:
    if x[articles].value() == 1.0:
        print(articles)
