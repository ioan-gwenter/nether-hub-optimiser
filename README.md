# nether-hub-optmiser
A simple python tool for optimising nether-highway travel paths in Minecraft.

![image](https://github.com/user-attachments/assets/98c31e5b-a824-43f9-86e0-e72b38ea1abc)

Input your currently defined portals in the dictionary provided, plus add your hub location. Run the script for a pseudo-optimal layout for nether highways.

The current algorithm will attempt to prioritise sticking to the inital cardinal directions (NSEW) before creating sub-highways via a greedy approach. This is by no means perfect and is ongoingly being improved.

Constraints that should be considered:
1. Highways can only be axially alligned (NS, EW)
2. The number of turns should be minimized. A turn can have many directions.
3. Near-Axially parallel highways should be merged to form sub-highways
