PROJECT DIORA
A Web Application where users can post stories, update stories, delete stories, and view other user's stories. 
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

*Install the following using CMD, to initialize the programs' extension requirements:

Flask
Flask-SQLAlchemy
Flask_login
DateTime
Flask_wtf
WTForms
Flask_bcrypt

*Database

The database file was created using DB Browser for SQLite and was used to view inputted values from the website.
Database filename: diora.db

_______________________________________________________________________________________________________________

Programmed by: 

Buentipo, Anthony C.

Gatmin, Charlene S.

