'''
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
'''

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTuples(myDict):
    return myDict.items()

print makeTuples(my_dict)

# The first method was an easy built-in method for returning a list of tuples, this is a more explicit method
def makeTuplesHard(myDict):
    returnList = []
    for key, data in myDict.iteritems():
        returnList.append((key, data))
    
    return returnList

print makeTuplesHard(my_dict)