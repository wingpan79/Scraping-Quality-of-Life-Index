#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
from datetime import datetime
data = {};
data = pd.DataFrame(data)
for x in range(2014, datetime.now().year +1 ):
    print(x)
    url = "https://www.numbeo.com/quality-of-life/rankings.jsp?title="+str(x)
    tables = pd.read_html(url)
    country_table = tables[1]
    del country_table['Rank']
    country_table['Year'] = x
    data = data.append(country_table, ignore_index=True)
data.to_csv("countries.csv", index=False)





