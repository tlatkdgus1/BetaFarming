class TotalDB:
    def __init__(self, file_path: str):
        self.db = []
        self.reward_total = 0
        with open(file_path, 'r') as reader:
            for line in reader:
                if (line.split(',')[0] == "Block Number") | (line.split(',')[0] == "Address"):
                    continue
                self.reward_total += float(line.split(',')[2])

    def get_total_reward(self):
        return self.reward_total / 10**18
