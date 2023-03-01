class Carro():
    vel_atual = 0
    vel_min = 0

    def __init__(self, vel_max):
        self.vel_max = vel_max

    def acelerar(self, delta=5):
        if self.vel_atual < self.vel_max:
            if delta + self.vel_atual > self.vel_max:
                self.vel_atual += self.vel_max - self.vel_atual
            else:
                self.vel_atual += delta

    def frear(self, delta=5):
        if self.vel_atual > self.vel_min:
            if self.vel_atual - delta < self.vel_min:
                self.vel_atual -= self.vel_min + self.vel_atual
            else:
                self.vel_atual -= delta



if __name__ == '__main__':
    c1 = Carro(200)
    print(c1.vel_atual)

    for _ in range(25):
        c1.acelerar(10)
        print(c1.vel_atual)

    for _ in range(10):
        c1.frear(delta=30)
        print(c1.vel_atual)
