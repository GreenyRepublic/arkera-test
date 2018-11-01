from unittest import TestCase
import operator
import math

class Query():
    field = 0
    def predicate(self, entry):
        return True

    def evaluate(self, table):
        returnTab = [()]
        for entry in table:
            if predicate(entry):
                returnTab.append(entry)
        return returnTab

#class idQuery(Query):
    #def __init__(self, predicate, list = []):
        

class urlQuery(Query):
    def __init__(self, url):
        self.url = url
    def predicate(self, entry):
        return (self.url == entry.url)
    

#class dateQuery(Query):

#class ratingQuery(Query):

class Database():
    def __init__(self):
        self.table = [()]

    def runQueries(self, queries):
        partition = self.table
        for query in queries:
            partition = query.evaluate(partition)
        return partition
