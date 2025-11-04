import datetime
from sqlalchemy import select, and_
from .models import auth_logs, alerts
from .db import database

async def check_failed_logins(employee_id=None, ip=None):
    window = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
    query = select([auth_logs.c.employee_id, auth_logs.c.ip]).where(and_(auth_logs.c.event_time>= window,auth_logs.c.success == False))
    if employee_id:
        query = query.where(auth_logs.c.employee_id == employee_id)
    if ip:
        query = query.where(auth_logs.c.ip == ip)

    rows = await database.fetch_all(query)
    count = len(rows)
    if count >= 5:
        await database.execute(
            alerts.insert().values(
                employee_id=employee_id,
                alert_type="failed_logins",
                score=str(count),
                details={"count": count, "window_min": 5}
            )
        )
        return True
    return False