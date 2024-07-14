import os, rich
from rich.text import Text
from rich.tree import Tree
from rich.console import Console

console = Console()
max = None
no_recursion_calc = None


def g_size(file):
    try:
        return os.path.getsize(file)
    except:
        return None


def f_size(size):
    if size == None:
        return None
    num = 0
    while size > 1024:
        size /= 1024
        num += 1
    unit = ["B", "KB", "MB", "GB", "TB", "PB"]
    return f"{size:.2f} ".rstrip(".0").zfill(1) + unit[num]


def walk_dir(path, tree, level=0):
    global max, no_recursion_calc
    try:
        listdir = os.listdir(path)
    except:
        return 0
    total_size = 0
    for file in listdir:
        if no_recursion_calc and level >= max:
            continue
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            parent = None
            if level < max:
                parent = tree.add(f"[bright_magenta]{file}")
            size = walk_dir(file_path, parent, level + 1)
            if size and parent:
                parent.label += f"[bright_yellow] ({f_size(size)})"
        else:
            size = g_size(file_path)
            if level < max:
                text_filename = Text(file, "bright_green")
                text_filename.highlight_regex(r"\.[^.]+$", "bold blue")
                text_filename.append(f" ({f_size(size)})", "bright_cyan")
                tree.add(text_filename)
        if size:
            total_size += size
    return total_size


def tree(path, m_level=7):
    global max, no_recursion_calc
    max = m_level
    no_recursion_calc = False
    tree = Tree(f"[bright_magenta]{os.path.abspath(path)}")
    size = walk_dir(path, tree)
    tree.label += f" [bright_yellow]({f_size(size)})"
    rich.print(tree)
