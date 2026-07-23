# Rocket Analyzer A-Series
# Physics Engine 🚀

G = 9.81


def calculate_thrust(dry_mass, fuel_mass, height, time):
    """
    Розрахунок середньої тяги ракети

    dry_mass  - суха маса (г)
    fuel_mass - маса палива (г)
    height    - висота (м)
    time      - час підйому (с)
    """

    # Загальна маса ракети в кг
    mass = (dry_mass + fuel_mass) / 1000


    # Прискорення
    acceleration = (2 * height) / (time ** 2)


    # Сила для прискорення
    acceleration_force = mass * acceleration


    # Сила тяжіння
    gravity_force = mass * G


    # Середня тяга двигуна
    thrust = acceleration_force + gravity_force


    # Переведення у кгс
    thrust_kg = thrust / G


    # Співвідношення тяги до маси
    twr = thrust_kg / mass


    return {
        "mass": mass,
        "acceleration": acceleration,
        "acceleration_force": acceleration_force,
        "gravity_force": gravity_force,
        "thrust_N": thrust,
        "thrust_kg": thrust_kg,
        "twr": twr
    }