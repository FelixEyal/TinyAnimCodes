import maya.cmds as cmds

def transferAttributes():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("Please select objects.")
        return
    
    for obj in selected_objects:
        # Get the object's name and side (assuming a naming convention)
        obj_name, obj_side = obj.rsplit('_', 1)
        
        if obj_side == "R":
            opposite_obj_name = obj_name + "_L"
        elif obj_side == "L":
            opposite_obj_name = obj_name + "_R"
        else:
            cmds.warning(f"Object '{obj}' does not follow the naming convention.")
            continue
        
        if cmds.objExists(opposite_obj_name):
            attributes = cmds.listAttr(opposite_obj_name, keyable=True)
            for attr in attributes:
                try:
                    value = cmds.getAttr(f"{opposite_obj_name}.{attr}")
                    cmds.setAttr(f"{obj}.{attr}", value)
                except:
                    cmds.warning(f"Could not copy attribute '{attr}' from '{opposite_obj_name}' to '{obj}'.")

# Call the function
transferAttributes()