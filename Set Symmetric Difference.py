def symdiff(s1, s2):
    return s1.symmetric_difference(s2) 


Set1 = {'blue', 'green'}
Set2 = {'blue', 'yellow'}

Set3 = {1, 2, 3, 4, 5}
Set4 = {1, 5, 6, 7, 8, 9}

diffs = symdiff (Set1, Set2)

diffs2 = symdiff (Set3, Set4)

print(diffs, diffs2)