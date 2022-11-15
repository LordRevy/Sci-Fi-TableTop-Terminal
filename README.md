# Sci-Fi-TableTop-Terminal

#----LOG IN SCREEN

- When this program initiates, you will be asked to log in. The users.json and records.json files can be deleted for a fresh start.

- You can fill out your own username and password to create a new account. Any records you create will be signed with this name.

- If you opt for a fresh start, the first account created must be the "Administratus" (Game Master). This account will be given full access to all content.

- When trying to log in, the program will take your input and attempt to find a match in the users.json file. (If the file itself does not exist, it will create one). If a match is found, it will give you access to the terminal with the clearance level associated with the account.

- You will be able view the Title of all records stored on the system but if your clearance level is below the clearance of the document, you will not be able to read the body of it or see who wrote it.

#----MAIN SCREEN BUTTONS

- Record List: You can select Record List to view all records stored in the records.json file. For now, this will appear on the console.

- View Records: The console will query what record you are trying to view. If you do not know what the records name is, try the "Record List" button. You will only be able to access records that you are authorized to see. Each account has a clearance level associated with it.

- Create Record: This allows you to create a new record to be saved on the records.json file. Note that your record can only be as secret as the clearance level that you currently have. If you were not allowed to view forbidden documents but were attempting to write them, that may draw unwanted attention.

- Redact Record: Any user can Redact a record, so long as their clearance level is 1 level higher than the record they are trying to redact. But be careful, with the appropriate clearance, Redacted records can still be viewed. (If a mistake was made, the record could be permanently deleted by going into the records.json file and deleting the information manually).

- Administratus: This tab opens a new screen for the Game Master only. This allows the Game Master to 1. View all Users that currently exist on the terminal. and 2. Raise or lower users clearance levels.

#----KEEP IN MIND

- The Administratus role is generally reserved for the Game Master, but it could make perfect sense for the players to be the Aministrator for a network of Terminals. This could provide fun role play aspects like searching for names in a terminal to find who has used it. But be careful as the players will be able to view any record stored within the terminal, regardless if its classification.

#----FUTURE PLANS

1. The major improvement I would like to implement in the near future is converting all interaction from the console over to the GUI itself. This will make it much simpler to only have one screen to worry about. This would also make the UI cleaner and more immersive. This will be done by:
  - Shifting the main screen buttons to the side or bottom to make more room.
  - Using the "Example Text" space to display the console communications.
  - Adding an entry on the main screen to replace having to use console inputs.

2. Currently the records display on a simple tkinter info messagebox. I would like to change this to actually displaying a window with artwork of a 40k-esk document that populates the information on it. Another cool feature would be to have a different documents depending on the classification. (so classified documents might have "CLASSIFIED" scrawled across the top, forbidden documents may have purity seals, etc.)

3. Once I get these goals done, I would like to comb through the code and attempt to simplify what I can and make it more readable.

