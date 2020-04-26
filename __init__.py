'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import bpy
from . powermylights import (ChangeLightPower_OT_operator,ChangePower_PT_Panel,MYLIGHTS_PT_Panel)


bl_info = {
    "name": "PowerMyLights",
    "author": "omnitrix9991",
    "location": "View3D",
    "description": "A addon to manage power of all lights in the Scene.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "wiki_url": "https://github.com/omnitrix9991/MeshVolumeModellerB3D",
    "warning": "",
    "category": "Object",
}




class LightAddonProperties(bpy.types.PropertyGroup):
    powerpercent: bpy.props.IntProperty(default=100, min=1,soft_max =300,step=10)
    checkto_applya: bpy.props.BoolProperty(default=True)

    collectioninfo:  bpy.props.PointerProperty(type=bpy.types.Collection)


classes = [LightAddonProperties,ChangeLightPower_OT_operator,ChangePower_PT_Panel,MYLIGHTS_PT_Panel]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.light_tool = bpy.props.PointerProperty(type=LightAddonProperties)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.light_tool


if __name__ == "__main__":
    register()


