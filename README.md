# Data collection through twitter API (Streaming API & REST API)

This repository contains the scripts to collect the streaming tweets and retrieve the historic tweets from twitter API. Because the Twitter Developer account used here is for academic purpose only, there are thresholds of streaming the tweets. In order to get the most for a particular event, we used both streaming API and REST API to get the tweets related to certain hashtags in a specified period. Apart from data collection, this repository also covers the step to remove the duplicate tweets through tweet id. 

## Installation


* Install the Tweepy  
  * Mac users open a new terminal window and type it there. 
  * Windows users open Anaconda prompt and type in the command below.

```
pip install tweepy
```
*  Load the neccessary packages
```
import tweepy
import json
from datetime import datetime
```

## Further Resource

* Twitter API Developer Platform - [Apply the access](https://developer.twitter.com/en/apply-for-access)
* [Tweepy Documentation](https://docs.tweepy.org/en/latest/index.html)
