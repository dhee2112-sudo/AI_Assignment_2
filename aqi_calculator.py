BREAKPOINTS = {
    "PM2.5": [(0, 50, 0, 30),
              (51, 100, 31, 60),
              (101, 200, 61, 90),
              (201, 300, 91, 120),
              (301, 400, 121, 250)],

    "PM10": [(0, 50, 0, 50),
             (51, 100, 51, 100),
             (101, 200, 101, 250),
             (201, 300, 251, 350)],

    "NO2": [(0, 50, 0, 40),
            (51, 100, 41, 80),
            (101, 200, 81, 180)],

    "CO": [(0, 50, 0, 1),
           (51, 100, 1.1, 2),
           (101, 200, 2.1, 10)]
}


def calculate_individual_aqi(pollutant, concentration):
    if pollutant not in BREAKPOINTS:
        return None

    for (i_low, i_high, bp_low, bp_high) in BREAKPOINTS[pollutant]:
        if bp_low <= concentration <= bp_high:
            aqi = ((i_high - i_low) / (bp_high - bp_low)) * \
                  (concentration - bp_low) + i_low
            return round(aqi)

    return None


def get_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"