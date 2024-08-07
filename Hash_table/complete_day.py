"""
Input: hours = [12,12,30,24,24]

Output: 2

Explanation:

The pairs of indices that form a complete day are (0, 1) and (3, 4).
[72,48,24,3]

"""

def count_complete_day_pairs(hours):
    count = 0
    for i in range(len(hours)):
        for j in range(i+1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                count += 1

    return count


print(count_complete_day_pairs([72,48,24,3]))
