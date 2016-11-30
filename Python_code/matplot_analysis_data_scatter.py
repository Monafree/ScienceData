%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as plk
from datetime import datetime

analysis_result = plk.load(open("/home/mona/Documents/Python/hep/query_with_row_start.plk"))

analysis_result_pd = pd.DataFrame(analysis_result)

analysis_result_pd['total_seconds']= analysis_result_pd.apply(lambda x: x['duration'].total_seconds(), axis = 1)
analysis_result_pd['total_ms'] = analysis_result_pd['total_seconds'] * 1000


plt.title("Query with row_start in HBase (1000 simulated traces with Python)")
plt.xlabel("Events Retrieved")
plt.ylabel("Time Consumption/ms")
plt.scatter(analysis_result_pd['got_num'],analysis_result_pd['total_ms'])
xmin, xmax = plt.xlim()
plt.xlim(0,xmax)
ymin, ymax = plt.ylim()
plt.ylim(0,ymax)

plt.hist(analysis_result_pd['total_ms'])



