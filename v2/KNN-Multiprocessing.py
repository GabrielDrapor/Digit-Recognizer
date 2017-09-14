#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description:
kaggle 0 

@author: drapor
"""

import pandas as pd
import numpy as np
import multiprocessing
import os
#import matplotlib.pyplot as plt

def processing(test_set):
    s = []
    print("Running... pid:" + str(os.getpid()))
    for idx, df in test_set.iterrows():
        print('%d/28000, pid %s' % (idx, os.getpid()))
        a = np.array(df)
        d = []
        for i in range(42000):
            b = np.array(pixel.iloc[i])
            d.append(np.dot((a-b).T,(a-b)))
        k = list(zip(d,range(len(d))))
        k.sort()
        m = []
        for i in k[:10]:
            m.append(label.loc[i[1]])
        s.append([idx,sum(m)/10])
    return s

if __name__ == '__main__':
    print('Importing the data...')
    train_set = pd.read_csv('train.csv')
    pixel = train_set.iloc[:,1:785]
    label = train_set.iloc[:,0]
    #plt.imshow(test.reshape(28,28), cmap=plt.cm.gray)
    test_set = pd.read_csv('test.csv')
    pool = multiprocessing.Pool(processes = 16)
    r = []
    for i in range(16):
        train = test_set.loc[1750*i:1750*(i+1)-1]
        r.append(pool.apply_async(processing,(train,)))
    pool.close()
    pool.join()
    result  = []
    for i in r:
        for j in i.get():
            result.append(j)
    result.sort()
    with open('result.csv',"w") as f:
        for i in result:
            f.writelines(str(i[0])+','+str(round(i[1]))[:-2]+'\n')