def next_number(member):
    while True:
        yield member
        breakpoints = ([0] + [i for i in range(1, len(member)) 
                              if member[i - 1] != member[i]]
                        + [len(member)])
        groups = [member[breakpoints[i - 1]:breakpoints[i]]
                  for i in range(1, len(breakpoints))]
        member = ''.join(str(len(group)) + group[0] for group in groups)
sequence = next_number("1")
for i in range(31):
    print(len(sequence.__next__()))
