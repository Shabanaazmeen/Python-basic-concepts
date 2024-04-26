n = int(input('enter the events'))
events = list(map(int, input().split()))
#def count_unsolved_crimes(events):
untreated_crimes = 0
available_officers = 0
for event in events:
    if event == -1:
        if available_officers == 0: 
            untreated_crimes += 1
        else:
            available_officers -= 1
else:  # Officers recruited
    available_officers += event
print(untreated_crimes(events))
    #return untreated_crimes

# Input reading and function call
#n = int(input('enter the events'))
#events = list(map(int, input().split()))
print(count_unsolved_crimes(events))

def count_unsolved_crimes(events):
    return untreated_crimes
