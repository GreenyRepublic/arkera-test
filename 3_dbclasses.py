from unittest import TestCase
import operator
import datetime
import enum

def notcontains(a, b):
    return (b not in a) 

class predTypes(enum.Enum):
    EQUALS = 0
    LESSTHAN = 1
    GREATERTHAN = 2
    IN = 3
    NOTIN = 4

class Query():
    entryIndex = 0
    predicates = {predTypes.EQUALS: operator.eq,
                  predTypes.LESSTHAN: operator.gt,
                  predTypes.GREATERTHAN: operator.lt,
                  predTypes.IN: operator.contains,
                  predTypes.NOTIN: notcontains}

    def evaluate(self, partition):
        returnTab = []
        for entry in partition:
            if self.predicate(entry):
                returnTab.append(entry)
        return returnTab
    
    def predicate(self, entry, data, pred):
        return pred(data, entry[self.entryIndex])
        

class idQuery(Query):
    
    entryIndex = 0
    def __init__(self, ids, pred):
        self.ids = ids
        self.pred = pred

    def predicate(self, entry):
        return super().predicate(entry, self.ids, self.predicates[self.pred])
        

class urlQuery(Query):
    entryIndex = 1    
    def __init__(self, url):
        self.url = url
        self.pred = "EQUALS"
        
    def predicate(self, entry):
        return super().predicate(entry, self.url, self.predicates[self.pred])

class dateQuery(Query):
    entryIndex = 2
    def __init__(self, date, pred = "EQUALS"):
        self.date = date
        self.pred = pred
        
    def predicate(self, entry):
        return super().predicate(entry, self.date, self.predicates[self.pred])
    
class ratingQuery(Query):
    entryIndex = 3
    def __init__(self, rating, pred = "EQUALS"):
        self.rating = rating
        self.pred = pred
        
    def predicate(self, entry):
        return super().predicate(entry, self.rating, self.predicates[self.pred])



testTable = [(0, "google.com", datetime.datetime(1995, 6, 3), 99),
             (1, "deandepot.com", datetime.datetime(2012,12,10), 24),
             (2, "arkera.ai", datetime.datetime(1993, 7, 2), 43),
             (3, "foobar.net", datetime.datetime(2001, 12, 25), 89)]

testQuery1 = [idQuery(2, "GREATERTHAN")]
testQuery2 = [idQuery(4, "LESSTHAN"), ratingQuery(50, "GREATERTHAN")]

def runQueries(table, queries):
    partition = table
    for query in queries:
        partition = query.evaluate(partition)
    return partition
