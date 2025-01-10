import maya.cmds as cmds
import re

def select_next_transform():
    # Get the current selection
    selected = cmds.ls(selection=True)
    
    if not selected:
        print("No object selected.")
        return
    
    for selected_node in selected:
        # Use regular expression to find the last number in the node name
        match = re.search(r'(\d+)(?!.*\d)', selected_node)
        
        if match:
            current_num = int(match.group(0))
            next_num = current_num + 1
            
            # Replace the current number with the next number in the name
            new_node_name = re.sub(r'(\d+)(?!.*\d)', str(next_num), selected_node)
            
            # Check if the new name exists and is a transform node
            if cmds.objExists(new_node_name):
                transform_node = cmds.ls(new_node_name, type="transform")
                if transform_node:
                    # Add the new node to the current selection without replacing the previous selection
                    cmds.select(transform_node[0], add=True)
                    print(f"Added to selection: {transform_node[0]}")
                else:
                    print(f"No transform found with name: {new_node_name}")
            else:
                print(f"No object exists with the name: {new_node_name}")
        else:
            print(f"No number found in the selected object name: {selected_node}")

# Example usage:
select_next_transform()
