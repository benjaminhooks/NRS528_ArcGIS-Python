# 1. Simple directory tree
# Replicate this tree of directories and subdirectories:
#
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

import os
import shutil

os.mkdir(r"C:\CC3")

os.mkdir(r"C:\CC3\draft_code")

os.mkdir(r"C:\CC3\draft_code\pending")

os.mkdir(r"C:\CC3\draft_code\complete")

os.mkdir(r"C:\CC3\includes")

os.mkdir(r"C:\CC3\layouts")

os.mkdir(r"C:\CC3\layouts\default")

os.mkdir(r"C:\CC3\layouts\post")

os.mkdir(r"C:\CC3\layouts\post\posted")

os.mkdir(r"C:\CC3\site")

shutil.rmtree(r"C:\CC3")

# Feedback - add a description of the challenge as comment at the top of each file. Makes life easier for me.
# Code looks great, lots of work to write out all the mkdir, but now its embedded in your brain.