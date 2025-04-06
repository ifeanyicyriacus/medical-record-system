from dataclasses import dataclass
from datetime import datetime
from enums import Gender
import bcrypt

@dataclass
class User:
    first_name: str
    last_name: str
    hash_password: str
    phone_number: str
    email_address: str
    dob: datetime
    gender: Gender
    role: str = "user"

    def set_password(self, password: str):
        self.hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.hash_password.encode('utf-8'))