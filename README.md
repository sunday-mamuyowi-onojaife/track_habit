							                                     	HOW TO RUN THE HABIT TRACKER APP
The database need to be set up first, for the app to come up in the first place, else it will hang the cursor in the command line. In the MySql DBMS, a database is named habit_tracker, then the accompanying SQL file called habit_tracker_database.sql is imported whilst we are in the empty database we created, this import allows us to prepopulate the empty database with our data.

Amongst the data is a 4 weeks data for a user with username karpov, email karpov@gmail.com and password karpov.
The habit.py,habitapi.py,habitdb.py,user.py are use to model the user and the user's habit and more so the habitdb.py represents the app's interaction with the underlying DBMS (database). The habitapi.py acts as the interface that make it easy for the model to be used by it's clients i.e. the Graphical User Interface classes that was built.

The graphical user interface was built using python cli module called Textual. With textual the user interface was crafted as widget that lives on the command line interface.

The entire Python Texture Module classes use to organize the user interface all resides in a folder called tui, then a habit_gui.py acts as the driver that starts the execution of the app by typing the following command on the folder that holds all the file as thus;

C:\[appFolder]>python habit_gui.py <Enter>

This command starts the app and all functionality can be used.

Note:
The database need to be set up first before the app is started from the command line. 
