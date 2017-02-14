# OpenVPN-Stats

Python script to display statistics for open vpn





How to run the script with a cron

#this will start the webserver displaing the statistics
@reboot /usr/bin/python /home/pi/scripts/ovpnstats/openvpn_display_html.py

#this will fetch and agregate stats each minute
*/1 * * * * sudo /usr/bin/python /home/pi/scripts/ovpnstats/openvpn_stats.py /dev/null 2>&1
