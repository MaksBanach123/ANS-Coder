class AnsDecoder:

    def __init__(self):
        self.r = 18
        self.n = 18
        self.mask = pow(2, self.n)-1

    def find_s(self, CDF, y):
        # szukamy s takiego, że:
        # CDF[s]<= y <CDF[s+1]
        for s in range(len(CDF) - 1):
            if CDF[s] <= y < CDF[s + 1]:
                return s
        print("No suitable s found for the given y.")

    def decode(self, x, f, CDF, stream):
        s = self.find_s(CDF, x & self.mask)
        x = int(f[s] * (x >> self.n) + (x & self.mask) - CDF[s])

        while x < pow(2, self.r) and stream:  # przesun o 1 w lewo, dodaj bit ze strumienia, usun go ze strumienia
            x <<= 1
            bit_to_add = stream[-1]
            x = x + int(bit_to_add, 2)
            stream.pop()
        return x, s, stream
