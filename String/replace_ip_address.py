def defangIPaddr(address):
    address = address.replace('.', '[.]')

    return address


print(defangIPaddr('fghj.fghj'))
