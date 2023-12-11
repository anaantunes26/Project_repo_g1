class GolfApp:
    def __init__(self):
        self.accounts = []
        self.courses = []

    def load_accounts(self):
        # Muster-Accounts
        self.accounts = [
            {"Benutzername": "casual_golfer123", "E-Mail": "casualgolfer123@example.com", "Passwort": "Golfer123!", "Mitgliedschaft": "Basic"},
            {"Benutzername": "golf_enthusiast45", "E-Mail": "golfenthusiast45@example.com", "Passwort": "GreenSwing45@", "Mitgliedschaft": "Premium"},
            {"Benutzername": "pro_golfer89", "E-Mail": "progolfer89@example.com", "Passwort": "ProPassion89$", "Mitgliedschaft": "Elite"}
        ]

    def load_courses(self):
        # Golfplätze in der Schweiz
        self.courses = [
            {"Name": "Swiss Alps Golf Club", "Ort": "Crans-Montana", "Beschreibung": "Ein atemberaubender Golfplatz in den Schweizer Alpen mit Panoramablicken und anspruchsvollen Löchern."},
            {"Name": "Lake Geneva Golf Resort", "Ort": "Genf", "Beschreibung": "Ein exklusiver Golfplatz am Genfer See mit Blick auf das Wasser und eine perfekte Kombination aus Herausforderung und Schönheit."},
            {"Name": "Zurich Valley Golf Club", "Ort": "Zürich", "Beschreibung": "Ein moderner Golfplatz in der Nähe von Zürich, der eine erstklassige Spielumgebung mit hochwertigen Einrichtungen bietet."}
        ]

    def get_accounts(self):
        return self.accounts

    def get_courses(self):
        return self.courses

# Beispiel, wie die GolfApp verwendet werden könnte:
# golf_app = GolfApp()
# golf_app.load_accounts()
# golf_app.load_courses()
# accounts = golf_app.get_accounts()
# courses = golf_app.get_courses()
# ... (weitere Verarbeitung der geladenen Daten)
