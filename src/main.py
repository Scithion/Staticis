import os
import shutil
import sys
from gencontent import *
from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"



def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(f"Using basepath: {basepath}")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    #generate_pages_recursive("content", "template.html", "public", basepath) adjusting for project 5.5 step 4
    generate_pages_recursive("content", "template.html", "docs", basepath)
 


main()
