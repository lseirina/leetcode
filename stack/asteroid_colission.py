"""
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5.
The 10 and -5 collide resulting in 10.
"""
def get_asteroid_colission(asteroids):
    res = []
    for astr in asteroids:
        if res and astr * res[-1] < 0 and abs(astr) > res[-1]:
            res.pop()
            res.append(astr)
        if res and abs(astr) < res[-1]:
            pass
        if res and astr * res[-1] < 0 and abs(astr) == abs(res[-1]):
            res.pop()
        else:
            res.append(astr)

    return res


print(get_asteroid_colission([5,10,-5]))