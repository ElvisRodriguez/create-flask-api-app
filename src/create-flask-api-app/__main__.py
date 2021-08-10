import argparse

from create import create_flask_app

def main():
    parser = argparse.ArgumentParser(description="Create a Flask API template")
    parser.add_argument("-p", "--project-name", help="Directory name for template", default="my-flask-app")
    args = parser.parse_args()
    create_flask_app(args.project_name)

if __name__ == "__main__":
    main()