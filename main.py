from data_manager.summary_parser import SummaryDB
from reward_calculator.reward_calc import RewardCalc
from data_manager.total_parser import TotalDB

db = SummaryDB("resources/LP_history.csv")
# db.print_db()
rc = RewardCalc("reward_config.json", "lp_staking", db)
rc.simulate_loops()
rc.reward_finish()
rc.print_reward_book()


print("==Validation==")
total = rc.total_reward()
print(" - total: " + str(total))

params = rc.get_initial_params()  # [start, end, perBlock]
expected_total = params[2] * (params[1] - params[0])
print(" - expected_total: " + str(expected_total))

print("== Sum of all rewards in total file ==")
tr = TotalDB("resources/LP - 11572613.csv")
print(" - parsed_total: " + str(tr.get_total_reward()))



