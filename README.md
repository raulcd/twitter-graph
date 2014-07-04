twitter-graph
=============

Some tests with twitter API and neo4j

Usage
=====
Create a secrets.txt file in the same directory with two lines:
* First Line: Your twitter API key
* Second Lone: Your twitter API secret

Example of secrets.txt:
'''
wmla023MKDF234vc34
234kj45hui4353GEWRT345fewger435geEETRET
'''

Dependencies
============
Install requirements.txt with pip

'''
pip install -r requirements.txt
'''

Neo4j should be installed and running with default settings (port 7474)

Run
===
Execute:
'''
python twitter_graph.py
'''

It will ask for the user you want to load the graph of friends and followers.
