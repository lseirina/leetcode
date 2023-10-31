"""
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1
"""

def defand_ip_adress(chars):

    return chars.replace(".", "[.]")

print(defand_ip_adress("1.1.1.1"))
