<h1>Building a GUI for Unix Commands Execution on MacOS</h1> 
<em>Sravya Kuchipudi (GWID: G43099352)</em> <br>

<h3>Project Purpose</h3> 
<p>The goal of this project is to provide a straightforward graphical user interface (GUI) that enables users to choose Unix commands from menus, enter the required parameters, run the commands, and show the results. This GUI will offer a simple and user-friendly alternative for MacOS's command prompt for executing Unix commands. </p>

<h2>Outline of Folders</h2> 
<ul>
  <li>data/ - any data used for the experiments and analysis is stored here</li>
  <li>papers/ - all the readings that have been analyzed are stored here
    <ul>
      <li>papers/articles/ - holds the articles that were referenced</li>
      <li>papers/textbooks/ - holds the textbooks that were referenced</li>
    </ul>
  </li>
  <li>presentations/ - presentations are stored here</li>
  <li>reports/ - all reports are stored here, named as report_DATE.pdf</li>
  <li>reviews/ - all reviews are stored here in respective folders, named as Review_Date_SubmitterName.pdf
    <ul>
      <li>reviews/reviewer/ - holds the reviews that I was reviewing</li>
      <li>reviews/submitter/ - holds the reviews that I am receiving</li>
    </ul>
  </li>
</ul>



<h2>Unix Commands GUI</h2>
<p>The Unix Commands GUI is a Python-based graphical user interface that allows you to execute various Unix commands using a user-friendly interface. This README provides instructions on how to use the GUI effectively.</p>
<h3>Getting Started</h3> 
<p>To use the Unix Commands GUI, follow these steps:</p>
<ol>
  <li>
    <p>Launch the GUI: Execute the Python script, and a window titled "Unix Commands GUI" will appear.</p>
  </li>
  <li>
    <p>Select a Command: In the main window of the GUI, you'll find a drop-down list labeled "Command." Click on the drop-down arrow to see a list of available commands.</p>
  </li>
  <li>
    <p>Choose a Command: From the drop-down list, select the Unix command you wish to run. Each command is accompanied by a brief description and a command template displayed in the "Arguments" entry field.</p>
  </li>
  <li>
    <p>Provide Command Arguments (If Required): Some commands require additional arguments to function correctly (e.g., file paths or directory names). If the selected command requires arguments, the corresponding template will be displayed in the "Arguments" entry field. Replace `<arguments>` in the template with the actual arguments you want to use.</p>
  </li>
  <li>
    <p>Run the Command: After selecting the command and providing the necessary arguments (if any), click the "Run" button. The GUI will execute the selected Unix command with the specified arguments.</p>
  </li>
  <li>
    <p>View Command Output: The output of the command will be displayed in a separate window titled "Output." The output will be preceded by the command and arguments you provided. If there are any errors during command execution, they will also be shown in this window.</p>
  </li>
  <li>
    <p>GUI Instructions: If you need a quick reminder of these instructions, you can click the "GUI Instructions" button. It will open a new window displaying the usage guidelines for the Unix Commands GUI.</p>
  </li>
  <li>
    <p>Command Information: To learn more about each available Unix command, click the "Command Info" button. A new window will open, showing a list of commands with their respective descriptions and templates.</p>
  </li>
</ol>
<h3>Caution</h3>
<p>This GUI is designed to execute basic Unix commands. Be cautious while running commands that modify or delete files/directories, as there is no confirmation prompt, and the actions will be performed immediately.</p>
<h3>Exiting the GUI</h3>
<p>To exit the GUI, simply close the main window or any other open window. You can use the close button (usually an "X" in the top right corner) to do this.</p>
<p>Now you are ready to use the Unix Commands GUI to perform various Unix commands and file operations in a simple and intuitive way. Enjoy!</p>
