import random
import math
import rhinoscriptsyntax as rs

def random_selection_from_objects():
    # Try to get currently selected objects
    objs = rs.SelectedObjects()
    # If no selection, prompt user to select objects
    if not objs:
        objs = rs.GetObjects("Select objects to randomly select from", preselect=True)
        if not objs:
            rs.MessageBox("No objects selected.", 0, "Warning")
            return

    total_count = len(objs)
    percentage = rs.GetInteger("Enter selection percentage (1-100):", 50, 1, 100)
    if percentage is None:
        rs.MessageBox("No percentage entered.", 0, "Warning")
        return

    # Calculate the number to select, at least 1
    count_to_select = max(1, int(math.ceil(total_count * percentage / 100.0)))
    selected_subset = random.sample(objs, count_to_select)

    # Unselect all, select the random subset
    rs.UnselectAllObjects()
    rs.SelectObjects(selected_subset)

random_selection_from_objects()
  