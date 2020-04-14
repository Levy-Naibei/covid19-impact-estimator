"""Novel covid-19 impact estimator program"""

def estimator(data):
    """Takes input data and returns a response in a given format"""

    impact = {}  # best case estimation
    severe_impact = {}  # your severe case estimation

    # Normalizes periods given to days
    if data['periodType'] == 'days':
        time_to_elapse = data['timeToElapse']
    elif data['periodType'] == 'weeks':
        time_to_elapse = data['timeToElapse'] * 7
    elif data['periodType'] == 'months':
        time_to_elapse = data['timeToElapse'] * 30

    time_elapse = 2 ** (int(time_to_elapse/ 3))
    total_hospital_beds = data['totalHospitalBeds'] * 0.35
    daily_income = data['region']['avgDailyIncomeInUSD']
    popl = data['region']['avgDailyIncomePopulation']

    # challenge-1
    # currently Infected
    impact['currentlyInfected'] = int(data['reportedCases'] * 10)
    severe_impact['currentlyInfected'] = int(data['reportedCases'] * 50)

    # Projected infections after a specified time
    impact['infectionsByRequestedTime'] = \
        int(impact['currentlyInfected'] * time_elapse)
    severe_impact['infectionsByRequestedTime'] = \
        int(severe_impact['currentlyInfected'] * time_elapse)

    # challenge-2
    # Severe positive cases that can recover when hospitalized
    impact['severeCasesByRequestedTime'] = \
        int(0.15 * impact['infectionsByRequestedTime'])
    severe_impact['severeCasesByRequestedTime'] = \
        int(0.15 * severe_impact['infectionsByRequestedTime'])

    # Available beds for covid-19 positive patients
    impact['hospitalBedsByRequestedTime'] = \
        int(total_hospital_beds - impact['severeCasesByRequestedTime'])
    severe_impact['hospitalBedsByRequestedTime'] = \
        int(total_hospital_beds - severe_impact['severeCasesByRequestedTime'])

    # challenge-3
    # ICU cases after a given time
    impact['casesForICUByRequestedTime'] = \
        int(0.05 * impact['infectionsByRequestedTime'])
    severe_impact['casesForICUByRequestedTime'] = \
        int(0.05 * severe_impact['infectionsByRequestedTime'])

    # Cases that require ventilators
    impact['casesForVentilatorsByRequestedTime'] = \
        int(0.02 * impact['infectionsByRequestedTime'])
    severe_impact['casesForVentilatorsByRequestedTime'] = \
        int(0.02 * severe_impact['infectionsByRequestedTime'])

    # Money in dollars to be lost daily
    impact['dollarsInFlight'] = \
        int((impact['infectionsByRequestedTime'] * popl * daily_income) / time_to_elapse)
    severe_impact['dollarsInFlight'] = \
        int((severe_impact['infectionsByRequestedTime'] * popl * daily_income) / time_to_elapse)

    output = {
        "data": data,
        "impact": impact,
        "severeImpact": severe_impact
    }

    return output
