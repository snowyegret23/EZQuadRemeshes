bl_info = {
    "name": "EZQuadRemeshes",
    "author": "snowyegret",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > EZQuadRemeshes",
    "description": "Easy quad remeshing tool",
    "category": "Mesh",
}

import bpy
from . import ez_quadremeshes_operation
from . import ez_quadremeshes_panel

def register():
    ez_quadremeshes_operation.register()
    ez_quadremeshes_panel.register()

def unregister():
    ez_quadremeshes_panel.unregister()
    ez_quadremeshes_operation.unregister()

if __name__ == "__main__":
    register()