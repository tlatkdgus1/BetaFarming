from data_manager.parsed_data import ParsedData


class DB:
    def __init__(self, file_path: str):
        self.db = []  # array of UserData
        with open(file_path, 'r') as reader:
            for line in reader:
                if line.split(',')[0] == "Block Number":
                    continue
                pd = ParsedData(line.split(','))
                self.db.append(pd)

    ]

    def get_user_data(self, user_addr: str) -> (bool, UserData):
        if user_addr in self.db:
            return True, self.db[user_addr]
        else:
            return False, UserData()

    def get_user_list(self):
        return self.db.keys()

    def print_db(self):
        for item in self.db.values():
            item.print_all()
