import re


def read_data(file: str):
    data = ""
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    return data


def part_one():
    patern = r"mul\((\d+),(\d+)\)"
    data = read_data("input.txt")

    grup = re.findall(patern, data)

    print(sum([int(a) * int(b) for a, b in grup]))


def main():
    part_one()


if __name__ == "__main__":
    main()
