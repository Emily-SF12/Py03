import sys

def str_to_int(item: str) -> int:
    return int(item)


def build_inventory(mess: str) -> dict[str, int]:
    spacing: list[str] = mess.split(" ")
    name: str = ""
    qtd: int = 0
    for item in spacing[1:]:
        spliting: list[str] = []
        spliting = item.split(":")
        if len(spliting) != 2:
            print(f"Error - invalid parameter {spliting}")
        else:
            try:
                qtd = str_to_int(spliting[1])
                name = (spliting[0])
                return name, qtd
            except ValueError as v_e:
                print(f"Quantity error for 'key': {v_e}")


def main(mess: str) -> None:

    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")
