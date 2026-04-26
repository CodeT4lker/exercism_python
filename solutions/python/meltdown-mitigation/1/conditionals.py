"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500  and temperature * neutrons_emitted < 500000:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ''
    generated_power = voltage * current
    efficiency_value = generated_power / theoretical_max_power * 100
    if efficiency_value >= 80:
        efficiency = 'green'
    elif efficiency_value >= 60:
        efficiency = 'orange'
    elif efficiency_value >= 30:
        efficiency = 'red'
    else:
        efficiency = 'black'
    return efficiency

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    category = ''
    value = temperature * neutrons_produced_per_second
    if value < threshold * 0.9:
        category = 'LOW'
    elif value <= threshold * 1.1:
        category = 'NORMAL'
    else:
        category = 'DANGER'
    return category
