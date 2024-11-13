import argparse
import sys
from pathlib import Path

import yaml

mod_dirs = [
    "Electronics Enclosure",
    "Hydra",
    # "MercuryOne",
    "MercuryOne.1",
    "Misc"
]

required_fields = [
    "title",
    "author",
    "description"
]

failOnError = False


def main():
    parser = argparse.ArgumentParser("generate-docs")
    parser.add_argument("baseDir", help="Base directory to scan and generate docs for", type=str)
    parser.add_argument("outDir", help="Output directory", type=str)
    parser.add_argument("-f", "--failOnError", help="Exit with non ' status code if an error is found", action='store_true')
    args = parser.parse_args()

    global failOnError
    failOnError = args.failOnError

    base_dir = args.baseDir
    out_dir = args.outDir
    for directory in mod_dirs:
        generate_dir(Path(base_dir) / directory, Path(out_dir))


def generate_dir(directory: Path, out_dir: Path):
    print(f"Generating for {directory.name}")
    out_dir.mkdir(parents=True, exist_ok=True)

    f = open(out_dir / directory.name, "w")

    for mod_dir in list(sorted(directory.iterdir())):
        if mod_dir.is_dir():
            info = generate_mod_info(mod_dir)
            f.write(f"{info.title} - {info.description} - {info.author}\n")

    f.close()


def error(message):
    print(message, file=sys.stderr)
    if failOnError:
        exit(1)


class ModInfo:
    def __init__(self, info):
        self.title = info["title"],
        self.author = info["author"],
        self.description = info["description"],
        self.image = info["image"] if "image" in info else None,
        self.remixed_from = info["remixed_from"] if "remixed_from" in info else None,
        self.license = info["license"] if "license" in info else None


def generate_mod_info(mod_dir: Path) -> ModInfo:
    print(f"Mod: {mod_dir.name}")
    info_file = mod_dir / "info.yaml"
    if not info_file.exists():
        error(f"Directory {mod_dir.name} does not contain info.yaml")

    with open(info_file) as stream:
        try:
            info = yaml.safe_load(stream)

            # run some validations
            # check for required fields in info.txt
            for field in required_fields:
                if field not in info:
                    error(f"{mod_dir.name} is missing '{field}' in info.yaml.")

            files_dir = mod_dir / "files"
            has_files = (files_dir.exists() and len(list(files_dir.iterdir())) > 0)
            has_url = "url" in info

            # check if there are any files in files, otherwise url must exist
            if not (has_files or has_url):
                error(f"{mod_dir.name} is does not have any files nor any 'url' set in info.yaml")

            # ensure url starts with https://
            if has_url and (not info["url"].startswith("https://") or len(info["url"]) < 8 + 4):
                error(f"{mod_dir.name} 'url' is not valid")

            return ModInfo(info)

        except yaml.YAMLError as exc:
            print(exc)


main()
