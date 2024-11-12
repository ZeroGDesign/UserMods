import argparse
import sys
from pathlib import Path
import yaml

mod_dirs = [
    "Misc"
]


def main():
    parser = argparse.ArgumentParser("generate-docs")
    parser.add_argument("baseDir", help="Base directory to scan and generate docs for", type=str)
    args = parser.parse_args()

    base_dir = args.baseDir
    for dir in mod_dirs:
        generate_dir(Path(base_dir) / dir)


def generate_dir(dir: Path):
    print(f"Generating for {dir.name}")
    for mod_dir in dir.iterdir():
        if mod_dir.is_dir():
            generate_mod_info(mod_dir)


def generate_mod_info(mod_dir):
    print(f"Mod: {mod_dir.name}")
    info_file = mod_dir / "info.yaml"
    if not info_file.exists():
        print(f"Directory {mod_dir.name} does not contain info.yaml", file=sys.stderr)
        exit(1)

    with open(info_file) as stream:
        try:
            info = yaml.safe_load(stream)
            
            title = info["title"]
            author = info["author"]
            description = info["description"]
            images = info["images"]

            print(title)
            print(author)
            print(description)
            for img in images:
                print(img)

        except yaml.YAMLError as exc:
            print(exc)

main()
