import plotly.figure_factory as pf

import random

diceSum = []

for i in range(0,100):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    diceSum.append(d1+d2)


graph = pf.create_distplot([diceSum] , ["Sum of 2 Dices"])

graph.show()


