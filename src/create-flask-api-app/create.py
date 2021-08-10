import os

from distutils.dir_util import copy_tree

def create_flask_app(destination):
    package_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(package_path, "api_template")
    current_directory = os.getcwd()
    destination_directory = os.path.join(current_directory, destination)
    copy_tree(template_path, destination_directory)