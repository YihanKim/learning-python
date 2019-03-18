from flask import Flask

app = Flask(__name__) # __main__ or filename

from app import routes


