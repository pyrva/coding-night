# Gooey GUI and PyInstaller

- https://docs.python.org/3/library/pathlib.html
- https://docs.python.org/3/library/argparse.html
- https://github.com/chriskiehl/Gooey
- https://www.pyinstaller.org/

This challenge is intended to show how to create a simple graphical user interface (GUI) for a script that you can share with others.
The Gooey package will take a simple command line script and provide a GUI with as little as two lines of code (including the import statement)!

`start.py` is a simple script that takes a directory and will find all files
of a given file type under that directory. It will then print out all the files that match the extensions and summarize how many files it found.

# Tasks

1. Take the `start.py` script and modify it so that it can read command line arguments. Use the [`argparse`](https://docs.python.org/3/library/argparse.html) library (part of the python standard library) to parse the arguments.

2. Using only the `@Gooey` decorator, convert the script from a command line utility to a GUI.

3. Swap `ArgumentParser` for `GooeyParser` to use the `DirChooser` widget to select the directory rather than having to type a directory path.

4. Use PyInstaller to create an executable that you could share with others.

# Extra Credit

Do the following in any order:

- Create boolean arguments for common file types that the user can check instead of having to type the file extensions they need.
- Use a `DateChooser` widget to provide a window of time in which the file must have been created/modified in.
- Play around with the `@Gooey` configuration options.
- Change the icons used by Gooey.
- Configure PyInstaller to output a single executable file rather than a directory.


## Skill Levels

Depeding on your skill level, you should start with the following configuration.

**Absolute Beginner:**
Take a look at `solution.py` and browse through the documentation to see if you can understand what is going on.

**Junior:**
Copy `requirements.txt` and `start.py` to your directory. Install the required packages. Work through the problems as best as you can. Refer to `solution.py` as necessary.

**Senior:**
Copy `start.py` to your directory. Figure out what packages you need to install and work through the problems as best as you can. 

**Professional:**
You have a blank slate. Make it all happen.
