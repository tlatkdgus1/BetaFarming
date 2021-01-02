class AdditionLane:
    def __init__(self, starting_height: int, rewards_per_block: float):
        self._lane = 0
        self._rewards_per_block = rewards_per_block
        self._latest_block = 0
        self._reward_start_height = starting_height

    def update_lane(self, current_block: int, total: float):

        if self._latest_block == current_block:
            return

        if not self._latest_block < current_block:
            raise Exception("Current height(" + str(current_block) + ") must be bigger than latest height("
                            + str(self._latest_block) + ")")

        delta = 0
        if self._reward_start_height > current_block:
            self._latest_block = current_block
            return
        else:
            if self._reward_start_height > self._latest_block:
                delta = current_block - self._reward_start_height
            else:
                delta = current_block - self._latest_block

        if total != 0:
            self._lane += self._rewards_per_block * delta / total
        self._latest_block = current_block

    def set_reward_per_block(self, current_block: int, total: int, rewards_per_block: int):
        self.update_lane(current_block, total)
        self._rewards_per_block = rewards_per_block

    def get_lane(self):
        return self._lane

    def get_rewards_per_block(self):
        return self._rewards_per_block
