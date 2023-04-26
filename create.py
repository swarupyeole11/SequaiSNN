import pandas as pd

dataset = []

with open("data.txt", "r") as data:
    a = data.readlines()
    for x in a:
        b = x.split(" ")
        c = []
        for i in b:
            if i == "":
                pass
            else:
                if i == "\n":
                    c.append(float(i[-1][:-1]))
                else:
                    c.append(float(i))
        # print(c)
        dataset.append(c)

print(dataset[-20:])

df = pd.DataFrame(dataset, columns = ['tm', 'Tsp1', "T1", "Q1", "P", "ierr", "D", "iae"])
df.to_csv('dataset.csv')