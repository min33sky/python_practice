# 문자열 줄바꿈 기준으로 나누기

def split_lines(s: str):
  return s.split('\n')

print(split_lines('This\nis a\nmultiline\nstring.\n'))