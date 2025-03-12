"""
A set partitioning model of a wedding seating problem

Authors: Stuart Mitchell 2009
"""

import pulp

def happiness(table):
    """
    Find the happiness of the table
    - by calculating the maximum distance between the letters
    """
    return abs(ord(table[0]) - ord(table[-1]))

max_tables = 5
max_table_size = 4
guests = "A B C D E F G I J K L M N O P Q R".split()

possible_tables = [tuple(c) for c in pulp.allcombinations(guests, max_table_size)]
x = pulp.LpVariable.dicts(
    "table", possible_tables, lowBound=0, upBound=1, cat=pulp.LpInteger
)
print(x)

seating_model = pulp.LpProblem("Wedding Seating Model", pulp.LpMinimize)

seating_model += pulp.lpSum([happiness(table) * x[table] for table in possible_tables])

for guest in guests:
    print([x[table] for table in possible_tables if guest in table])
    seating_model += (
        pulp.lpSum([x[table] for table in possible_tables if guest in table]) == 1,
        f"Must_seat_{guest}",
    )


seating_model += (
    pulp.lpSum([x[table] for table in possible_tables]) <= max_tables,
    "Maximum_number_of_tables",
)