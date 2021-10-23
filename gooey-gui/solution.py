from pathlib import Path
from argparse import ArgumentParser
from gooey import Gooey, GooeyParser


def find_files(top: Path, extensions: list[str]) -> list[dict[str, Path]]:
    """
    Finds all files in the given directory with the given extensions.
    Returns a list of dictionaries with the file name and path.
    """
    return {ext: list(Path(top).resolve().rglob(f"*.{ext}")) for ext in extensions}


def display_files(files: list[dict[str, Path]]) -> None:
    """
    Displays the files in the given list.
    """
    for ext, file_list in files.items():
        if not file_list:
            continue
        print(f"{ext}:")
        for file in file_list:
            print(f"- {str(file)}")

    print("\n\n", "*" * 40)
    print("Summary:")
    for ext, file_list in files.items():
        print(f".{ext} Files: {len(file_list)}")


def find_and_display_files(top: Path, extensions: list[str]) -> None:
    """
    Finds all files in the given directory with the given extensions.
    Displays the results.

    This function really only exists to help highlight the similarities between
    `main` and `gooey_main`.

    Since we're using a text input field for the file extensions, we need to
    account for the user using commas to separate the extensions. This is only
    necessary for the Gooey version.
    """
    extensions = [ext.replace(",", " ") for ext in extensions]
    files = find_files(top, extensions)
    display_files(files)


def main():
    """
    Main program to find files with a given extension in a given directory.

    This will parse the command line arguments, find the files, and the print
    the results.
    """
    parser = ArgumentParser(description="Find files on your machine")
    parser.add_argument("-d", "--directory", type=str, required=True)
    parser.add_argument("-e", "--extensions", type=str, nargs="+", required=True)
    args = parser.parse_args()

    find_and_display_files(args.directory, args.extensions)


@Gooey
def gooey_main():
    """
    Demonstrate using the GooeyParser.

    You could add `@Gooey` to the main function, but the main function is just
    using the standard ArgumentParser. This shows how similar the GooeyPasrser
    is to the ArgumentParser. The only real difference here is that we are
    specifying the `DirChooser` widget for the `directory` argument to make it
    nicer to use.
    """
    parser = GooeyParser(description="Find files on your machine")
    parser.add_argument(
        "-d", "--directory", type=str, required=True, widget="DirChooser"
    )
    parser.add_argument("-e", "--extensions", type=str, nargs="+", required=True)
    args = parser.parse_args()

    find_and_display_files(args.directory, args.extensions)


if __name__ == "__main__":
    gooey_main()
