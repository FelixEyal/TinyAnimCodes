import maya.cmds as cmds
import re

def add_previous_transform_to_selection():
    # Get the current selection
    selected = cmds.ls(selection=True)
    
    if not selected:
        print("No object selected.")
        return
    
    # Assuming we're working with a single selection (the last selected object will be used for decrementing)
    selected_node = selected[-1]
    
    # Use regular expression to find the last number in the node name
    match = re.search(r'(\d+)(?!.*\d)', selected_node)
    
    if match:
        current_num = int(match.group(0))
        previous_num = current_num - 1
        
        if previous_num < 1:
            print("No lower transform available.")
            return
        
        # Replace the current number with the previous number in the name
        new_node_name = re.sub(r'(\d+)(?!.*\d)', str(previous_num), selected_node)
        
        # Check if the new name exists and is a transform node
        if cmds.objExists(new_node_name):
            transform_node = cmds.ls(new_node_name, type="transform")
            if transform_node:
                # Add the transform node to the current selection without deselecting
                cmds.select(transform_node[0], add=True)
                print(f"Added to selection: {transform_node[0]}")
            else:
                print(f"No transform found with name: {new_node_name}")
        else:
            print(f"No object exists with the name: {new_node_name}")
    else:
        print("No number found in the selected object name.")

# Example usage:
add_previous_transform_to_selection()
