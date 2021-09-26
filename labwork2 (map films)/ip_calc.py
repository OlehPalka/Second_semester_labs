"""
This module containes functions which mfke operations with ip addresses
"""


def get_ip_from_raw_address(raw_address):
    """
    This function returns an ip adress

    >>> get_ip_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    return raw_address[:-3]


def get_binary_mask_from_raw_address(raw_address):
    """
    this function returns Binary Subnet Mask

    >>> get_binary_mask_from_raw_address('91.124.230.205/30')
    '11111111.11111111.11111111.11111100'
    """
    result = "00000000.00000000.00000000.00000000"
    mask = int(raw_address.split("/")[1])
    if mask < 8:
        pass
    elif mask < 17:
        mask += 1
    elif mask < 25:
        mask += 2
    else:
        mask += 3
    return result[:mask].replace("0", "1") + result[mask:]


def get_network_address_from_raw_address(raw_address):
    """
    This function returns Network Address

    >>> get_network_address_from_raw_address("91.124.230.205/30")
    '91.124.230.204'
    """
    bin_adress = [str(bin(int(i)))
                  for i in raw_address[:-3].split('.')]
    for i in range(4):
        bin_adress[i] = bin_adress[i][2:]
        if len(bin_adress) != 8:
            addable_part = ""
            for _ in range(8 - len(bin_adress[i])):
                addable_part += "0"
            bin_adress[i] = addable_part + bin_adress[i]
    bin_mask = get_binary_mask_from_raw_address(raw_address).split(".")

    result = ["".join([str(int(bin_adress[i][a])
                           & int(bin_mask[i][a])) for a in range(8)]) for i in range(4)]
    for i in range(4):
        result[i] = str(int(result[i], 2))
    return ".".join(result)


def get_broadcast_address_from_raw_address(raw_address):
    """
    This function returns Broadcast Address

    >>> get_broadcast_address_from_raw_address("91.124.230.205/30")
    '91.124.230.207'
    """
    inv_mask = "00000000.00000000.00000000.00000000"
    mask = int(raw_address.split("/")[1])
    if mask < 8:
        pass
    elif mask < 17:
        mask += 1
    elif mask < 25:
        mask += 2
    else:
        mask += 3
    inv_mask = inv_mask[:mask] + inv_mask[mask:].replace("0", "1")
    inv_mask = inv_mask.split(".")
    bin_adress = [str(bin(int(i)))[2:]
                  for i in raw_address[:-3].split('.')]
    for i in range(4):
        if len(bin_adress) != 8:
            addable_part = ""
            for _ in range(8 - len(bin_adress[i])):
                addable_part += "0"
            bin_adress[i] = addable_part + bin_adress[i]
    result = ["".join([str(int(bin_adress[i][a])
                           | int(inv_mask[i][a])) for a in range(8)]) for i in range(4)]
    for i in range(4):
        result[i] = str(int(result[i], 2))
    return ".".join(result)


def get_first_usable_ip_address_from_raw_address(raw_address):
    """
    This function returns First usable host

    >>> get_first_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    net_ad = get_network_address_from_raw_address(raw_address).split(".")
    net_ad[-1] = str(int(net_ad[-1]) + 1)
    return ".".join(net_ad)


def get_penultimate_usable_ip_address_from_raw_address(raw_address):
    """
    This function returns Penultimate usable host IP

    >>> get_penultimate_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    penul = get_broadcast_address_from_raw_address(raw_address).split(".")
    penul[-1] = str(int(penul[-1]) - 2)
    return ".".join(penul)


def get_number_of_usable_hosts_from_raw_address(raw_address):
    """
    This function returns Number of usable Hosts

    >>> get_number_of_usable_hosts_from_raw_address("91.124.230.205/30")
    2
    """
    return (2 ** (32 - int(raw_address.split("/")[1]))) - 2


def get_ip_class_from_raw_address(raw_address):
    """
    This function finds to which class adress belongs

    >>> get_ip_class_from_raw_address("91.124.230.205/30")
    'A'
    """
    class_ip = int(raw_address.split(".")[0])
    if class_ip < 126:
        result = "A"
    elif class_ip < 191:
        result = "B"
    elif class_ip < 223:
        result = "C"
    elif class_ip < 239:
        result = "D"
    elif class_ip < 247:
        result = "E"
    return result


def check_private_ip_address_from_raw_address(raw_address):
    """
    This function checks if the address is private.

    >>> check_private_ip_address_from_raw_address("91.124.230.205/30")
    False
    """
    if raw_address.startswith("10.") or \
            raw_address.startswith("172.16.") or\
            raw_address.startswith("172.31.") or\
            raw_address.startswith("192.168."):
        return True
    return False


if __name__ == '__main__':
    numsandsign = "1234567890/."
    address = input()
    for element in address:
        if element not in numsandsign:
            print("Error")
            exit()
    if "/" not in address:
        print("Missing prefix")
        exit()
    if address.count(".") != 3:
        print(None)
        exit()
    print(get_ip_from_raw_address(address))
    print(get_binary_mask_from_raw_address(address))
    print(get_network_address_from_raw_address(address))
    print(get_broadcast_address_from_raw_address(address))
    print(get_first_usable_ip_address_from_raw_address(address))
    print(get_penultimate_usable_ip_address_from_raw_address(address))
    print(get_number_of_usable_hosts_from_raw_address(address))
    print(get_ip_class_from_raw_address(address))
    print(check_private_ip_address_from_raw_address(address))
