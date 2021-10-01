import sys
from objsize import get_deep_size


def getSizeOf(obj, size="b"):
    '''
    getSizeOf(obj) -> Returns a float equal to the size of an object in bytes.\n
    getSizeOf(obj, "MB") -> Returns a float equal to the size of an object in megabytes.\n
    See the sizes list for a list of available sizes.

    Sizes:\n
        "b"  -> Bytes,\n
        "kb" -> Kilobytes,\n
        "mb" -> Megabytes,\n
        "gb" -> Gigabytes,\n
        "tb" -> Terabytes
    '''
    sizes = {
        "b":  1,
        "kb": 1024,
        "mb": 1048576,
        "gb": 1073741824,
        "tb": 1099511627776,
    }

    obj_size = 0
    return get_deep_size(obj) / sizes[size]

def isTooLarge(obj, limit=2, size="mb"):
    if getSizeOf(obj, size)>limit:
        return True
    return False