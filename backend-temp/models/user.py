from db import Database

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        with Database() as db:
            db.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (self.name, self.email, self.password)
            )

    @staticmethod
    def get_all():
        with Database() as db:
            results = db.query("SELECT * FROM users")
            return results

    @staticmethod
    def get_by_id(user_id):
        with Database() as db:
            results = db.query("SELECT * FROM users WHERE id = %s", (user_id,))
            if results:
                return results[0]
            return None

    def update(self):
        with Database() as db:
            db.execute(
                "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s",
                (self.name, self.email, self.password, self.id)
            )

    def delete(self):
        with Database() as db:
            db.execute("DELETE FROM users WHERE id = %s", (self.id,))
