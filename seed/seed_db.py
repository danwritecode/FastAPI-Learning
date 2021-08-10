import sqlite3

con = sqlite3.connect("test_app.db")

cur = con.cursor()

try:
    # Create table
    cur.execute('''CREATE TABLE User
                (User_Id int, Email text, Name text)''')
except:
    pass

users = [
    { "user_id":23459876, "email":"jane@email.com", "name": "Jane Doe" },
    { "user_id":34532356, "email": "kansan@email.com", "name": "Kansan Nakamoto" },
    { "user_id":34532357, "email": "henry@email.com", "name": "Henry Falls" },
    { "user_id":34532358, "email": "rixen@email.com", "name": "Rixen Knox" }
]

for user in users: 
    cur.execute("insert into User values (?, ?, ?)", (user["user_id"], user["email"], user["name"]))

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()