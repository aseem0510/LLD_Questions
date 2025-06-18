from typing import List, Optional
from Group.Group import Group
from User.User import User


class GroupController:
    def __init__(self):
        self.group_list: List[Group] = []

    def create_new_group(self, group_id: str, group_name: str, created_by_user: User) -> Group:
        # Create a new group
        group = Group()
        group.group_id = group_id
        group.group_name = group_name

        # Add the user who created the group as a member
        group.add_member(created_by_user)

        # Add the group to the global list of groups
        self.group_list.append(group)
        return group

    def get_group(self, group_id: str) -> Optional[Group]:
        for group in self.group_list:
            if group.group_id == group_id:
                return group
        print("No such group exists!")
        return None

    def get_all_groups(self) -> List[Group]:
        return self.group_list
