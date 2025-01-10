import maya.cmds as cmds

def copyAttributes():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("Please select objects.")
        return
    
    attribute_values = {}
    
    for obj in selected_objects:
        attributes = cmds.listAttr(obj, keyable=True)
        attr_values = {}
        
        for attr in attributes:
            try:
                value = cmds.getAttr(f"{obj}.{attr}")
                attr_values[attr] = value
            except:
                cmds.warning(f"Could not copy attribute '{attr}' from '{obj}'.")
        
        attribute_values[obj] = attr_values
    
    return attribute_values

# Call the function
copied_attributes = copyAttributes()
