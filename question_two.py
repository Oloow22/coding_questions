class User:
    #the user class to represet a user
    def __init__(self, id, name, email):
        #initialize the user with all their attributes
        self.id = id
        self.name = name
        self.email = email

class UserManager:
    # class to manage the users stored in memory
    
    def __init__(self):
        #initialize the user manager as an empty list
        self.users = []

    def add_user(self, id, name, email):
        #add a user to the list
        new_user = User(id, name, email)
        self.users.append(new_user)
        return new_user

    def get_user(self, id):
        #retrieve a user by their id
        for user in self.users:
            if user.id == id:
                return user
            else: print("User does not exist")

    def update_user(self, id, name=None, email=None):
        #changing a users details
        user = self.get_user(id)
        if name:
            user.name = name
        if email:
            user.email = email
        return user

    def delete_user(self, id):
        # Find the user by ID
        user = self.get_user(id)
        
        # Remove user from the list by excluding the user with the given ID
        updated_users = []
        for u in self.users:
            if u.id != id:
                updated_users.append(u)
        self.users = updated_users
        
        # Return the deleted user
        return user


user_manager = UserManager()

try:
    # Add new users
    user1 = user_manager.add_user(1, "David", "david@example.com")
    user2 = user_manager.add_user(2, "Mike", "mike@example.com")

    # Retrieve a user by ID
    retrieved_user = user_manager.get_user(1)
    print(f"Retrieved User: {retrieved_user.name} ({retrieved_user.email})")

    # Update a user's details
    updated_user = user_manager.update_user(1, name="John Smith")
    print(f"Updated User: {updated_user.name} ({updated_user.email})")

    # Delete a user by ID
    deleted_user = user_manager.delete_user(2)
    print(f"Deleted User: {deleted_user.name} ({deleted_user.email})")

except ValueError as e:
    print(f"Error: {e}")