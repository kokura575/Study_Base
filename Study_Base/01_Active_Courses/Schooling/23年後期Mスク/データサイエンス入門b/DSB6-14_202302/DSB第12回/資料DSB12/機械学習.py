import pandas as pd
#ファイルから読み込む
df = pd.read_csv('/content/data1.csv')

import matplotlib.pyplot as plt
#散布図を描く
plt.scatter('x' , 'y' , data=df , c='label')


from sklearn import linear_model
#分類器の準備
clf = linear_model.LogisticRegression()

import numpy as np
#訓練データと結果データに分ける
data = df.values
y_train = data[: , 0]
X_train = data[: , 1:3]

#学習させる
clf.fit(X_train , y_train)

#指定のデータを準備
X_test = np.array([[10,40],[30,60],[60,60]])

#指定のデータで予測
pred = clf.predict(X_test)

#結果を表示
pred

#グリッドの座標を求める
array = np.mgrid[0:70:0.5 , 20:105:0.5]
x = array[0].ravel()
y = array[1].ravel()
X_test = np.c_[x,y]


#グリッドの全ての点を予測する
pred = clf.predict(X_test)

#予測結果をPandasに変換
df_X = pd.DataFrame(X_test , columns=['x' , 'y'])
df_y = pd.DataFrame(pred, columns=['label'])
df_pred = pd.concat([df_X , df_y] , axis=1)

#結果をグラフの表示
plt.scatter('x' , 'y' , c='label' , data = df_pred , s=1)
plt.scatter('x' , 'y' , c='label' , data=df , s=20)