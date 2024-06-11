# Museum Route Finder

## Overview

This application provides a graphical interface to find routes through a museum based on selected entrances and target galleries. The program uses depth-first search to generate all possible routes, ensuring that no subset routes are included in the final result. The routes are then displayed in a Tkinter GUI.

## Features

- Select multiple entrances and target galleries.
- Generate and display all possible routes excluding subsets.
- User-friendly Tkinter interface for easy interaction.

## Required Libraries

- `tkinter`: For the graphical user interface.
- `collections.defaultdict`: For handling the graph data structure.

## Installation

Ensure you have Python installed (version 3.6 or higher). The required libraries are included with the Python standard library.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/museum-route-finder.git
    cd museum-route-finder
    ```

2. Run the script:
    ```bash
    python museum_route_finder.py
    ```

3. In the GUI:
    - Select one or more entrances.
    - Select the target galleries.
    - Click the "Find routes" button to generate and display the possible routes.

## Files

- `museum_route_finder.py`: Main script containing the application logic and GUI.

## Example

1. Select entrances (e.g., UL1, UL2).
2. Select target galleries (e.g., PG1, S1G2).
3. Click "Find routes" to see the possible routes displayed in the text area.

Enjoy exploring the museum routes!

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

