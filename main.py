from data_manager.db import DB
from reward_calculator.reward_calc import RewardCalc

db = DB("resources/LP_summary.csv")
# db.print_db()
rc = RewardCalc("reward_config.json", "lp_staking", db)
rc.simulate_loop()
rc.reward_finish()
rc.print_reward_book()