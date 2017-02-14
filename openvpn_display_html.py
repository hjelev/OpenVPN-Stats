#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys,subprocess,web, pickle,glob

web.config.debug = False
urls = ('/', 'vpn')
app = web.application(urls, globals(),autoreload=True)

STATUS = "/var/log/openvpn-status.log"
fmt = "%(cn)-25s %(real)-15s %(sent)13s %(recv)13s %(since)25s"

db_folder = "db"

sizes = [  
    (1<<50L, 'PB'),
    (1<<40L, 'TB'),
    (1<<30L, 'GB'),
    (1<<20L, 'MB'),
    (1<<10L, 'KB'),
    (1,       'B')
]

headers = {  
	'cn':    'Common Name', 
	'real':  'Real Address', 
	'sent':  'Download', 
	'recv':  'Upload', 
	'since': 'Connected Since'
}
	
	
headers_total = {  
	'cn':    'Common Name', 
	'real':  'Real Address', 
	'sent':  'Download', 
	'recv':  'Upload', 
	'since': 'Last Online'
}


def byte2str(size):  
    for f, suf in sizes:
        if size >= f:
            break

    return "%.2f %s" % (size / float(f), suf)

def getScriptPath(): #gets script directory
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def print_current():
	status_file = open(STATUS, 'r')  
	stats = status_file.readlines()  
	status_file.close()
		
	hosts = []

	for line in stats:  
		cols = line.split(',')

		if len(cols) == 5 and not line.startswith('Common Name'):
			host  = {}
			host['cn']    = cols[0]
			host['real']  = cols[1].split(':')[0]
			host['recv']  = byte2str(int(cols[2]))
			host['sent']  = byte2str(int(cols[3]))
			host['since'] = cols[4].strip()
			hosts.append(host)

	return fmt % headers + "<br/>" + "<br/>".join([fmt % h for h in hosts])  
	
def print_total():
	log_files = glob.glob(os.path.join(getScriptPath(), db_folder) + "/*.log")
	stats = []

	for lf in log_files:
		
		old_host = pickle.load(open( lf, "rb" )) #read data from file
		old_host[0]['recv'] += old_host[1]['recv']
		old_host[0]['sent'] += old_host[1]['sent']
		old_host[0]['recv']  = byte2str(old_host[0]['recv'])
		old_host[0]['sent']  = byte2str(old_host[0]['sent'])
		stats.append(old_host[0])
	
	return (fmt % headers_total + "<br/>" + "<br/>".join([fmt % s for s in stats])).replace(" ", "&nbsp;")

class vpn:
	def GET(self):
		stats = print_total().replace (" ", "&nbsp;")
		cur_stats = print_current().replace (" ", "&nbsp;")
		return "<BODY BGCOLOR='e5e5e5'> <div style='font-family:Courier,monospace;'> ------- Total --------<br/>" + stats +"<br/>------- Current --------<br/>"+ cur_stats+"</div></body>"
				
if __name__ == '__main__':
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8075))