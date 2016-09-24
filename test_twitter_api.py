import re

import twitter

PATTERN = '(([\ud83c][\udde6-\uddff]){1}([\ud83c][\udde6-\uddff]){1}){1}'
PATTERN = '[\U0001f1e6-\U0001f1ff]{2}'
from myservices.local_settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN_KEY

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)
# print api.GetUserTimeline(screen_name='msilva', exclude_replies=True, include_rts=False)  # includes
# entities
print(api.VerifyCredentials())
# print(api.GetUserTimeline(screen_name='materialpodcast'))
list = api.GetSearch(raw_query='q=to%3Amaterialpodcast', result_type='recent', include_entities=True)
for tweet in list:
    print tweet
    # print tweet.user
    print tweet.user.location
print 'test USA'
test_usa = api.GetStatus(status_id=756848529298100224)
print test_usa
print test_usa.user.location
print test_usa.text
for c in test_usa.text:
    print c
print re.match(PATTERN, test_usa.text)

print 'test PT'
test_pt = api.GetStatus(status_id=756907864493584385)
print test_pt
print test_pt.user.location
print test_pt.text
for c in test_pt.text:
    print c
print 'match'
print re.match(PATTERN, test_pt.text)
print 'findall'
print re.findall(PATTERN, test_pt.text)
print 'findalldecoded'

print 'test AZ'
test_az = api.GetStatus(status_id=756908460952920064)
print test_az
print test_az.user.location
print test_az.text
for c in test_az.text:
    print c
print re.match(PATTERN, test_az.text)


# assert tweet has code
# assert only one
# get country from tweet
# update db
