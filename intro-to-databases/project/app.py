from user import User

my_user = User('rex@terra.com', 'Rex', 'Smith', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('Terra@Turner.koshka')

print(user_from_db)

my_user.save_to_db()

