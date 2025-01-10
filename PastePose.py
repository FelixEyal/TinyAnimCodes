import maya.cmds as cmds

def pasteAttributes(copied_attributes):
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("Please select objects.")
        return
    
    for obj in selected_objects:
        if obj in copied_attributes:
            attr_values = copied_attributes[obj]
            for attr, value in attr_values.items():
                try:
                    cmds.setAttr(f"{obj}.{attr}", value)
                except:
                    cmds.warning(f"Could not paste attribute '{attr}' to '{obj}'.")
        else:
            cmds.warning(f"No attributes copied for object '{obj}'.")
            

# Assuming you have copied attributes earlier and stored them in 'copied_attributes'
# Call the function
pasteAttributes(copied_attributes)
