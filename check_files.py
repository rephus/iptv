import requests
import sys 

file_name = sys.argv[1]
print ("reading {}".format(file_name) )
with open(file_name, 'r') as f:
   read_data = f.read()
   
   channel_header = ""
   for line in read_data.split("\n"):
        try: 
            if not 'http' in line: 
                channel_header = line
            if 'http' in line: 
                r = requests.get(line, timeout=1)
                if r.status_code < 400:
                        print("working channel ({}) {} {} ".format(r.status_code, channel_header, line))
                #else: 
                        #print("404 channel {} {} ".format(channel_header, line))
        except Exception as e: 
            pass
            #print("Unable to get channel {} {}: {}".format(channel_header, line, e))
