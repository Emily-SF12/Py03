import sys


def show_data(args: list[str]) -> None:
    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {len(args) - 1}")
        for i, arg in enumerate(args[1:], start=1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(args)}")


def main(args: list[str]) -> None:
    args = sys.argv
    print("=== Command Quest ===")
    show_data(args)


if __name__ == "__main__":
    main(sys.argv)
