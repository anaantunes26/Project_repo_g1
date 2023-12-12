class GolfApp:
    def __init__(self):
        self.accounts = []

    def load_accounts(self):
        # Hier könntest du vorhandene Accounts laden, wenn nötig
        pass

    def create_account(self, first_name, last_name, handicap, username, password, is_admin):
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

# Beispiel, wie die GolfApp verwendet werden könnte:
# golf_app = GolfApp()
# golf_app.load_accounts()

# Hier würdest du vermutlich Benutzereingaben erhalten und dann create_account() aufrufen
# username = "neuer_benutzername"
# password = "passwort123"
# usw.
# golf_app.create_account("Vorname", "Nachname", 18, username, password, False)
# ... (weitere Verarbeitung der Accounts)
