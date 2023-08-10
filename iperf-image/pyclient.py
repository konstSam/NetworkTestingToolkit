import json
import matplotlib.pyplot as plt
import os

with open('/mnt/data/webserver/iperf3logs.json', 'r') as json_file:
    json_load = json.load(json_file)

data2 = []
data = json_load['intervals']
for x in range(0, len(data)):
    data2.append(data[x]['sum'])
val = []
for i in range(len(data2)):
    val.append((data2[i]['bits_per_second'], data2[i]['end']))

time = []
nums = []
for i in range(len(val)):
    x, y = val[i]
    time.append(int(y))
    nums.append(x/10**6)

avg = sum(nums)/len(nums)

plt.style.use('seaborn-darkgrid')
plt.plot(time, nums, marker='o', markerfacecolor='blue',
         markersize=3, label='Intervals')
plt.xticks(time)
plt.xlabel('seconds')
plt.ylabel('Mbps')
plt.title('Iperf3 Logs', fontweight='bold')
plt.axhline(y=avg, color='r', linestyle=':', label='Average %.1f' % avg)
plt.legend()

if os.path.exists("/mnt/data/webserver/iperf3logs.jpg"):
    os.remove("/mnt/data/webserver/iperf3logs.jpg")

if min(nums)-10 < 0:
    lim = 0
else:
    lim = min(nums)/1.1

plt.ylim([lim, max(nums)*1.1])
plt.show()
plt.savefig('/mnt/data/webserver/iperf3logs.jpg')
