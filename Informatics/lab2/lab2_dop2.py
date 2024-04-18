class Hamming:
    encoded_size = 7
    msg_size = 4
    s_arr = []

    def __init__(self, a, b):
        self.encoded_size = a
        self.msg_size = b
        i = 1
        while i < self.encoded_size:
            self.s_arr.append(i)
            i *= 2

    def decode(self, msg):
        msg = [int(x) for x in msg]
        s = 0
        for check_bit in self.s_arr:
            now_s = 0
            for i in range(check_bit - 1, self.encoded_size, check_bit * 2):
                for j in range(i, i + check_bit):
                    now_s ^= msg[j]
            s += check_bit * now_s
        if s == 0:
            print("Нет ошибок")
        else:
            msg[s - 1] += 1
            msg[s - 1] %= 2
            print(f"Ошибка в символе номер {s}")

        print("Переданное сообщение: ") 
        i = 1
        for j in range(self.encoded_size): 
            if j == i-1:
                i*=2
                continue
            print(msg[j], end="")
        return s == 0


if __name__ == "__main__":
    from sys import argv

    assert len(argv) > 1, "подайте сообщение аргументом :(. Пример python hamming.py 1011011"

    h = Hamming(7, 4)
    h.decode(argv[1])
