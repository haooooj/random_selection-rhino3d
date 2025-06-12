
# Random Selection Tool for Rhino3D

Speed up your modelling and exploration process with a custom script that allows you to randomly select a percentage of objects from your current selection. This is especially useful for design variation studies, optimisation workflows, or when working with large object sets.

## What is the Random Selection Tool?

The **Random Selection Tool** lets you select a random subset of objects from a given group based on a user-defined percentage:

* Choose any group of objects in your Rhino model.
* Specify the percentage of items you want to randomly select.
* The script will automatically deselect all objects and reselect only the chosen random subset.

This tool is particularly useful in generative design processes, sampling studies, or curating large datasets for testing.

## Why Use It?

Rhino does not offer built-in tools to randomly filter objects from a selection. When working with complex or large-scale geometry, especially in iterative design processes, it can be tedious to manually select subsets. This tool automates and streamlines that process.

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` in the command line.
2. Browse to the location where you saved the script and select it.

### Method 2 Creating a Button or Alias for Easy Access (Optional)

#### Creating a Toolbar Button

1. **Right-click** on an empty area of the toolbar and select **New Button**.
2. In the **Button Editor**:

   * **Left Button Command**:

     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\random_selection.py"
     ```

     Replace `FullPathToYourScript` with the actual file path where you saved the script.
   * **Tooltip and Help**: Add a note like: `Randomly select a percentage of objects`.
   * **Set an Icon (Optional)**: Assign an icon if desired.

#### Creating an Alias

1. Go to **Tools > Options** and select the **Aliases** tab.

2. **Create a New Alias**:

   * **Alias**: For example, `randselect`
   * **Command Macro**:

     ```plaintext
     _-RunPythonScript "FullPathToYourScript\random_selection.py"
     ```

3. Use it by typing `randselect` into the command line.

### Using the Tool

1. **Select** the objects you want to sample from (or let the script prompt you).
2. You will be prompted to enter a **selection percentage** (e.g., 30).
3. The script will automatically:

   * Calculate how many objects correspond to that percentage.
   * Randomly choose that number of objects.
   * Unselect all and highlight only the randomly selected subset.

