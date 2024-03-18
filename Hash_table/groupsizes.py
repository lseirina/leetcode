"""
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
"""
def  group_people(groupsizes):
    i = 0
    my_dict = {}
    res = []

    for num in groupsizes:
        if num in my_dict:
            my_dict[num].append(i)
        else:
            my_dict[num] = [i]
        i += 1
        if len(my_dict[num]) == num:
            res.append(my_dict[num])
            my_dict[num] = []

    return res





print(group_people([3,3,3,3,3,1,3]))