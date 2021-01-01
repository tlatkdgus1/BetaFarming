class ParsedData:
    def __init__(self, data):
        self.addr = int(data[2], 16)
        self.number = int(data[0], 10)
        # self._hash = int(data[1], 16)
        self.value = float(data[3])

    def to_string(self):
        return "['" + hex(self.addr) + "', '" + str(self.number) + "', '" + str(self.value) + "']"

    def get_addr(self):
        return hex(self.addr)

    def get_ctx(self) -> list:
        return [hex(self.addr), self.number, self.value]


class DB:
    def __init__(self, file_path: str):
        self.db = []  # array of UserData
        with open(file_path, 'r') as reader:
            for line in reader:
                if (line.split(',')[0] == "Block Number") | (line.split(',')[0] == "Address"):
                    continue
                pd = ParsedData(line.split(','))
                self.insert_data(pd)

    def pop_data(self) -> (bool, list):
        if len(self.db) > 0:
            return True, self.db.pop(0)
        else:
            return False, []

    def insert_data(self, data: ParsedData):
        self.sanity_check(data)
        self.db.append(data.get_ctx())

    def sanity_check(self, data: ParsedData) -> bool:
        db_size = len(self.db)
        if db_size != 0:
            prev = self.db[len(self.db) - 1]
            if prev[1] > data.number:
                raise Exception("Block number must be bigger than previous one")
        return True

    def len(self):
        return len(self.db)

    def print_db(self):
        for item in self.db:
            print("['" + item[0] + "', '" + str(item[1]) + "', '" + str(item[2]) + "']")

