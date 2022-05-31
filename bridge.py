# Задача №5
q = 0
time = 0

speed = []  # скорости
bridge_length = int(input("Введите длину моста: "))
number_people = int(input("Введите количество человек, переходящих мост: "))

for i in range(number_people):
    s = float(input("Скорость " + str(q) + "-го " + "="));
    q += 1
    speed.append(s)
faster = max(speed)


def bridge(n, faster, time):
    if not speed:
        return
    if n == 2:
        fast = max(speed)
        time += bridge_length / fast

        speed.remove(fast)
        fast = max(speed)

        print(speed)
        time += bridge_length / fast
        print("Общее время: " + str(time))
    else:
        time += bridge_length / faster
        speed.remove(max(speed))

        fast = max(speed)

        time += bridge_length / fast

        n -= 1
        bridge(n, faster, time)


bridge(number_people, faster, time)
