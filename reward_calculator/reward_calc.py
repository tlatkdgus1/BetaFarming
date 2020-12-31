from data_manager.db import DB
import json


class RewardCalc:
    def __init__(self, config_file_path: str, kind: str, db: DB):

        if (kind != "lp_staking") & (kind != "bfc_staking"):
            raise Exception("'kind' must be 'lp_staking' or 'bfc_staking'")

        self.starting_height = 0
        self.end_height = 0
        self.reward_per_block = 0

        with open(config_file_path, "r") as json_file:
            json_obj = json.load(json_file)
            self.starting_height = json_obj["starting_block_height"]
            self.end_height = json_obj["end_block_height"]
            self.reward_per_block = json_obj[kind]["reward_per_block"]

        self.db = db
        self.report = {}

    def reward_calculate(self):
        users = self.db.get_user_list()

        for user in users:
            self.calc_user_reward(user)

    def calc_user_reward(self, user_addr: str):
        success, user_data = self.db.get_user_data(user_addr)
        if not success:
            raise Exception("Wrong Data")

        success, prev = user_data.pop()
        while success:
            success, cur = user_data.pop()
            if success:
                delta = cur[0] - prev[0]
                self.reward_per_block * delta






            prev = data




