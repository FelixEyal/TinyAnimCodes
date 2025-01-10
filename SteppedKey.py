import maya.cmds as cmds

def set_stepped_key_on_selected():
    # Get the current selection of objects
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        print("No objects selected.")
        return
    
    # Get the current time from the time slider
    current_time = cmds.currentTime(query=True)
    
    # Set stepped key on each selected object at the current time
    for obj in selected_objects:
        # Set key at current time
        cmds.setKeyframe(obj, time=current_time)
        
        # Change the tangent to stepped
        cmds.keyTangent(obj, time=(current_time,), inTangentType="step", outTangentType="step")
        
        print(f"Stepped key set for {obj} at time {current_time}")

# Example usage:
set_stepped_key_on_selected()