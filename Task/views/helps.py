from enum import Enum

class Message(Enum):
    SUCCESS = 'success'
    ERROR = 'error'
    DELETE_SUCCESS = 'deleted'
    UPDATE_SUCCESS = 'updated'
    