import os
from dotenv import load_dotenv, set_key

load_dotenv()

settings = {
    'forward' : os.getenv('MOVE_FORWARD'),
    'backward' : os.getenv('MOVE_BACKWARD'),
    'left' : os.getenv('TURN_LEFT'),
    'right' : os.getenv('TURN_RIGHT')
}

def save_key(key, value):
    set_key('.env', key, value)