import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
dice_result = []
count = []
# print(dice1, dice2)

df = pd.read_csv('data.csv')

for i in range(0, 101):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2
    count.append(i)
    dice_result.append(diceTotal)

# fig = px.bar(dice_result, x = count, y = dice_result)
# fig.show()
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
fig.show()
fig2.show()

print(dice_result)
