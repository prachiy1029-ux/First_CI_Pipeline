"""Program 27: Rotate a list by k positions."""


def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]