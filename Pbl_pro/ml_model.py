import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def predict_college(cet_score):
    df = pd.read_csv('output_file.csv')
    a = 'comp'
    df = df.sort_values(a, ascending=False)

    for i in range(len(df)):
        if cet_score >= df.iloc[i][a]:
            college = df.iloc[i]['name']
            a = df.iloc[i]
            break

    return college
