'''                                    LAB: Directory Search with os Module [recursion]

DIFFICULTY: Easy
TIME: 15-30 minutes

OBJECTIVES:
-Boost skills in OS interaction using Python.
-Implement practical applications of the os module functions.

SCENARIO:
Develop a program to recursively search for directories in a specified path using Python's os module.

[labs_to_be_revisited_directory_tree.png]

FEATURES:
-Implement a function `find` that takes two arguments: `path` and `dir`.
--`path` is where the search begins, and can be either relative or absolute.
--`dir` is the directory name you're searching for.
-Output the absolute paths of any matching directories.
-Execute the search recursively to include all subdirectories.

EXAMPLE:
Input: path="./tree", dir="python"
Output:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python

'''




import os

# os.makedirs("tree/c/other_courses/cpp")
# os.mkdir("tree/c/other_courses/python")
# os.chdir("tree")
# os.makedirs("cpp/other_courses/c")
# os.mkdir("cpp/other_courses/python")
# os.makedirs("python/other_courses/c")
# os.mkdir("python/other_courses/cpp")
# os.chdir("..")


import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print()
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")

'''
Managed to print two out of three output lines correctly but decided it wasn't efficient to continue. 
Reviewed the official solution (shown above as deleted own attempt), which was is also flawed.  It prints all lines but 
includes an incorrect, extra folder in each directory path. A next step is to find a reliable external example focusing on 
recursion for directory traversal.
'''