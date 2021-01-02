from data_manager.db import DB
from reward_calculator.reward_calc import RewardCalc

db = DB("resources/LP_history.csv")
# db.print_db()
rc = RewardCalc("reward_config.json", "lp_staking", db)
rc.simulate_loops()
rc.reward_finish()
rc.print_reward_book()


total = rc.total_reward()
print("total: " + str(total))
params = rc.get_initial_params()  # [start, end, perBlock]

expected_total = params[2] * (params[1] - params[0])
print("expected_total: " + str(expected_total))




