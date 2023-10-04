Pygame Raycasting Engine
This project implements a 2D raycasting engine in Pygame to simulate a 3D perspective.

Overview
main.py - Runs the main game loop and contains the entry point code
settings.py - Defines configuration settings like screen size, colors, etc
entity.py - Contains the player entity class and movement controls
map.py - Defines the 2D map array and processes it into map blocks
raycasting.py - Handles casting rays and projecting them into a 3D perspective
renderer.py - Renders the rays and map into the final scene

How it Works:
 main.py initializes Pygame and creates the screen
 Each frame, the player position is updated and rays are cast outward based on player view angle
 Rays intersect with map blocks, indicating distance to that block
 Ray distances are used to draw walls and floors scaled and projected into a 3D view
 Sprite objects can be overlaid and projected into perspective
 Running the Code
 To run the project, simple execute main.py:

Copy code

python main.py
Use WASD keys to move around.

ESC to quit.

Next Steps

Some ideas for enhancing the project:

Add lighting based on ray intersection angles
Implement field-of-view and fog effects
Add textures to map blocks
Allow jumping over/crouching under blocks
Add moving enemies and more game mechanics

Credits:
Raycasting algorithm expired from Lode Vandevenne's tutorials