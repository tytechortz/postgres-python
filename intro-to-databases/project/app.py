from user import User

my_user = User.load_from_db_by_email('Terra@Turner.koshka')

print(my_user)

