import sys


def greet(name: str, shout_count: int = 1):
    return f"Hello, {name}{shout_count * '!'}"


if __name__ == "__main__":

    n = int(sys.argv[2]) if len(sys.argv) == 3 else 1
    print(greet(sys.argv[1], n))
