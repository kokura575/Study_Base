import numpy as np

def  get_sample() :
    s_data = []
    r = np.random.rand(50)　#標本数50個
    r = r * len(data)				#何番目のデータを取り出すか
    r_i = r.astype('int32')		#整数化
    
    for index in r_i :
        s_data.append(data[index])		#データ取り出し
        
    return np.array(s_data)
    
ave = []
for i in range(2000) :		#標本を2000個作る
    x = get_sample()
    ave.append(np.mean(x))		#得た標本の平均値
print(np.mean(np.array(ave)))	#標本の平均の平均
print(np.std(np.array(ave)))		#標本の平均の標準偏差
print(np.median(ave))				#標本の平均の中央値