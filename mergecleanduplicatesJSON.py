
#Merge the tweets from streaming API and REST API

#load the library
import json
from datetime import datetime

#Open both .json files
with open('fortnite_event_live.json') as fileStream:
    streamData = fileStream.read()
    
with open('fortnite_event_historic.json') as fileSearch:
    searchData = fileSearch.read()

#combine both json data
combinedData = (streamData + searchData)

#write to new .json file
with open('fortnite_event_combined.json', 'w') as fileCombined:
    fileCombined.write(combinedData)


#Deduplicate the tweets

#reopen the new combined file, remove duplicates using "id" key/value
with open('fortnite_event_combined.json', 'r') as fileCombined:
    tweetsDuplicates = map(json.loads, fileCombined)
    uniques = {} #initialize dict
    for x in tweetsDuplicates:
        tweetID = x['id']
        if tweetID not in uniques:
            uniques[tweetID] = x
    
#write to new file using the unique values    
with open('fortnite_event_uniques.json', 'w') as fileUnique:
    for k in uniques.values():
        fileUnique.write(json.dumps(k))
        fileUnique.write('\n')


#reopen the new file with unique tweets, sort by timestamp
with open('fortnite_event_uniques.json', 'r') as fileUnique:
    tweetsUniques = map(json.loads, fileUnique)
    tweetsSorted = sorted(tweetsUniques, key=lambda l: datetime.strptime(l['created_at'],'%a %b %d %X %z %Y'))

#write to new file using the sorted unique values    
with open('fortnite_event_sorted.json', 'w') as fileSorted:
    for m in tweetsSorted:
        fileSorted.write(json.dumps(m))
        fileSorted.write('\n')    
