from data_manager.db import DB
from reward_calculator.reward_calc import RewardCalc

db = DB("resources/LP - 11557079.csv")
# db.print_db()
rc = RewardCalc("reward_config.json", "lp_staking", db)
