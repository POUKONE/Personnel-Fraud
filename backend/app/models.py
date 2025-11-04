from sqlalchemy import (MetaData, Table, Column, Integer, String, Date, TIMESTAMP, Boolean, JSON, ForeignKey)
from sqlalchemy.sql import func
metadata = MetaData ()
employees = Table (
    "employees",
    metadata,
    Column ("id", Integer, primary_key=True),
    Column ("username", String, unique=True, nullable=False),
    Column ("full_name", String),
    Column ("email", String, unique=True),
    Column ("department", String),
    Column ("role", String),
    Column ("manager_id", Integer, nullable=True),
    Column ("hire_date", Date, nullable=True),
    Column ("status", String, default="active"),
    Column ("created_at", TIMESTAMP, server_default=func.now())
)

auth_logs = Table(
    "auth_logs",
    metadata,
    Column ("id", Integer, primary_key=True),
    Column ("employee_id", Integer, nullable=True),
    Column ("event_time", TIMESTAMP, server_default=func.now()),
    Column ("ip", String),
    Column ("user_agent", String),
    Column ("success", Boolean),
    Column ("device_id", String),
    Column ("geo_city", String),
    Column ("geo_country", String)
)

app_events = Table(
    "app_events",
    metadata,
    Column ("id", Integer, primary_key=True),
    Column ("employee_id", Integer, nullable=True),
    Column ("event_time", TIMESTAMP, server_default=func.now()),
    Column ("action", String),
    Column ("resource_type", String),
    Column ("resource_id", String),
    Column ("before", JSON),
    Column ("after", JSON),
    Column ("source", String)
)

alerts = Table(
    "aletrs",
    metadata,
    Column ("id", Integer, primary_key=True),
    Column ("employee_id", Integer, nullable=True),
    Column ("alert_time", TIMESTAMP, server_default=func.now()),
    Column ("alert_type", String),
    Column ("score", String),
    Column ("details", JSON)
)