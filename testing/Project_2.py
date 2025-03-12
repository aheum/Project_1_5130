#Objective: Minimize costo for articles

#Deciscion variables:
#Cost per reporter
#Type per article
#clicks per article


#Constraints
#Min one article per reporter
#Minimum clicks from readers to keep advertising
#Include one article of each type
#No type more than half of articles
#Additional 600 cost per extra article per reporter
#Subtract 115 per article

from pulp import *
import pandas as pd

limit=1200

data = pd.read_csv('tnn_data_1200_clicks.csv', engine='python')
print(data)

prob=LpProblem("Project_2", LpMinimize)

decision_variables=[]
for rownum, row in data.iterrows():
    variable = str('x' + str(rownum))
    variable = pulp.LpVariable(str(variable), lowBound = 0, upBound = 1, cat= 'Integer') #make variables binary
    decision_variables.append(variable)
    
print ("Total number of decision_variables: " + str(len(decision_variables)))
print ("Array with Decision Variables:" + str(decision_variables))



total_cost = ""
for rownum, row in data.iterrows():
    for i, schedule in enumerate(decision_variables):
        if rownum == i:
            formula = row['Cost']*schedule
            total_cost += formula
            
prob += total_cost
print ("Optimization function: " + str(total_cost))

