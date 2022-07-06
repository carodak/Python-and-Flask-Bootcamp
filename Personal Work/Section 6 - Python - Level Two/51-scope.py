x = 'outside'

def report():
    # Hey grab the global level x variable!
    #global x
    # reassign global x
    x = 'inside'
    return x

print(report())
print(x)

# LEGB RULE: Python will seach in this order: local > enclosing > global > built in

# LOCAL
def report():
    x = 'local'
    print(x)

# ENCLOSING

x = 'THIS IS GLOBAL LEVEL'

def enclosing():
    # an x at this enclosing level
    x = 'Enclosing Level'

    def inside():
        # no x at this local level
        # x = 'local'
        print(x)
    inside()

enclosing()

# built in = length, sum..
