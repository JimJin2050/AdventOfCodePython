# -*- coding: utf-8 -*-


class Velocity(object):

    def __init__(self, initial_x_velocity, initial_y_velocity):
        self.x_velocity = initial_x_velocity
        self.y_velocity = initial_y_velocity

    def next_velocity(self):
        if self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.x_velocity += 1
        else:
            pass

        self.y_velocity -= 1


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Probe(object):
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.target_area = None

    def set_target_area(self, target_rectangle):
        self.target_area = target_rectangle

    def is_target_area_reached(self):
        if all([
            self.target_area[0].x <= self.position.x <= self.target_area[1].x,
            self.target_area[1].y <= self.position.y <= self.target_area[0].y
        ]):
            return True
        else:
            return False

    def launch(self):
        max_y = -1
        if self.target_area:
            while all([
                self.position.x <= self.target_area[1].x,
                self.position.y >= self.target_area[1].y
            ]):
                self.position.x += self.velocity.x_velocity
                self.position.y += self.velocity.y_velocity

                max_y = max(max_y, self.position.y)
                if self.is_target_area_reached():
                    return True, max_y

                self.velocity.next_velocity()

            return False, -1
        else:
            raise ValueError("The target area is still not set!")


def main():
    # read data
    with open("data/day17_input.txt") as f:
        data_list = f.readlines()

    # parse data
    x_scope, y_scope = data_list[0].strip().split(":")[1].strip().split(",")
    start_x, end_x = list(map(int, x_scope.split("=")[1].split("..")))
    end_y, start_y = list(map(int, y_scope.split("=")[1].split("..")))

    # process probe launch
    maximum_y, velocity_amount = 0, 0

    for x_velocity in range(end_x + 1):
        if end_y < 0:
            y_range = range(end_y - 1, -end_y + 1)
        else:
            y_range = range(end_y + 1)
        for y_velocity in y_range:
            temp_velocity = Velocity(x_velocity, y_velocity)
            probe = Probe(Position(0, 0), temp_velocity)
            probe.set_target_area((Position(start_x, start_y), Position(end_x, end_y)))

            target_area_reached, highest_y = probe.launch()
            if target_area_reached:
                maximum_y = max(maximum_y, highest_y)
                velocity_amount += 1

    # Answer of part 1
    print("What is the highest y position it reaches on this trajectory: {}".format(maximum_y))

    # Answer of part 2
    print("Count of the velocity of probe which reaches target: {}".format(velocity_amount))


if __name__ == "__main__":
    main()
