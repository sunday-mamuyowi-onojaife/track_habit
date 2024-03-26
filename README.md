To set up the database that the habit tracking app gets it's data from and sends it's data to, the database needs to be created with some pre-populated data. Amongst the data is a 4 week data for a user with username karpov and email karpov@gmail.com, subsequently,users can be added as needed.
Accompanying the files,is a file called habit_tracker_database.sql, that need to be imported into MySQL DBMS to set up the data needed to assist log in into the App.

The habit.py,habitapi.py,habitdb.py,user.py are use to model the user and the user's habit and more so the habitdb.py represents the app's interaction with the underlying DBMS (database). The habitapi.py acts as the interface that make it easy for the model to be used by it's clients i.e. the Graphical User Interface classes that was built.

The graphical user interface was built using python cli module called Textual. With textual the user interface was crafted as widget that lives on the command line interface.

The entire Python Texture Module classes use to organize the user interface all resides in a folder called tui, then a habit_gui.py acts as the driver that starts the execution of the app by typing the following command on the folder that holds all the file as thus;

C:\[appFolder]>python habit_gui.py <Enter>

This command starts the app and all functionality can be used.

Note:
The database need to be set up first before the app is started from the command line. 
