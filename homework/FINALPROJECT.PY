#recipe project
#3 recipes
#cooking 

class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(First, Second):
    def __init__(self):
        print "third"
