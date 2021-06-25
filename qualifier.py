from typing import Any, List, Optional


def pad_item(item: str, max_len: int, centered: bool) -> str:
    """
    helper function to pad the item to the maximum size
    """
    left_pad: str = ' ' * int((max_len-len(item))/2) if centered else ' '
    right_pad: str = ' ' * int(max_len - len(left_pad + item))
    res = left_pad + item + right_pad
    return res


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    # store sresulting table as a string
    res_table: str = ""
    # map standard strings to the provided border characters
    border = {
        "tl": '┌', "tm": '┬',
        "tr": '┐', "bl": '└',
        "bm": '┴', "br": '┘',
        "l": '├', "m": '┼',
        "r": '┤', "h": '─',
        "v": '│',
    }

    # generate maximum item size (padded) for all columns in a row
    max_col_len: dict[int, int] = {}
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            max_col_len[j] = len(str(col))+2 if i == 0 else max(
                max_col_len[j], len(str(col))+2)

    # consider label size of maximum item size
    if labels:
        for i, col in enumerate(labels):
            max_col_len[j] = max(max_col_len[j], len(str(col))+2)

    # generate top border of the table
    for i, val in max_col_len.items():
        if i == 0:
            res_table += border["tl"]
        else:
            res_table += border["tm"]
        res_table += border["h"] * val
    res_table += border["tr"]
    res_table += '\n'

    if labels:
        # generate the labels row
        for i, col in enumerate(labels):
            res_table += border["v"]
            res_table += pad_item(str(col), max_col_len[i], centered)
        res_table += border["v"]
        res_table += '\n'

        # generate the separator when the label row is shown
        for i, val in max_col_len.items():
            if i == 0:
                res_table += border["l"]
            else:
                res_table += border["m"]
            res_table += border["h"] * val
        res_table += border["r"]
        res_table += '\n'

    # generate the main table
    for row in rows:
        for i, col in enumerate(row):
            res_table += border["v"]
            res_table += pad_item(str(col), max_col_len[i], centered)
        res_table += border["v"]
        res_table += '\n'

    # generate the bottom border of the table
    for i, val in max_col_len.items():
        if i == 0:
            res_table += border["bl"]
        else:
            res_table += border["bm"]
        res_table += border["h"] * val
    res_table += border["br"]
    res_table += '\n'

    return res_table


# uncomment the following code to test program
# table = make_table(
#     rows=[
#         ["Lemon"],
#         ["Sebastiaan"],
#         ["KutieKatj9"],
#         ["Jake"],
#         ["Not Joe"]
#     ]
# )
# print(table)
