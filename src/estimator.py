import math

def estimator():
    """covid-19 impact estimator"""
    # pylint: disable=unused-variable
    # pylint: disable=pointless-string-statement

    # pylint: disable = undefined-variable

    data = {
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeInUSD": 3,
            "avgDailyIncomePopulation": 0.77
        },
        "periodType": "days",
        "timeToElapse": 60,
        "reportedCases": 45,
        "population": 1456011609,
        "totalHospitalBeds": 1000
    }

    # challenge-1
    """ estimate currently infected """
    currently_infected_impact = int(data['reportedCases'] * 10)
    currently_infected_severe = int(data['reportedCases'] * 50)

    """ estimate projected infections """
    infections_by_requested_time_impact = currently_infected_impact * 2**20
    infections_by_requested_time_severe = currently_infected_severe * 2**20

    # challenge-2
    """estimate severe positive cases that require hospitalization to recover"""
    severe_cases_by_requested_time_impact = 0.15 * infections_by_requested_time_impact
    severe_cases_by_requested_time_severe = 0.15 * infections_by_requested_time_severe

    """estimate beds available for covid-19 positive patients"""
    total_beds_for_covid_19_patients = 0.35 * data['totalHospitalBeds']
    beds_impact = total_beds_for_covid_19_patients - severe_cases_by_requested_time_impact
    beds_severe = total_beds_for_covid_19_patients - severe_cases_by_requested_time_severe

    # challenge-3
    """estimate ICU cases"""
    cases_for_icu_by_requested_time_impact = 0.05 * infections_by_requested_time_impact
    cases_for_icu_by_requested_time_severe = 0.05 * infections_by_requested_time_severe

    """estimate ventilators required"""
    cases_for_ventilators_impact = 0.02 * infections_by_requested_time_impact
    cases_for_ventilators_severe = 0.02 * infections_by_requested_time_severe

    """estimate dollars to be lost"""
    dollars_in_flight_impact = int(infections_by_requested_time_impact * data['region']['avgDailyIncomeInUSD']* data['timeToElapse'])
    dollars_in_flight_severe = int(infections_by_requested_time_severe * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])

    output = {
        "data": data,

        "estimate": {
            "impact": {
                "currentlyInfected": currently_infected_impact,
                "infectionsByRequestedTime": infections_by_requested_time_impact,
                "severeCasesByRequestedTime": severe_cases_by_requested_time_impact,
                "hospitalBedsByRequestedTime": beds_impact,
                "casesForICUByRequestedTime": cases_for_icu_by_requested_time_impact,
                "casesForVentilatorsByRequestedTime":cases_for_ventilators_impact,
                "dollarsInFlight": dollars_in_flight_impact
            },
            "severeImpact": {
                "currentlyInfected": currently_infected_severe,
                "infectionsByRequestedTime": infections_by_requested_time_severe,
                "severeCasesByRequestedTime": severe_cases_by_requested_time_severe,
                "hospitalBedsByRequestedTime": beds_severe,
                "casesForICUByRequestedTime": cases_for_icu_by_requested_time_severe,
                "casesForVentilatorsByRequestedTime":cases_for_ventilators_severe,
                "dollarsInFlight": dollars_in_flight_severe
            }

        }
    }

    return output