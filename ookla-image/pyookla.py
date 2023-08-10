import matplotlib.pyplot as plt
import numpy as np
import json
import os

with open('/mnt/data/webserver/ookla/ooklalogs.json', 'r') as json_file:
    json_load = json.load(json_file)

download = json_load["download"]["bandwidth"] / 10**6
upload = json_load["upload"]["bandwidth"] / 10**6
ping = json_load["ping"]["latency"]
jitter = json_load["ping"]["jitter"]


labels = ['Download', 'Upload']
metrics = [download, upload]  # download # upload
x = np.arange(len(labels))
width = 0.55  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(0, download, width, color="blue")
rects2 = ax.bar(1, upload, width, color="green")

ax.set_ylim(top=max(metrics)*1.2)
plt.text(1, max(metrics)*1.15, 'Ping: %.2f ms' % ping, horizontalalignment='center',
         verticalalignment='center', fontsize=14, color='r')
plt.text(1, max(metrics)*1.08, 'Jitter: %.2f ms' % jitter, horizontalalignment='center',
         verticalalignment='center', fontsize=14, color='r')

ax.set_ylabel('Mbits/sec', fontweight='bold')
ax.set_title('Ookla Speedtest', fontweight='bold')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3, fontweight='bold')  # show values
ax.bar_label(rects2, padding=3, fontweight='bold')

fig.tight_layout()

if os.path.exists("/mnt/data/webserver/ookla/ooklalogs.jpg"):
    os.remove("/mnt/data/webserver/ookla/ooklalogs.jpg")

plt.show()
plt.savefig('/mnt/data/webserver/ookla/ooklalogs.jpg')
