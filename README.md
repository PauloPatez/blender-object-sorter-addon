# Blender Object Sorter Add-on
This add-on provides a quick and easy way to sort the objects inside a collection alphabetically in Blender. By default, Blender does not provide a built-in way to sort objects, so this add-on fills that gap.

I created this add-on because I needed the objects inside collections in a specific order for a geometry nodes project, and found that sorting them alphabetically was the easiest way to achieve this.

## Installation
1. Download the [latest release](https://github.com/PauloPatez/blender-object-sorter-addon/releases/download/v0.0.1/object-sorter-v0.0.1.zip) of the add-on as a .zip file.
2. In Blender, go to Edit > Preferences > Add-ons.
3. Click the "Install" button and select the downloaded .zip file.
4. Enable the add-on by checking the box next to its name.

## Usage
Before using the add-on, it's important to understand how the "Sort Alphabetically" option in the Restriction Toggles menu works. This option affects only the way objects are displayed in the Outliner panel, and does not affect the real order of objects in the scene. When "Sort Alphabetically" is enabled, objects are displayed in alphabetical order based on their names, and when it is disabled, they are displayed in the order they are stored in memory, usually it is the order they were created.

To use the add-on:

1. In the Outliner panel, disable the "Sort Alphabetically" option in the Restriction Toggles menu.
2. Right-click on the collection that you want to sort.
3. Select "Sort Objects Alphabetically" from the context menu.
4. The add-on will then sort the objects inside the selected collection alphabetically.

## Planned Features
Manual sorting of objects is planned for a future update of the add-on.

## Contributing
If you encounter any issues with the add-on, please feel free to open a new issue on the GitHub repository. Pull requests are also welcome if you would like to contribute to the development of the add-on.

## License
This add-on is released under the GNU General Public License v3.0. See the LICENSE file for more details.
