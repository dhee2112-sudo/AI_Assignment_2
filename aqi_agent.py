# aqi_agent.py

from aqi_calculator import calculate_individual_aqi, get_category


def read_sensor_data(file_name):
    pollutants = {}

    with open(file_name, "r") as f:
        for line in f:
            name, value = line.strip().split(":")
            pollutants[name.strip()] = float(value.strip())

    return pollutants


def aqi_agent(file_name):
    data = read_sensor_data(file_name)

    print("---- Individual AQI Values ----")

    overall_aqi = 0
    dominant_pollutant = None

    for pollutant, concentration in data.items():
        aqi = calculate_individual_aqi(pollutant, concentration)

        if aqi is not None:
            print(f"{pollutant} → AQI: {aqi}")

            if aqi > overall_aqi:
                overall_aqi = aqi
                dominant_pollutant = pollutant

    category = get_category(overall_aqi)

    print("\n---- Overall AQI ----")
    print("Dominant Pollutant:", dominant_pollutant)
    print("Overall AQI:", overall_aqi)
    print("Category:", category)


if __name__ == "__main__":
    aqi_agent("aqi_data.txt")