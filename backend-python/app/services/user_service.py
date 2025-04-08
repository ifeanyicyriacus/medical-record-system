from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, data: dict) -> dict:
        return self.user_repository.create_user(data)

    def get_user_by_id(self, user_id: str) -> dict:
        return self.user_repository.get_user_by_id(user_id)

    def update_user(self, user: User) -> None:
        return self.user_repository.update_user(user)

    def delete_user(self, user_id: str) -> None:
        return self.user_repository.delete_user(user_id)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    def register_user(self, data: dict) -> dict:
        return self.create_user(data)

    def login_user(self, email: str, password: str):
        return self.authenticate_user(email, password)
