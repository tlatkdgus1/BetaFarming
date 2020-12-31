# csv에서 파싱된 데이터.
class ParsedData:
    def __init__(self, data):
        self._addr = int(data[2], 16)
        self._number = int(data[0], 10)
        # self._hash = int(data[1], 16)
        self._value = float(data[3])

    def to_string(self):
        print("['" + str(self._addr) + "', '" + str(self._number) + "', '" + str(self._value) + "']")

    def get_addr(self):
        return hex(self._addr)

    def get_ctx(self) -> []:
        return [self._number, self._value]

    def to_string(self):
        print("['" + str(self._addr) + "', '" + str(self._number) + "', '" + str(self._value) + "']")
