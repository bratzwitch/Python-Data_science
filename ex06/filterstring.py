import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3
        S = sys.argv[1]
        N = int(sys.argv[2])
        if not all(c.isalpha() or c.isspace() for c in S):
            raise AssertionError
        words = S.split()
        r = list(ft_filter(lambda w: len(w) > N, [word for word in words]))
        result = r
        print(result)
    except (AssertionError, ValueError):
        print("AssertionError")


if __name__ == "__main__":
    main()
