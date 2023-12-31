def max_length(s):
    my_dict = {}
    a = -1
    for i in range(len(s)):
        if s[i] in my_dict:
            a = max(a, ( i - my_dict[s[i]] - 1))
        else:
            my_dict[s[i]] = i

    return a


print(max_length("mgntdygtxrvxjnwksqhxuxtrv"))