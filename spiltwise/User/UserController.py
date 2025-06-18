from typing import List, Optional
from User.User import User


class UserController:
    def __init__(self):
        self.user_list: List[User] = []

    def add_user(self, user: User):
        self.user_list.append(user)

    def get_user(self, user_id: str) -> Optional[User]:
        for user in self.user_list:
            if user.user_id == user_id:
                return user
        return None

    def get_all_users(self) -> List[User]:
        return self.user_list
