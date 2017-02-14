# OpenVPN-Stats

Python script to display statistics for open vpn


How to run the script with a cron:
```
  #this will start the webserver displaing the statistics
  @reboot /usr/bin/python /home/pi/scripts/ovpnstats/openvpn_display_html.py

  #this will fetch and agregate stats each minute
  */1 * * * * sudo /usr/bin/python /home/pi/scripts/ovpnstats/openvpn_stats.py /dev/null 2>&1
```

After running openvpn_display_html.py it will create a webserver on port:8075 to display the statistics.
You can change this port by modifying the last line of the script.

Here is how the statistics look:

```
------- Total --------
Common Name               Real Address         Download        Upload               Last Online
user1                     82.112.169.26       928.03 KB     715.20 KB  Mon Oct  3 11:49:48 2016
user2                     82.112.169.26       783.10 MB     142.89 MB  Tue Feb 14 13:05:21 2017
user3                     85.118.77.146         4.29 GB       2.93 GB  Tue Feb 14 13:04:05 2017
hjelev                    85.118.92.81         41.63 GB      10.30 GB  Wed Jan 25 15:23:01 2017
UNDEF                     85.118.81.119        55.95 KB      19.26 KB  Tue Feb 14 15:06:18 2017
user4                     46.47.84.49           8.06 GB     806.24 MB  Mon Feb 13 00:49:54 2017
------- Current --------
Common Name               Real Address         Download        Upload           Connected Since
hjelev                    85.118.92.81          1.61 MB      10.30 MB  Wed Jan 25 15:23:01 2017
user4                     46.47.84.49         221.06 MB     806.24 MB  Mon Feb 13 00:49:54 2017
```
