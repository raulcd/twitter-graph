#!/usr/bin/env python

def get_followers(user):
    """
    docstring for get_twitter_followers
    Get twitter followers from a user and returns the list of followers
    
    """
    pass

def get_followed(user):
    """
    Get the followed users from a user
    """
    info = get_twitter_info(user)
    return info

def get_twitter_info(user):
    """
    Get the twitter info for a given user
    """
    #TODO Request to twitter to get info
    pass

if __name__ == '__main__':
    user = raw_input("What's the username you want to check?")
    print get_followed(user)
