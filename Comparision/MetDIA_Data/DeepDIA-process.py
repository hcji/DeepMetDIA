# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:57:03 2020

@author: hcji
"""

import os
import pandas as pd
from DeepDIA.DeepDIA import DeepDIA_process

Dir = 'E:/project/MetDIA demo data/data'
files = os.listdir(Dir)
files = [f for f in files if '.mzXML' in f]
for f in files:
    f = Dir + '/' + f
    ft, fo = f, f
    dda_result = pd.read_csv(ft.replace('.mzXML', '.ms2.csv'))
    features = dda_result[['mz', 'rt', 'maxo']]
    features.columns = ['mz', 'rt', 'intensity']
    dia_result = DeepDIA_process(f, features)
    dia_result.to_csv(fo.replace('.mzXML', '.deepdia.csv'))
    