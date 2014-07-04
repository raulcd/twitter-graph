#!/usr/bin/env python
import tweepy
from py2neo import neo4j

SECRETS_FILE = 'secrets.txt'
NEO4J_DB = 'http://localhost:7474/db/data/'


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
    return tweepy.Cursor(api.followers, id=user)


def get_followed(api, user):
    """
    Get the followed users from a user
    """
    return tweepy.Cursor(api.friends, id=user)


def get_twitter_connections(user):
    api = get_twitter_api(*read_secrets())
    friends = get_followed(api, user)
    followers = get_followers(api, user)
    return {'user': user, 'friends': friends, 'followers': followers}


def start_database():
    return neo4j.GraphDatabaseService(NEO4J_DB)


def update_nodes(graph_db, user_connections):
    people = graph_db.get_or_create_index(neo4j.Node, 'people')
    user_node = people.get_or_create('name', user_connections['user'],
                                     {'name':  user_connections['user']})
    count = 0
    for friend in user_connections['friends'].items():
        friend_node = people.get_or_create('name', friend.screen_name,
                                           {'name': friend.screen_name,
                                            'location': friend.location,
                                            'timezone': friend.timezone})
        user_node.create_path("FOLLOWS", friend_node)
        if count == 0:
            count += 1
            dict_attributes = vars(friend)
            for k, v in dict_attributes.iteritems():
                print "Key: %s, Value: %s" % (k, v)
    for follower in user_connections['followers'].items():
        follower_node = people.get_or_create('name', follower.screen_name,
                                             {'name': follower.screen_name,
                                              'location': follower.location,
                                              'timezone': follower.timezone})
        follower_node.create_path("FOLLOWS", user_node)


if __name__ == '__main__':
    graph_db = start_database()
    user = raw_input("What's the username you want to check?")
    user_connections = get_twitter_connections(user)
    update_nodes(graph_db, user_connections)
