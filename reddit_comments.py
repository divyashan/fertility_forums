import pdb
import requests
import json
import csv
import time
import datetime
from datetime import datetime, timezone


begin = datetime(2015, 1, 1)
begin = begin.replace(tzinfo=timezone.utc).timestamp()
end = datetime(2020, 9, 15).replace(tzinfo=timezone.utc).timestamp()

reddit_name = 'ttcafterloss'
data_dir = './data/reddit/' + reddit_name + '/comments' 
base_url = "https://api.pushshift.io/reddit/search/comment/?subreddit=" + reddit_name + "&size=1000"
# Put together timestamps for the last 5 years, in half year chunks

start = begin
i = 0
time_interval = (end-begin)/100
while start < end+1:
	time.sleep(1)
	url = base_url + "&after=" + str(int(start)) + "&before=" + str(int(start+time_interval))
	resp = requests.get(url)
	
	try:	
		dicts = json.loads(resp.content)
	except:
		pdb.set_trace()
	with open(data_dir + "/" + str(i) + ".data", "w") as outfile:
		outfile.write(json.dumps(dicts))
	
	start += time_interval
	i += 1
	print(i)

