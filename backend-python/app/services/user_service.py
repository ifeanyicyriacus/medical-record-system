from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User):
        user.set_password(user.hash_password)
        return self.user_repository.save(user)

    def get_user_by_id(self, user_id: int):
        return self.user_repository.find_by_id(user_id)

    def update_user(self, user: User):
        return self.user_repository.update(user)

    def delete_user(self, user_id: int):
        return self.user_repository.delete(user_id)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None