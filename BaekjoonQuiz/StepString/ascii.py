import string

ascii_code = {"A": 65, "a": 97, "0": 48}
lower = {b: a for a, b in enumerate(string.ascii_lowercase)}
upper = {b: a for a, b in enumerate(string.ascii_uppercase)}

typed = input()

if typed in lower:
    print(ascii_code["a"] + lower[typed])

elif typed in upper:
    print(ascii_code["A"] + upper[typed])

else:
    print(ascii_code["0"] + int(typed))

# ord(string) 함수 사용 시 string을 유니코드 int로 반환하는데 ascii 코드와 알파벳, 숫자 순서는 같음
# chr(int) 함수 사용 시 숫자를 유니코드 숫자 위치를 string으로 반환해줌.