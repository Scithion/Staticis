import os
import shutil
from htmlnode import *
from markdown_blocks import *
from inline_markdown import *
from textnode import *

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Trim trailing slash except when basepath is root
    base = basepath.rstrip("/") if basepath != "/" else ""
    template = template.replace('href="/', f'href="{base}/')
    template = template.replace('src="/', f'src="{base}/')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                # Compute relative path from content directory
                rel_path = os.path.relpath(md_path, dir_path_content)
                # Change .md to .html
                html_rel_path = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, html_rel_path)
                generate_page(md_path, template_path, dest_path, basepath)