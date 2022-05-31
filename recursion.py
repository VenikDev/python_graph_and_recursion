# Задание № 1
N = int(input("N = "))


def output_in_reverse_order(N):
    if N:
        print(N % 10, end=' ')
        output_in_reverse_order(N // 10)


output_in_reverse_order(N)

print()


# Задание № 2
def head(N):
    if N >= 10:
        return 10 * head(N // 10) + N % 10
    else:
        return 110 + N


print(head(N))

print()

# Задание № 3
t = str(input("t: "))
start = 0
end = len(t) - 1


def is_palindrome(start, end, text):
    if text[start] != text[end]:
        print("Nope")
    elif text[start] == text[end]:
        if start <= end:
            return is_palindrome(start + 1, end - 1, text)
        print("Yep")


is_palindrome(start, end, t)

print()

# Задание №4
n = 2

def tower_of_hanoi(n, start, add, end):
    if (n == 1):
        print('Движение диска 1: {} {}'.format(start, end))
        return
    tower_of_hanoi(n - 1, start, end, add)
    print('Движение диска {}: {} {}'.format(n, start, end))
    tower_of_hanoi(n - 1, add, start, end)


tower_of_hanoi(n, 'A', 'B', 'C')
print()
