from datetime import datetime, timedelta
from ics import Calendar, Event

def create_pd_block(summary="Explore new teaching tool", minutes=30, filepath="pd_block.ics"):
    c = Calendar()
    e = Event()
    e.name = summary
    e.begin = datetime.now() + timedelta(days=1, hours=9)  # tomorrow 9AM
    e.duration = timedelta(minutes=minutes)
    c.events.add(e)
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(c.serialize_iter())
    return filepath
