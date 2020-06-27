# import sqlite3

# db = sqlite3.connect('bd.db')
# c = db.cursor()

# c.execute('''
# 	CREATE TABLE IF NOT EXISTS users (
# 	id INTEGER PRIMARY KEY,
# 	name TEXT NOT NULL, 
# 	email TEXT NOT NULL UNIQUE
# 	)
# ''')

# c.execute('INSERT INTO users (name, email) VALUES ("Jared", "jared@gmail.com")')
# c.execute('INSERT INTO users (name, email) VALUES ("Mary", "mary@gmail.com")')
# c.execute('INSERT INTO users (name, email) VALUES ("Rock", "rock@gmail.com")')
# c.execute('INSERT INTO users (name, email) VALUES ("Man", "man@gmail.com")')

# c.executescript('''
# 	INSERT INTO users (name, email) VALUES ("Rely", "rely@gmail.com");
# 	INSERT INTO users (name, email) VALUES ("Brick", "brick@gmail.com");
# 	INSERT INTO users (name, email) VALUES ("Stonks", "stonks@gmail.com")
# ''')

# users = [
# 	('User 1', 'user1@gmail.com'),
# 	('User 2', 'user2@gmail.com'),
# 	('User 3', 'user3@gmail.com')
# ]
# c.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)
# db.commit()

# ***********************************************************************
# Выборка данных 

import sqlite3

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

db = sqlite3.connect('bd.db')
db.row_factory = dict_factory
c = db.cursor()

email = 'rely@gmail.com'

# c.execute(f'SELECT * FROM users WHERE email = "{email}"')
# c.execute('SELECT * FROM users WHERE email = ?', (email,))
# c.execute('SELECT * FROM users WHERE email = :email OR name = :name', {'email': email, 'name': 'Rely'})

c.execute('SELECT * FROM users')
res = c.fetchall()

print(res)

# for user in res:
# 	print(user[1], user[2])



db.close()