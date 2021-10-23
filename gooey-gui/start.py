from pathlib import Path


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


def main():
    """
    Main program to find files with a given extension in a given directory.

    This will parse the command line arguments, find the files, and the print
    the results.
    """
    pass



if __name__ == "__main__":
    main()
