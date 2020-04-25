#!/usr/bin/env python3
"""
Test plane creation
"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')

from src import *


def main():
    # Scene creation
    scene = Scene("../shaders/", light_dir=(0, 1, 1), camera_dist=50)
    
    # Water generation
    scene.generate_water("../img/blue.jpg", 50)

    test = Object(scene.shaders['test'], "cube", "../obj/others/cube/cube.obj")
    scene.add(test)

    scene.viewer.run()


if __name__ == '__main__':
    glfw.init()
    main()
    glfw.terminate()