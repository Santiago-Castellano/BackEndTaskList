from enum import Enum

class Message(Enum):
    SUCCESS = 'success'
    ERROR = 'error'
    DELETE_SUCCESS = 'deleted'
    UPDATE_SUCCESS = 'updated'

def permission_denied(action):
    return f"You don't have permission to {action} that."