import logging
from enum import Enum


# Enum type
class ErrorCodes(Enum):
    ERROR_CODE = "[ERROR]"


# Custom Exception
class CustomException(Exception):
    def __init__(self, msg, error_code):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return f"[ERROR] msg = {self.msg}, Code = {self.error_code}"


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age


# 커스텀 에러 발생
def create_user(username, age):
    if len(username) < 4 or age < 14:
        raise CustomException("Can't Signup", 400)

    return User(username, age)


# 에러처리를 하나의 Enum타입으로 하는 경우
def create_user_anti(username, age):
    if len(username) < 4 or age < 14:
        return ErrorCodes.ERROR_CODE

    return User(username, age)


if __name__ == '__main__':
    # anti pattern
    anti = create_user_anti("jay", 20)
    if type(anti) == ErrorCodes:
        print(anti.value + " 에러 발생")

    # try - except 로 에러 핸들링, 하지만 로그만 남음 - bad
    try:
        create_user("jay", 20)

    except Exception as e:
        print(e)

    # try - except, 로그 + 알림 + 추가 작업
    try:
        create_user("jay", 20)
    except Exception as e:
        logging.error(e) # 로그
        print("채널 알림 메시지") # 채널에 알림 보내는 작업
    finally:
        print("close 필요하면 close") # 필수 마무리 작업