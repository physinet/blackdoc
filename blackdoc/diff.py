import datetime
import difflib

from .colors import color_diff


def unified_diff(a, b, path, color):
    then = datetime.datetime.utcfromtimestamp(path.stat().st_mtime)
    now = datetime.datetime.utcnow()
    src_name = f"{path}\t{then} +0000"
    dst_name = f"{path}\t{now} +0000"

    diff = "\n".join(
        difflib.unified_diff(
            a.splitlines(),
            b.splitlines(),
            fromfile=src_name,
            tofile=dst_name,
            lineterm="",
        )
    )
    if color:
        diff = color_diff(diff)

    return diff
