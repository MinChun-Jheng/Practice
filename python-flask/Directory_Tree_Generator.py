"""Directory Tree Generator
-----------------------------------
use argparser to add the arg
"""
import argparse
import os
from walkdir import filtered_walk

parser = argparse.ArgumentParser(description='Print the directory-tree code for the LaTex dirtree package.')
parser.add_argument(dest='path', type=str, help="Root directory of tree")
parser.add_argument('-d', '--maxDepth', type=int, help="Max depth for tree expansion")
parser.add_argument('-H', '--includeHidden', dest='includeHidden', action='store_true', help='Include hidden files')
parser.add_argument('-S', '--includeSystem', dest='includeSystem', action='store_true', help='Include system files')
system_file_names = [".DS_Store"]
# Delete trailing
def delete_trailing_slash(path_name):
    while path_name.endswith('/'):
        path_name = path_name[:-1]
    return path_name
# Counts how many level deeps 
def get_relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset
# Escape illagal Symbols for Latex
def escape_illegal(name):
    illegal_chaar_array = ['//', '&', '%', '$', '#', '_', '{', '}', '~', '^']
    for char in illegal_chaar_array:
        name = name.replace(char, "\\" + char)
    return name
rootDir = delete_trailing_slash(parser.parse_args().path)
includeHidden = parser.parse_args().includeHidden
includeSystem = parser.parse_args().includeSystem
maxDepth = parser.parse_args().maxDepth
# if the directory exists
if os.path.isdir(rootDir) and os.path.exists(rootDir):
    indentChar = " "
    # Depth of the root
    levelOffset = rootDir.count(os.path.sep) - 1
    # Create filter
    excluded_filter = []
    if not includeHidden:
        excluded_filter.append(".*")
    if not includeSystem:
        excluded_filter += system_file_names
    print("\dirtree{%")
    for dirName, subdirList, fileList in sorted(filtered_walk(rootDir, depth=maxDepth, excluded_dirs=excluded_filter)):
        level = get_relative_depth(dirName, levelOffset)
        baseName = os.path.basename(dirName)
        if level == 1:  #for the first level only print the wole path
            print(indentChar + "." + str(level) + "{" + escape_illegal(dirName) + "}.")
        else:
            print(indentChar * level + ","+ str(level) + "{" + escape_illegal(dirName) + "}.")
        level += 1
        for fileName in sorted(fileList):
            print(indentChar * level + "." + str(level) + " {" + escape_illegal(fileName) + "} .")
    print("}")
else:
    print("Error: root directory not found")