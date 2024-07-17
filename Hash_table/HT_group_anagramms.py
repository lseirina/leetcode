
# For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"],
# the function should return [["eat","tea","ate"],["tan","nat"],["bat"]]
# because the first three strings are anagrams of each other,
# the next two strings are anagrams of each other, and the last string has no anagrams in the input arra


def group_anagrams(words):
    my_dict = {}
    for word in words:
        s_word = ''.join(sorted(word))
        if s_word in my_dict:
            my_dict[s_word].append(word)
        else:
            my_dict[s_word] = [word]

    return list(my_dict.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



















# def find_anagrams(words: list[str]) -> list[str]:
#     """Collect all anagrams in groups."""
#     my_dict = {}
#     for word in words:
#         s_word = ''.join(sorted(word))
#         if s_word in my_dict:
#             my_dict[s_word].append(word)
#         else:
#             my_dict[s_word] = [word]

#     return list(my_dict.values())

# print(find_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))























# def group_anagrams(words):

#     anagram_groups = {}
#     for word in words:
#         sorted_word = "".join(sorted(word))
#         if sorted_word in anagram_groups:
#             anagram_groups[sorted_word].append(word)
#         else:
#             anagram_groups[sorted_word] = [word]

#     return list(anagram_groups.values())


# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
