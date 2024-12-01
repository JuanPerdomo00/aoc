from typing import List, Tuple


def read_input(path: str) -> Tuple[List[int]]:
    left_list = []
    right_list = []

    with open(path, "r") as f:
        for line in f:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


def distance(a: int, b: int) -> int:
    return abs(b - a)


def main():
    # print(read_input("./input.txt"))
    left, right = read_input("./input.txt")

    left.sort()
    right.sort()

    distance_n_L_R: int = sum(
        distance(left_n, right_n) for left_n, right_n in zip(left, right)
    )

    print(f"{distance_n_L_R}")


if __name__ == "__main__":
    main()
