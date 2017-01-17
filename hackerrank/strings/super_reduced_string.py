import re


def super_reduced_string(input_string):
    regex = re.compile(r'(\w)(\1)')
    match = regex.search(input_string)
    
    while match:
        input_string = input_string.replace(match.group(), '')
        match = regex.search(input_string)
        
    return input_string if input_string else 'Empty String'


print super_reduced_string(raw_input())
