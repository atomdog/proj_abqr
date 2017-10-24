# proj_abqr
This code forms the algorithmic backbone of the Autonomous Biomimetic Quadrupedal Robot Project, my senior thesis project. 

Most of the codebase consists of functions so that relatively complicated actions can be abstracted to a level that is equal to the simplicity of the action that will be performed, such as turning 15 degrees from the current heading, or etc.

Simple and mathematical was the mantra during much of the design process, and the code does an acceptable job at representing that. 

Weaker links include the grid system. I am attempting to abstract it to what is functionally a Cartesian plane where every point above a certain resolution contains an additional state value. 

Here is a brief summary of each file and its functionality

1. angledet.py: calculates the angle between the current point's place on an abstract line and a point in the distance. 
