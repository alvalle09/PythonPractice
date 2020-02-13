import json

#  use 'r' for reading file
with open('input.json', 'r') as input:
    obj = json.load(input)
    print('Hello, ' + obj['name'])
    # use 'w' for write method
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies: \n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")


