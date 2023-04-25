from db import Database

class PhoneNumber:
    def __init__(self, user_id, phone_number):
        self.user_id = user_id
        self.phone_number = phone_number

    def save(self):
        with Database() as db:
            db.execute(
                "INSERT INTO phone_numbers (user_id, phone_number) VALUES (%s, %s)",
                (self.user_id, self.phone_number)
            )

    @staticmethod
    def get_all_by_user_id(user_id):
        with Database() as db:
            results = db.query("SELECT * FROM phone_numbers WHERE user_id = %s", (user_id,))
            return results

    def delete(self):
        with Database() as db:
            db.execute("DELETE FROM phone_numbers WHERE id = %s", (self.id,))
