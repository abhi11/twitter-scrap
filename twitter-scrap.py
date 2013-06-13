#!/bin/env python
import twitter
from operator import attrgetter
     

api=twitter.Api(consumer_key='tI0bUJuctVgzA82wGYLiQ',
                consumer_secret='59GVWA6j7RJt1Ntw2cFi57FS91jzRFIk6lbNzH8Cs8', 
                access_token_key='165807027-Y9GeHly2EiJ5LBzcI3eAGvNp9M44kpO5tK9yfu2n', 
                access_token_secret='qTopfcbhvo1qo3RvWvqzxDg2IHeJETyz8x5SPn8n0zk')


user=api.GetUser(screen_name=str(raw_input("Enter screen name: ")))
print "-------------User Information-----------\n"
print "Name: "+user.name
print "Id: "+str(user.id)
print "Location: "+user.location
print "Status: "+user.status.text
print "Total Status count: "+ str(user.statuses_count)
print "Followers: "+str(user.followers_count)
print "Following: "+str(user.friends_count)

print "\nPrinting all the tweets of %s in order of popularity(i.e retweets)\n" %user.name

##Print all user statuses and no of retweets   
statuses=api.GetUserTimeline(user.id)
i=0
while(i < len(statuses)):
    j=0
    while(j < len(statuses)-i-1):
        if(statuses[j].retweet_count < statuses[j+1].retweet_count):
            temp=statuses[j]
            statuses[j]=statuses[j+1]
            statuses[j+1]=temp
        j=j+1

    i=i+1

for status in statuses: 
    s=status.text
    print "**************************************************************\n"
    print "Tweet: "+s.encode('utf-8')
    print "Retweet Count: "+str(status.retweet_count)
    print "**************************************************************\n\n"
 
