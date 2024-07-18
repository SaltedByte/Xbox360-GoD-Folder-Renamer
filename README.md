# Xbox360-GoD-Folder-Renamer
This script renames your GoD folders to a more readable and user-friendly format.

### Prerequisites
* Python installed on your machine
* All of your GoD folders (i.e. 584109F6) in the same directory

### Disclaimer
Please use responsibly, this is intended for your legally obtained GoD backup folders.  I am not endorsing obtaining these files in any illegitimate ways.
> [!CAUTION]
> If you are unfamiliar with python or this script, I strongly suggest that you make a backup of your collection or copy a few folders into a test directory.  This is to ensure you understand how this script works before using it incorrectly and possibly alter your library in ways you did not intend.

### Instructions
1. Download both the renamer.py and games_mapping.txt files into the same directory
2. Open the renamer.py file in a text editor like notepad
3. Edit line 4 to change to games_dir variable to the path to your GoD folder directory (make sure you use 2 \\ when pasting)
4. Save renamer.py
5. Open a terminal in that directory (depending on your OS, you should be able to CD into the directory or start there)
6. Run the following command.     ```python renamer.py```
7. Your game folders should now be renamed to the title of the game instead of their ID

### Future Considerations
The game_mapping.txt file is a work in progress and has some duplicated titles.  The list of games are incomplete but should mostly be there.  If you feel so inclined, please make a pull request with a more complete list of games.  I would be than happy to merge it into the project.
