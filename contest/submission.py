"""

"""


def main():
    pass


if __name__ == "__main__":
    main()


# --- Helpers
import sys

def debug(*values, **kwargs):
    def is_arr(x):
        return type(x) in [list, tuple]

    def is_2d(x):
        return is_arr(x) and any(is_arr(y) for y in x)

    if len(values) == 1 and is_2d(values[0]):
        for row in values[0]:
            debug(row)
        debug(**kwargs)
        return

    print(*values, file=sys.stderr, **kwargs)

def ii(): return int(input())
def ia(): return list(map(int, input().split()))
# ---
