#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: drapor
"""
import pandas as pd
import numpy as np
print('Importing the data...')
train_set = pd.read_csv('train.csv')
pixel = train_set.iloc[:,1:785]
label = train_set.iloc[:,0]
test_set = pd.read_csv('test.csv')
r = []
for t in range(len(test_set)):
        print('%d/28000' % (t+1))
    a = np.array(test_set.loc[t])
    d = []
    for i in range(len(train_set)):
        b = np.array(pixel.loc[i])
        d.append(np.dot((a-b).T,(a-b)))
    k = list(zip(d,range(len(d))))
    k.sort()
    m = []
    for i in k[:10]:
        m.append(label.loc[i[1]])
    r.append(sum(m)/10)
