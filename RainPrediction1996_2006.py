import DataProcessing1996_2006 as Parser
from sklearn import tree
import numpy as np
from sklearn import ensemble
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd


result = Parser.getData();

TrainningData = result[0][0]
TrainningLabel = result[0][1]

TestingData = result[1][0]
TestingLabel = result[1][1]


A = ensemble.RandomForestRegressor();
B = tree.DecisionTreeRegressor();
C = linear_model.Lasso(alpha=0.1)
Models={}
Models["RForest"] = A
Models["DTree"] = B
Models["Linear"] = C


Best_Score = 0;
Best_Model = A;
Best_Model_Name = "RForest"
Scores = []
for modelName, model in Models.items():
    model.fit(TrainningData,TrainningLabel)
    score = model.score(TestingData,TestingLabel)
    Scores.append((modelName,[score]))
    if (score > Best_Score):
        Best_Score = score
        Best_Model = model
        Best_Model_Name = modelName

prediction = Best_Model.predict(TestingData)

Days = []
for i in range(1, 1097):
    Days.append(i)



df = pd.DataFrame.from_items(items=Scores,orient='index',columns=['Score'])
df.plot(kind ='bar' ,ylim =(0.9,1.0), figsize=(13,6),align='center',colormap='Accent')
plt.xticks(np.arange(len(Models)),df.index)

plt.figure(2,figsize=(15,6))
plt.plot(Days,TestingLabel,'g',label = 'Actual')
plt.legend(bbox_to_anchor=(1, 1), loc=2);

plt.plot(Days,prediction,'r', label = 'Prediction')
plt.legend(bbox_to_anchor=(1, 1), loc=2);
plt.xlabel("Days(2004.01.01-2006.12.31)")
plt.ylabel("Precip(mm)")
plt.title( Best_Model_Name + " model predicts precip(mm) from 2014-2016 (score: " + str(round(Best_Score,2)) + ")")

plt.show()