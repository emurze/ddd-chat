import uuid
from datetime import datetime


def next_id() -> str:
    return str(uuid.uuid4())


def get_current_date() -> datetime:
    return datetime.utcnow()
