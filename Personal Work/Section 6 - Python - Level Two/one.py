#one

def func():
    print("func() is one.py")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__': #if we ran this script directly (not imported)
    print('one.py is being run directly!')
    # usually people would call their function here
else:
    print('one.py has been imported!')
