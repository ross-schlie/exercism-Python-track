"""exercism bowling module."""


class BowlingGame:

    def __init__(self):
        self.frame_index = 0
        self.current_frame = []
        self.frame_points = [[]] * 10

        self.fill_balls = 1

        self.times_rolled_in_last_frame = 0
        self.last_frame_pins_left = 10

    def __next_frame(self):
        self.frame_index += 1
        if sum(self.current_frame) == 10:
            self.fill_balls += 1

        self.current_frame = []

    def roll(self, pins):
        if pins < 0:
            raise Exception("Cannot score negative points")
        elif pins > 10:
            raise Exception("Cannot score more than 10 points")

        if self.frame_index < 9:
            # Process frame (open frame, spare or strike)
            if len(self.current_frame) == 0 and pins < 10: # open frame
                self.current_frame.append(pins)
            else:
                self.current_frame.append(pins)
                if sum(self.current_frame) > 10:
                    raise Exception("Cannot score more than 10 points in a frame.")

                self.frame_points[self.frame_index] = self.current_frame
                self.__next_frame()
        else:
            self.__process_last_frame(pins)

    def __process_last_frame(self, pins):
        if self.fill_balls == 0:
            raise Exception("Cannot continue to roll in last frame when out of fill balls.")

        self.current_frame.append(pins)
        self.frame_points[self.frame_index] = self.current_frame

        self.last_frame_pins_left -= pins
        if self.last_frame_pins_left < 0:
            raise Exception("Cannot knock down more than 10 pins.")

        if self.last_frame_pins_left == 0:
            # spare or strike
            self.times_rolled_in_last_frame = 0
            self.last_frame_pins_left = 10
            # don't count fill balls as used if it's a strike on first roll or spare on 2nd
            if len(self.current_frame) > 2:
                self.fill_balls -= 1

        else:
            # open frame
            if self.times_rolled_in_last_frame == 1: # second roll (not a spare)
                self.times_rolled_in_last_frame = 0
                self.fill_balls -= 1
            else: # first roll
                self.times_rolled_in_last_frame = 1
                if len(self.current_frame) > 2 and self.fill_balls == 1:
                    self.fill_balls -= 1


    def score(self):
        points = 0
        for index, points_in_frame in enumerate(self.frame_points):
            if index < 10:
                # first add the points from pins
                points += sum(points_in_frame)
                # for strikes and spares, look ahead
                if sum(points_in_frame) == 10 and len(points_in_frame) == 2: # spare
                    next_frame = self.frame_points[index + 1]
                    points += next_frame[0]
                if sum(points_in_frame) == 10 and len(points_in_frame) == 1: # strike
                    next_frame = self.frame_points[index + 1]
                    # if this is also a strike
                    if len(next_frame) == 1:
                        # case won't occur when this is the last frame anyway
                        next_next_frame = self.frame_points[index + 2]
                        points += next_frame[0] + next_next_frame[0]
                    else:
                        # It should not be possible for it to have more.. but..
                        points += next_frame[0] + next_frame[1]
            else:
                # 10th frame is straight number of pins
                points += sum(points_in_frame)

        return points
