import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime as dt
sns.set()


from import_data import import_data
df = import_data('export_20190301_3A9B9D.csv')

# divide the time serie in events
from event_generator import event_generator
events_list = event_generator(df,4)

# select the short events
for i in range(len(events_list)-1,-1,-1):
    if len(events_list[i]) > 15:
        del events_list[i]
from tools import events2array
events_array = events2array(events_list)
print(events_array.shape)

# To choose the cluster number
# kmax = 5
# from Clustering import calculate_WSS
# WSS = calculate_WSS(events_array,kmax)
#
# from Clustering import calculate_Silouette
# sil = calculate_Silouette(events_array,kmax)
#
# ax = plt.gca()
# ax2 = ax.twinx()
#
# ax.plot(range(2,kmax+2),WSS)
# ax2.plot(range(2,kmax+1),sil)
# plt.show()

from Clustering import K_means
clusters = K_means(events_array,2)


# plot results
for k in np.arange(2):
    folder = str(k+1) + '/'
    clust_index = np.where(clusters == k)
    for i in clust_index[0]:
        events_list[i].plot.bar()
        name = 'figures/' + folder + 'figure_' + str(i) + '.png'
        plt.title(events_list[i].index[0])
        plt.savefig(name)
        plt.close()
