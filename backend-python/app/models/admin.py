from dataclasses import dataclass
from user import User
from enums import Gender, UserRole

@dataclass
class Admin(User):
    admin_id: int
    role: UserRole = UserRole.ADMIN