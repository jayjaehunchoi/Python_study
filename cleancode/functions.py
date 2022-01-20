class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.users = []

    def add(self, user):
        self.users.append(user)


class Email:
    def send(self, email, message):
        print(email + " 에게 \'" + message + "\' 내용으로 이메일을 전송했습니다.")


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


def create_user(email, password):
    if "@" not in email or len(password) < 6 :
        raise Exception("user is not valid")

    user = User(email, password)

    database = Database("mysql")
    database.add(user)

    email_sender = Email()
    email_sender.send(database.users[0].email, "회원 가입 완료!")


# create_user 개선
def create_user2(email, password):
    user = validate_user(email, password)
    send_email(put_database(user))


def validate_user(email, password):
    if "@" not in email or len(password) < 6 :
        raise Exception("user is not valid")

    return User(email, password)


def put_database(user):
    database = Database("mysql")
    database.add(user)
    return database


def send_email(database):
    email_sender = Email()
    email_sender.send(database.users[0].email, "회원 가입2 완료!")


if __name__ == '__main__':
    create_user("wogns0108@naver.com", "12345678")

    create_user2("wogns0108@naver.com", "12345678")

    # create_user("wo", "1234567") # 검증에서 에러

    # create_user("wogns0108@naver.com", "123") # 검증에서 에러