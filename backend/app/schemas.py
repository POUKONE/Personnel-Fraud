from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class EmployeeIn(BaseModel):
    username: str
    full_name: Optional[str]
    email: Optional[str]
    department: Optional[str]
    role: Optional[str]

class EventIn(BaseModel):
    employee_id: Optional[int]
    event_time: Optional[datetime]
    ip: Optional[str]
    user_agent: Optional[str]
    success: Optional[bool]
    device_id: Optional[str]
    action: Optional[str]
    resource_type: Optional[str]
    resource_id: Optional[str]
    before: Optional[Any]
    after: Optional[Any]
    source: Optional[str]