def groupThePeople(groupSizes):

    i = 0
    result = []
    my_dict = {}
    for num in groupSizes:
        if num in my_dict:
            my_dict[num].append(i)
        else:
            my_dict[num] = [i]
        i += 1

        if num == len(my_dict[num]):
            result.append(my_dict[num])
            my_dict[num] = []

    return result




