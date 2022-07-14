# -*- encoding: utf-8 -*-


def how_many_fishes_at_the_end_for_one_fish(fish_timer, days):
    fish_count_list = [0] * 9
    fish_count_list[fish_timer] = 1

    for time in range(days):
        new_count = fish_count_list[0]
        for i in range(8):
            fish_count_list[i] = fish_count_list[i + 1]

        fish_count_list[6] += new_count
        fish_count_list[8] = new_count

    return sum(fish_count_list)


def how_many_fishes_at_the_end_for_fish_list(init_fish_timers, days):
    fish_count_dict = {}
    for distinct_timer in set(init_fish_timers):
        fish_count_dict[distinct_timer] = how_many_fishes_at_the_end_for_one_fish(distinct_timer, days)

    return sum([fish_count_dict[fish_timer] for fish_timer in init_fish_timers])


if __name__ == "__main__":
    # read data
    with open("data/day6_input.txt") as f:
        data_list = f.readlines()

    fish_timers = [int(timer) for timer in data_list[0].split(",")]
    print(how_many_fishes_at_the_end_for_fish_list(fish_timers, 256))
