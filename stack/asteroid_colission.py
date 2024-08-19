"""
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5.
The 10 and -5 collide resulting in 10.
"""

def get_asteroid_colission(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < abs(asteroid):
                stack.pop()
                continue
            if stack[-1] == abs(asteroid):
                stack.pop()
            break
        else:
            stack.append(asteroid)

    return stack


print(get_asteroid_colission([5,10,-5]))