from data_manager.db import DB
from reward_calculator.additional_lane import AdditionLane
import json


class User:
    def __init__(self, user_addr: str):
        self.addr = user_addr
        self.balance = 0
        self.point_on_lane = 0
        self.reward = 0

    def set_lane(self, lane: float):
        self.point_on_lane = lane

    def get_lane(self):
        return self.point_on_lane


class RewardCalc:
    def __init__(self, config_file_path: str, kind: str, db: DB):
        # set configuration parameters
        self._starting_height = 0
        self._end_height = 0
        self._reward_per_block = 0

        if (kind != "lp_staking") & (kind != "bfc_staking"):
            raise Exception("'kind' must be 'lp_staking' or 'bfc_staking'")

        with open(config_file_path, "r") as json_file:
            json_obj = json.load(json_file)
            self._starting_height = json_obj["starting_block_height"]
            self._end_height = json_obj["end_block_height"]
            self._reward_per_block = json_obj[kind]["reward_per_block"]

        # set parsed raw data
        self.db = db

        # simulation context
        self.total = 0
        self.lane = AdditionLane(self._starting_height, self._reward_per_block)
        self.current_height = 0
        self.user_book = {}  # key: user addr, value: [user deposit amount, pointOnLane]
        self.reward_book = {}  # key: user addr, value: reward amount

    def simulate_loop(self):

        iter_limit = self.db.len()
        for i in range(iter_limit):
            success, ctx = self.db.pop_data()  # ctx: [addr, number, value]
            self._simulate(ctx[0], ctx[1], ctx[2])

    def _simulate(self, addr: str, number: int, value: float):
        user = self.load_user(addr)

        # update reward parameters
        self.lane.update_lane(number, self.total)

        # give reward to the user
        benefit = user.balance * (self.lane.get_lane() - user.get_lane())
        user.reward += benefit
        self.reward_book[addr] = user.reward

        # update user lane
        user.set_lane(self.lane.get_lane())

        # update deposit state
        user.balance += value
        self.total += value
        self.store_user(addr, user)

    def load_user(self, addr: str) -> User:
        if addr not in self.user_book:
            return User(addr)
        else:
            return self.user_book[addr]

    def store_user(self, addr: str, user: User):
        self.user_book[addr] = user

    def reward_finish(self):
        self.lane.update_lane(self._end_height, self.total)

        user_list = self.user_book.keys()
        for user_adder in user_list:
            user = self.user_book[user_adder]
            reward = user.balance * (self.lane.get_lane() - user.get_lane())
            user.reward += reward

    def print_reward_book(self):
        user_list = self.user_book.keys()
        for user_addr in user_list:
            user = self.user_book[user_addr]
            print("[" + user.addr + ", " + str(user.reward) +"]")

