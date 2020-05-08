import sys
from twitter_scraper import Profile, get_tweets
from twitter_functions import process_tweets

try:
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    profile_name=args[0]
    tweets={}

    if "--profilename" or "-p" in opts:
        profile = Profile(profile_name)
        profile.to_dict()
        
        for tweet in get_tweets(profile_name, pages=1):
            if tweet['entries']['photos']:
                sep = ' pic'
                tweet_text = tweet['text'].split(sep, 1)[0]
                tweets.update([(tweet_text,tweet['entries']['photos'][0])])
        process_tweets(tweets)
except:
        raise SystemExit(f"Usage: {sys.argv[0]} -p twitter_handle")
