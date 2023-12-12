
class GolfApp:
    def __init__(self):
        self.accounts = []

    def load_accounts(self):
        # Load existing accounts from storage (file, database, etc.) if needed
        # Example: self.accounts = load_accounts_from_storage()
        pass

    def save_accounts(self):
        # Save accounts to storage (file, database, etc.)
        # Example: save_accounts_to_storage(self.accounts)
        pass

    def create_account(self, first_name, last_name, handicap, username, password, is_admin):
        # Check if the username already exists
        usernames = [acc['Username'] for acc in self.accounts]
        if username in usernames:
            return None  # Username already exists

        new_account = {
            "First Name": first_name,
            "Last Name": last_name,
            "Handicap": handicap,
            "Username": username,
            "Password": password,
            "Is Admin": is_admin
        }
        self.accounts.append(new_account)
        return new_account

    def login(self, username, password):
        # Check if the username and password match an existing account
        for account in self.accounts:
            if account['Username'] == username and account['Password'] == password:
                return True  # Successful login
        return False  # Invalid credentials
