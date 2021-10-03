"""exercism meltdown mitigation module."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    is_critical = False
    MAX_TEMPERATURE_NEUTRONS_PRODUCT = 500000
    if temperature < 800 and neutrons_emitted > 500:
        if temperature * neutrons_emitted < MAX_TEMPERATURE_NEUTRONS_PRODUCT:
            is_critical = True

    return is_critical


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = int((generated_power/ theoretical_max_power) * 100)
    efficiency_level = 'black'
    if efficiency >= 80:
        efficiency_level = 'green'
    elif efficiency >= 60:
        efficiency_level = 'orange'
    elif efficiency >= 30:
        efficiency_level = 'red'

    return efficiency_level


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return safety range.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    status_code = 'DANGER'
    LOW_THRESHOLD = threshold * 0.40
    NORMAL_THRESHOLD_MIN = threshold * 0.90
    NORMAL_THRESHOLD_MAX = threshold * 1.10
    output = temperature * neutrons_produced_per_second
    if output < LOW_THRESHOLD:
        status_code = 'LOW'
    elif output > NORMAL_THRESHOLD_MIN and output < NORMAL_THRESHOLD_MAX:
        status_code = 'NORMAL'

    return status_code
