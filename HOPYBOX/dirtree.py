import os
import rich
from rich.text import Text
from rich.tree import Tree

def get_file_size(file):
  try:
    return os.path.getsize(file)
  except:
    pass

def format_file_size(size):
  if size is None:
    return "Error:No permission"
  num = 0
  while size > 1024:
    size /= 1024
    num += 1
    unit = ["IB", "KIB", "MIB", "GIB", "TIB" ,"PIB"]
    return f"{size:.2f}".rstrip(".0").zfill(1) + unit[num]


def walk_dir(path, tree, level=0) -> int:
    global max_level, no_recursion_calc
    try:
        listdir = os.listdir(path)
    except:
        return 0
    total_size = 0
    for file in listdir:
        if no_recursion_calc and level >= max_level:
            continue
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            parent = None
            if level < max_level:
                parent = tree.add(f"[magenta]{file}")
            size = walk_dir(file_path, parent, level + 1)
            if size and parent:
                parent.label += f"[yellow] [{format_file_size(size)}]"
        else:
            size = get_file_size(file_path)
            if level < max_level:
                text_filename = Text(file, "green")
                text_filename.highlight_regex(r"\.[^.]+$", "")
                text_filename.append(
                    f" ({format_file_size(size)})", "\033[92m")
                tree.add(text_filename)
        if size:
            total_size += size
    return total_size


max_level = None
no_recursion_calc = None
def tree_dir(path, m_level=7, no_calc=False):
  global max_level, no_recursion_calc
  max_level = m_level
  no_recursion_calc = no_calc
  tree = "\033[92m{os.path.abspath(path)}"
  size = walk_dir(path, tree)
  tree.label += f"\033[92m[{format_file_size(size)}]"
  print(tree)
tree_dir('/sdcard/PL')