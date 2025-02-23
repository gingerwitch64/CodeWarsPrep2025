import sys
string: str = sys.stdin.read().rstrip()
output: str = ""

for ch in string:
    ascii_code: int = ord(ch)
    top_digit: int    = ascii_code // 36
    middle_digit: int = (ascii_code - (top_digit * 36)) // 6
    bottom_digit: int = (ascii_code - (top_digit * 36) - (middle_digit * 6)) // 1
    output = output + f"{top_digit}{middle_digit}{bottom_digit}"
print(output)
