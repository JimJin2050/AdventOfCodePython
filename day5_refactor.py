# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Segment(ABC):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    @abstractmethod
    def mark(self, marks):
        pass


class HorizontalSegment(Segment):
    def mark(self, marks):
        for x in range(min(self.start_point.x, self.end_point.x), max(self.start_point.x, self.end_point.x) + 1):
            marks[x][self.end_point.y] += 1


class VerticalSegment(Segment):
    def mark(self, marks):
        for y in range(min(self.start_point.y, self.end_point.y), max(self.start_point.y, self.end_point.y) + 1):
            marks[self.start_point.x][y] += 1


class DiagonalSegment(Segment):
    def mark(self, marks):
        x1, y1, x2, y2 = self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y
        while x1 != x2 and y1 != y2:
            marks[x1][y1] += 1
            x1 = x1 + 1 if x1 < x2 else x1 - 1
            y1 = y1 + 1 if y1 < y2 else y1 - 1
        marks[x2][y2] += 1


class SegmentFactory(object):
    @staticmethod
    def get_segment(start_point, end_point):
        if start_point.x == end_point.x:
            return VerticalSegment(start_point, end_point)
        elif start_point.y == end_point.y:
            return HorizontalSegment(start_point, end_point)
        elif abs(start_point.x - end_point.x) == abs(start_point.y - end_point.y):
            return DiagonalSegment(start_point, end_point)
        else:
            print("Invalid segment {} {}".format(start_point, end_point))


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    # read data
    with open("data/day5_input.txt") as f:
        data_list = f.readlines()

    # parse data
    segment_list = [
        [
            [
                int(line.strip().split("->")[0].strip().split(",")[0]),
                int(line.strip().split("->")[0].strip().split(",")[1])],
            [
                int(line.strip().split("->")[1].strip().split(",")[0]),
                int(line.strip().split("->")[1].strip().split(",")[1])]
        ] for line in data_list
    ]

    # implement calculation
    n = 999
    marks_part1 = [[0] * 999 for _ in range(n)]
    marks_part2 = [[0] * 999 for _ in range(n)]

    for segment in segment_list:
        start_point = Point(*segment[0])
        end_point = Point(*segment[1])
        generated_segment = SegmentFactory.get_segment(start_point, end_point)
        if not isinstance(generated_segment, DiagonalSegment):
            generated_segment.mark(marks_part1)
        generated_segment.mark(marks_part2)

    count_part1, count_part2 = 0, 0
    for row in range(n):
        for col in range(n):
            if marks_part1[row][col] >= 2:
                count_part1 += 1
            if marks_part2[row][col] >= 2:
                count_part2 += 1

    print("Part1 result: {}".format(count_part1))
    print("Part2 result: {}".format(count_part2))


#def how_many_fishes_at_the_end_for_one_fish(fish_timer, days):
    # if days - (fish_timer + 1) < 0:
    #     return 0
    # else:
    #     days -= (fish_timer + 1)
    #     return 1 + count_of_descendants_of_one_fish(6, days) + count_of_descendants_of_one_fish(8, days)
