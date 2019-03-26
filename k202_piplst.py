# -*- coding: utf-8 -*-

import sys
import os
import pandas as pd
import pip
from pip._internal.utils.misc import get_installed_distributions
#=============
plst=get_installed_distributions();
print(plst[10])

df=pd.DataFrame();
df['<name>']=plst;
print(df.tail())
fss="tmp\\m100.csv";print("\n"+fss)
df.to_csv(fss,index=False)

