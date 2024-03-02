
from mlxtend.frequent_patterns import *
import pandas as pd
transactions = int(input("Enter the number of transactions: "))
data = {}
for i in range(transactions):
    items = input(f"Enter the items for transaction {i+1} (separated by spaces): ").split()
    for item in items:
        if item not in data:
            data[item] = [0] * transactions
        data[item][i] = 1
df=pd.DataFrame(data)
while True:
    support=float(input("enter the minimum support value : ")) 
    itemset=apriori(df,min_support=support,use_colnames=True)
    itemset['length']=itemset['itemsets'].apply(lambda x:len(x))
    print("all frequent itemsets:")
    print(data)
    mlength=max(itemset['length'])
    for length in range(1,mlength+1):
        print(f"frequent{length}-itemsets:")
        print(itemset[itemset['length']==length])
        print()
    print("all association rules:")
    rules=association_rules(itemset,metric="confidence",min_threshold=0)
    rules=rules[['antecedents','consequents','antecedent support','confidence','lift']]
    print(rules)
    confidence=float(input("enter the minimum confidence value: "))
    validrules=rules[(rules['antecedent support']>=support)&(rules['confidence']>=confidence)]
    invalidrules=rules[~rules.index.isin(validrules.index)]
    print("valid association rules:")
    print(validrules)
    print("invalid association rules:")
    print(invalidrules)
