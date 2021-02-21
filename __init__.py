# ----------------------------------------------------------
# File __init__.py
# ----------------------------------------------------------
#

# Addon info
# ----------------------------------------------------------

bl_info = {
    "name": "Shape Key Transfer",
    "description": "Copies shape keys from one mesh to another.",
    "author": "Amir Shehata, email: amir.shehata@gmail.com",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tools > Shape Key Transfer",    
    "warning": "This has not been tested rigorously.",
    "wiki_url": "",    
    "category": 'Mesh'}


# register
# ----------------------------------------------------------

import bpy
from bpy.props import (PointerProperty, CollectionProperty, StringProperty, EnumProperty)
from . uisettings import *
from . shapekeytransfer import *

    
# Custom scene properties

bpy.types.Scene.customshapekeylist_index = IntProperty()
bpy.types.Scene.srcMeshShapeKey = StringProperty()
bpy.types.Scene.destMeshShapeKey = StringProperty()

def load_custom_properties():
    bpy.types.Scene.shapekeytransferSettings = PointerProperty(type=UISettings)
    bpy.types.Scene.listUse = EnumProperty(
        items=[
            ('all', 'all', 'Transfer all shape keys in the source mesh', 'HIDE_OFF', 0),
            ('include', 'include', 'Include all shape keys in the list', 'HIDE_OFF', 1),
            ('exclude', 'exclude', 'Exclude all shape keys in the list', 'HIDE_ON', 2)
        ],
        default="all"
    )
    bpy.types.Scene.customshapekeylist = CollectionProperty(type=ShapeKeyItem)

#bpy.app.handlers.load_post.append(load_custom_properties)

def register():
    bpy.utils.register_class(UISettings)
    bpy.utils.register_class(TransferShapeKeysOperatorUI)
    bpy.utils.register_class(ShapeKeyItem)
    bpy.utils.register_class(CopyDrivers)

    bpy.utils.register_class(CopyKeyNamesOperator)
    bpy.utils.register_class(InsertKeyNamesOperator)
    bpy.utils.register_class(TransferShapeKeyOperator)
    bpy.utils.register_class(CopyShapeKeys)
    bpy.utils.register_class(TransferExcludedShapeKeyOperator)
    bpy.utils.register_class(RemoveShapeKeyOperator)
    bpy.utils.register_class(CUSTOM_OT_actions)
    bpy.utils.register_class(CUSTOM_OT_clearList)
    bpy.utils.register_class(CUSTOM_OT_removeDuplicates)
    bpy.utils.register_class(CUSTOM_UL_items)

    load_custom_properties()

    bpy.utils.register_class(VIEW3D_PT_tools_ShapeKeyTransfer)


# unregister
# ----------------------------------------------------------

def unregister():
    bpy.utils.unregister_class(UISettings)
    bpy.utils.unregister_class(TransferShapeKeysOperatorUI)
    bpy.utils.unregister_class(ShapeKeyItem)
    bpy.utils.unregister_class(CopyDrivers)

    bpy.utils.unregister_class(CopyKeyNamesOperator)
    bpy.utils.unregister_class(InsertKeyNamesOperator)
    bpy.utils.unregister_class(TransferShapeKeyOperator)
    bpy.utils.unregister_class(CopyShapeKeys)
    bpy.utils.unregister_class(TransferExcludedShapeKeyOperator)
    bpy.utils.unregister_class(RemoveShapeKeyOperator)
    bpy.utils.unregister_class(CUSTOM_OT_actions)
    bpy.utils.unregister_class(CUSTOM_OT_clearList)
    bpy.utils.unregister_class(CUSTOM_OT_removeDuplicates)
    bpy.utils.unregister_class(CUSTOM_UL_items)
    bpy.utils.unregister_class(VIEW3D_PT_tools_ShapeKeyTransfer)
