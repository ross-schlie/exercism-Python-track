"""exercism two bucket module."""


def measure(bucket_one, bucket_two, goal, start_bucket):
    """
    Measure an exact number of liters by strategically transferring liters of fluid between the buckets.

    :param bucket_one int - the (max) size of bucket one
    :param bucket_two int - the (max) size of bucket two
    :param bucket_one int - the desired number of liters to reach
    :param start_bucket string - which bucket to fill first, either bucket one or bucket two

    :return tuple -
        - the total number of "moves" it should take to reach the desired number of liters, including the first fill
        - which bucket should end up with the desired number of liters (let's say this is bucket A) - either bucket one or bucket two
        - how many liters are left in the other bucket (bucket B)
    """

    bucket_reached_goal = None
    other_bucket = None
    bucket_ab_one_contents = 0
    bucket_ab_two_contents = 0
    bucket_ba_one_contents = 0
    bucket_ba_two_contents = 0
    goal_reached = False

    if start_bucket == "one":
        bucket_ab_one_contents = bucket_one
        bucket_ba_one_contents = bucket_one
    else:
        bucket_ab_two_contents = bucket_two
        bucket_ba_two_contents = bucket_two

    steps = 0
    while not goal_reached:
        steps += 1
        # Check to see if goal has been reached
        if bucket_ab_one_contents == goal or bucket_ba_one_contents == goal:
            goal_reached = True
            bucket_reached_goal = "one"
            if bucket_ab_one_contents == goal:
                other_bucket = bucket_ab_two_contents
            else:
                other_bucket = bucket_ba_two_contents

        elif bucket_ab_two_contents == goal or bucket_ba_two_contents == goal:
            goal_reached = True
            bucket_reached_goal = "two"
            if bucket_ab_two_contents == goal:
                other_bucket = bucket_ab_one_contents
            else:
                other_bucket = bucket_ba_one_contents

        else: # Process next 'step'
            #  NOT allowed at any point to have the smaller bucket full and the larger bucket empty
            # (opposite of start conditions) - if it reaches such a condition, stop processing it
            if start_bucket == "two" and bucket_ab_one_contents == bucket_one and bucket_ab_two_contents == 0:
                pass
            else:
                bucket_ab_one_contents, bucket_ab_two_contents = bucket_fill(bucket_one, bucket_ab_one_contents, bucket_two, bucket_ab_two_contents)

            if start_bucket == "one" and bucket_ba_one_contents == 0 and bucket_ba_two_contents == bucket_two:
                pass
            else:
                bucket_ba_two_contents, bucket_ba_one_contents  = bucket_fill(bucket_two, bucket_ba_two_contents, bucket_one, bucket_ba_one_contents)

    return (steps, bucket_reached_goal, other_bucket)

def bucket_fill(bucket_a_capacity, bucket_a_contents, bucket_b_capacity, bucket_b_contents):
    """
    Perform a step in the measure bucket process and return the contents of each bucket.

    :param bucket_a_capacity int - The maximum amount of fluid bucket A can have.
    :param bucket_a_contents int - The amount of fluid in bucket A.
    :param bucket_b_capacity int - The maximum amount of fluid bucket B can have.
    :param bucket_b_contents int - The amount of fluid in bucket B.
    :return tuple (bucket_a_contents, bucket_b_contents) The amount of fluid in buckets A and B.

    The only valid moves are:
    - pouring from either bucket to another (A -> B)
    - emptying either bucket and doing nothing to the other
    - filling either bucket and doing nothing to the other (Fill A)

    NOT allowed at any point to have the smaller bucket full and the larger bucket empty
        (opposite of start conditions)
    """

    if bucket_a_contents == 0: # 1. If A is empty, fill it
        bucket_a_contents = bucket_a_capacity
    elif bucket_b_contents == bucket_b_capacity: #2. If B is full, empty it
        bucket_b_contents = 0
    else: # Pour contents of A to B
        fluid_b_can_accept = bucket_b_capacity - bucket_b_contents
        if fluid_b_can_accept > bucket_a_contents: # All of A poured into B
            bucket_b_contents += bucket_a_contents
            bucket_a_contents = 0
        else: # Pour what is possible from A to B
            bucket_b_contents += fluid_b_can_accept
            bucket_a_contents -= fluid_b_can_accept

    return (bucket_a_contents, bucket_b_contents)

def analyze_solutions():
    # A of size 3, B of size 5, A filled first, goal = 1
    # 1 3/3, 0/5    Fill A
    # 2 0/3, 3/5    A -> B
    # 3 3/3, 3/5    Fill A
    # 4 1/3. 5/5    A -> B (A meets goal)

    # A of size 3, B of size 5, B filled first, goal = 1 (inverted)
    # 1 0/3, 5/5    Fill B
    # 2 3/3, 2/5    B -> A
    # 3 0/3, 2/5    Empty A
    # 4 2/3, 0/5    B -> A
    # 5 2/3. 5/5    Fill B
    # 6 3/3. 4/5    B -> A
    # 7 0/3, 4/5    Empty A
    # 8 3/3, 1/5    B -> A  (A meets goal)

    # xxxxxxxxxxxxxx
    # A of size 3, B of size 5, B filled first, goal = 1 (inverted)
    # 1 0/3, 5/5    Fill B xxxx
    # 2 3/3, 5/5    Fill A
    # 3 3/3, 0/5    Empty B = Fail
    # 4 0/3, 0/5
    # 5 0/3. 0/5
    # 6 0/3. 0/5
    # 7 0/3, 0/5
    # 8 0/3, 0/5

    # A of size 7, B of size 11, A filled first, goal = 2
    # 1 7/7 0/11    Fill A
    # 2 0/7 7/11    A -> B
    # 3 7/7 7/11    Fill A
    # 4 3/7 11/11   A -> B
    # 5 3/7 0/11    Empty B
    # 6 0/7 3/11    A -> B
    # 7 7/7 3/11    Fill A
    # 8 0/7 10/11   A -> B
    # 9 7/7 10/11   Fill A
    # 10 6/7 11/11  A -> B
    # 11 6/7 0/11   Empty B
    # 12 0/7 6/11   A -> B
    # 13 7/7 6/11   Fill A
    # 14 2/7 11/11  A -> B (A meets goal)

    # A of size 7, B of size 11, B filled first, goal = 2 (inverted)
    # 1 0/7 11/11   Fill B
    # 2 7/7 4/11    B -> A
    # 3 0/7 4/11    Empty A
    # 4 4/7 0/11    B -> A
    # 5 4/7 11/11   Fill B
    # 6 7/7 8/11    B -> A
    # 7 0/7 8/11    Empty A
    # 8 7/7 1/11    B -> A
    # 9 0/7 1/11    Empty A
    # 10 1/7 0/11   B -> A
    # 11 1/7 11/11  Fill B
    # 12 7/7 5/11   B -> A
    # 13 0/7 5/11   Empty A
    # 14 5/7 0/11   B -> A
    # 15 5/7 11/11  Fill B
    # 16 7/7 9/11   B -> A
    # 17 0/7 9/11   Empty A
    # 18 77 2/11    B -> A (B meets goal)
    pass
