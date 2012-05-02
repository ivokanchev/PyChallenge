def look_and_say(member):
    while True:
        yield member
        breakpoints = ([0] + [i for i in range(1, len(member)) 
                              if member[i - 1] != member[i]]
                        + [len(member)])
        groups = [member[breakpoints[i - 1]:breakpoints[i]]
                  for i in range(1, len(breakpoints))]
        member = ''.join(str(len(group)) + group[0] for group in groups)
 
# Print the 10-element sequence beginning with "1"
sequence = look_and_say("1")
for i in range(10):
    print sequence.next()
