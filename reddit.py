import praw
import pdb
import requests
import json
import csv
import time
import datetime
from datetime import datetime, timezone

client_id = "ql-_f6PWk3jphw"
client_secret = "YzVC4mhatCWK-tRMTnzkA0VB4ng"
reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id=client_id,
    client_secret=client_secret,
)

gg = reddit.subreddit('infertility')


begin = datetime(2015, 1, 1)
begin = begin.replace(tzinfo=timezone.utc).timestamp()
end = datetime(2020, 9, 15).replace(tzinfo=timezone.utc).timestamp()

reddit_name = 'secondaryfertility'
data_dir = './data/reddit/' + reddit_name 
base_url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + reddit_name + "&size=1000"
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

