def report_person(name='Unknown Name'):
    print("reporting {}!".format(name))

report_person("Cindy")
report_person()

def add_num(num1,num2):
    res = num1+num2
    return res

result = add_num(2,4)
print(result+10)
