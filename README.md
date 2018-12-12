PROJECT DIORA
A Web Application where users can post stories, update stories, delete stories, and view other user's stories. 
______________________________________________________________________________________________________________

Created Users(default, and can be used in the log-in page):
1. email: tc@gmail.com Password: tc
2. email: tony@gmail.com Password: tony
3. email: cha@gmail.com Password: cha
4. email: juan@gmail.com Password: juan
5. email: denise@gmail.com Password: 12345

______________________________________________________________________________________________________________

Functionalities:

1. A visitor of the website Diora can view posts that were posted 
   by other users, and search: by Title (Partial Search or Filtered Search) or by Author (Partial Search or Filtered Search).
2. A user can register to have an account by typing and completing the required fields: username, email, password.
3. A user can login to: 
	3.1. Create Stories by providing the following: Title, and Content. 
	3.2. Update Stories that the user posted.  
	3.3. Delete Stories that the user posted.
4. User's credentials will be stored in a database.
5. The Admin can view the following using the database: 
	5.1. stories created by users:
		5.1.1. author or user's username
		5.1.2. title of the story created by 5.1.1.
		5.1.3. date when the story was posted.
		5.1.4. content of the story.
	5.2. User's credentials:
		5.2.1. username
		5.2.2. email
		5.2.3. password(hashed to hide User's real password)
_______________________________________________________________________________________________________________

Things to Initialize:

*Install the following using CMD(pip install), to initialize the programs' extension requirements:

Flask, Flask-SQLAlchemy, Flask_login, DateTime, Flask_wtf, WTForms, Flask_bcrypt

*Database

The database file was created using DB Browser for SQLite and was used to view inputted values from the website.
Database filename: diora.db

_______________________________________________________________________________________________________________

How to run:

To run, open cmd, go to file location of diora.py and type:

python diora.py

then, go to chrome browser or any browser and type: 

localhost:5000

_______________________________________________________________________________________________________________

Programmed by: 

Buentipo, Anthony C.

Gatmin, Charlene S.

