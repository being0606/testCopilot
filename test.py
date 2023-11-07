def great(name):
    print('Hello', name)
    """인사메시지를 출력합니다."""

if __name__ == '__main__':
    great('world')
    great('Gumby')
    print(great.__doc__)