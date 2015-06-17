import os
from config import app
from flask import Flask


# APPLICATION MAIN
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run('127.0.0.1', port=port)
	print '\nApplication Started'