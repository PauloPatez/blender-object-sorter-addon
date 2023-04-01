# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name" : "Object Sorter",
    "author" : "Paulo Patez",
    "description" : "",
    "blender" : (3, 1, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

def add_to_collection_menu(self, context):
    self.layout.operator("outliner.sort_collection_objects")

class OS_OT_SortCollectionObjects(bpy.types.Operator):
    bl_idname = "outliner.sort_collection_objects"
    bl_label = "Sort Objects Alphabetically"
    bl_description = "Sort objects inside the active collection alphabetically"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.collection is not None

    def execute(self, context):
        objects = context.collection.objects
        keys = [o.name for o in objects]
        keys.sort()
        count = len(keys)
        for index, key in enumerate(keys):
            if index == count - 1:
                continue
            obj = objects[key]
            objects.unlink(obj)
            objects.link(obj)
        return {'FINISHED'}

classes = [
    OS_OT_SortCollectionObjects
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
        bpy.types.OUTLINER_MT_collection_new.append(add_to_collection_menu)
        bpy.types.OUTLINER_MT_collection.prepend(add_to_collection_menu)

def unregister():
    for c in classes:
        bpy.types.OUTLINER_MT_collection_new.remove(add_to_collection_menu)
        bpy.types.OUTLINER_MT_collection.remove(add_to_collection_menu)
        bpy.utils.unregister_class(c)