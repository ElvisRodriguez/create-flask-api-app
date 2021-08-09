import argparse
import os

from distutils.dir_util import copy_tree

def create_flask_app(destination):
    package_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(package_path, "api_template")
    current_directory = os.getcwd()
    destination_directory = os.path.join(current_directory, destination)
    copy_tree(template_path, destination_directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Flask API template")
    parser.add_argument("-p", "--project-name", help="Directory name for template", default="my-flask-app")
    args = parser.parse_args()
    create_flask_app(args.project_name)