import DataProcessing as dp
from sklearn import tree
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch


data,label = dp.getData()
X_train, X_test, y_train, y_test= model_selection.train_test_split(data, label, test_size=0.3)
clf = tree.DecisionTreeRegressor()
clf.fit(X_train,y_train)
print (clf.score(X_test,y_test))
prediction = clf.predict(X_test)

Days = []
for i in range(1,111):
    Days.append(i)

plt.figure(1)
plt.plot(Days,y_test,'g')
plt.legend(bbox_to_anchor=(1, 1), loc=2);

plt.figure(2)
plt.plot(Days,prediction,'r')
plt.legend(bbox_to_anchor=(1, 1), loc=2);

plt.show()
