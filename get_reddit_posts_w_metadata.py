import datetime
from datetime import datetime, timezone
import time
import os

import praw
import psaw
from psaw import PushshiftAPI
import pandas as pd

"""
NOTE
Things to look for later
* post was removed if selftext == '[removed']
"""

client_id = "ql-_f6PWk3jphw"
client_secret = "YzVC4mhatCWK-tRMTnzkA0VB4ng"
reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id=client_id,
    client_secret=client_secret,
)

reddit_name = 'infertility'
data_dir = './data/reddit/' + reddit_name + '/praw/posts'
api = PushshiftAPI(reddit)

begin = datetime(2015, 1, 1)
begin = begin.replace(tzinfo=timezone.utc).timestamp()
end = datetime(2020, 9, 15).replace(tzinfo=timezone.utc).timestamp()

start = begin
i = 0
time_interval = (end-begin)/100
interval_dfs = []
while start < end + 1:
    results = list(api.search_submissions(after=int(start),
                                          before=int(start+time_interval),
                                          subreddit=reddit_name))
    result_df = pd.DataFrame([r.__dict__ for r in results])
    # save result_df to file
    result_df.to_csv(os.path.join(data_dir, "{}.csv".format(i)))
    interval_dfs.append(result_df)

    start += time_interval
    i += 1
    print(i)

# save aggregate results
final_df = pd.concat(interval_dfs)
final_df.to_csv(os.path.join(data_dir, "all.csv"))
