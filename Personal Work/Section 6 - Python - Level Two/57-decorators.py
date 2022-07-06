def hello(name='Jose'):
    print('The hello () func has been run')
    def greet():
        return "This is inside the greet()"
    def welcome():
        return "This is inside welcome()"
    print(greet())
    print(welcome())

hello()
