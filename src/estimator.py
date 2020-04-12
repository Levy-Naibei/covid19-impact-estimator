"""Novel covid-19 impact estimator program"""
def estimator(data):
    """function to estimate covid-19 impact"""

    # pylint: disable = line-too-long
    impact = {}  # your best case estimation
    severe_impact = {}  # your severe case estimation

    if data['periodType'] == 'days':
        time_to_elapse = data['timeToElapse']
    elif data['periodType'] == 'weeks':
        time_to_elapse = data['timeToElapse'] * 7
    elif data['periodType'] == 'months':
        time_to_elapse = data['timeToElapse'] * 30

    time_to_elapse = 2 ** (int(time_to_elapse/ 3))
    total_hospital_beds = data['totalHospitalBeds'] * 0.35
    daily_income = data['region']['avgDailyIncomeInUSD']

    # challenge-1
    # currentlyInfected
    impact['currentlyInfected'] = int(data['reportedCases'] * 10)
    severe_impact['currentlyInfected'] = int(data['reportedCases'] * 50)

    # infectionsByRequestedTime
    impact['infectionsByRequestedTime'] = int(impact['currentlyInfected'] * time_to_elapse)
    severe_impact['infectionsByRequestedTime'] = int(severe_impact['currentlyInfected'] * time_to_elapse)

    # challenge-2
    # severeCasesByRequestedTime
    impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
    severe_impact['severeCasesByRequestedTime'] = int(0.15 * severe_impact['infectionsByRequestedTime'])

    # total_hospital_beds for covid positive patients
    impact['hospitalBedsByRequestedTime'] = int(total_hospital_beds - impact['severeCasesByRequestedTime'])
    severe_impact['hospitalBedsByRequestedTime'] = int(total_hospital_beds - severe_impact['severeCasesByRequestedTime'])

    # challenge-3
    # casesForICUByRequestedTime
    impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
    severe_impact['casesForICUByRequestedTime'] = int(0.05 * severe_impact['infectionsByRequestedTime'])

    # casesForVentilatorsByRequestedTime
    impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
    severe_impact['casesForVentilatorsByRequestedTime'] = int(0.02 * severe_impact['infectionsByRequestedTime'])

    # dollarsInFlight
    impact['dollarsInFlight'] = int((impact['infectionsByRequestedTime'] * data['population'] * daily_income) / time_to_elapse)
    severe_impact['dollarsInFlight'] = int((severe_impact['infectionsByRequestedTime'] * data['population'] * daily_income) / time_to_elapse)

    output = {
        "data": data,
        "impact": impact,
        "severeImpact": severe_impact
    }

    return output
