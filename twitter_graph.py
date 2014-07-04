#!/usr/bin/env python
import tweepy

SECRETS_FILE = 'secrets.txt'


def read_secrets():
    twitter_key, twitter_secret = open(SECRETS_FILE).readlines()
    return twitter_key[:-1], twitter_secret[:-1]


def get_twitter_api(key, secret):
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth)
    return api


def get_followers(api, user):
    """
    docstring for get_twitter_followers
    Get twitter followers from a user and returns the list of followers
    """
    return api.followers(id=user)
    pass


def get_followed(api, user):
    """
    Get the followed users from a user
    """
    return api.friends(id=user)


if __name__ == '__main__':
    user = raw_input("What's the username you want to check?")
    api = get_twitter_api(*read_secrets())
    friends = get_followed(api, user)
    print "Follows"
    for friend in friends:
        print friend.name
    print "Followers"
    followers = get_followers(api, user)
    for follower in followers:
        print follower.name
