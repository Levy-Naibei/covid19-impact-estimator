# def estimator(data):
#   """covid-19 impact estimator"""
#   # pylint: disable=unused-variable
#   # pylint: disable=pointless-string-statement
#
#   input_data = data
#
#   input_data = {
#     "region": {
#       "name": "Africa",
#       "avgAge": 19.7,
#       "avgDailyIncomeInUSD": 3,
#       "avgDailyIncomePopulation": 0.77
#     },
#     "periodType": "days",
#     "timeToElapse": 60,
#     "reportedCases": 45,
#     "population": 1456011609,
#     "totalHospitalBeds": 1000
#   }
#
#   # challenge-1
#   """ estimate currently infected """
#   currently_infected_impact = int(input_data['reportedCases'] * 10)
#   currently_infected_severe = int(input_data['reportedCases'] * 50)
#
#   """ estimate projected infections """
#   time_to_elapse = 2 ** int(input_data['timeToElapse'] / 3)
#   infections_by_requested_time_impact = int(currently_infected_impact * time_to_elapse)
#   infections_by_requested_time_severe = int(currently_infected_severe * time_to_elapse)
#
#   # challenge-2
#   """estimate severe positive cases that require hospitalization to recover"""
#   severe_cases_by_requested_time_impact = 0.15 * infections_by_requested_time_impact
#   severe_cases_by_requested_time_severe = 0.15 * infections_by_requested_time_severe
#
#   """estimate beds available for covid-19 positive patients"""
#   total_beds_for_covid_19_patients = 0.35 * input_data['totalHospitalBeds']
#   beds_impact = total_beds_for_covid_19_patients - severe_cases_by_requested_time_impact
#   beds_severe = total_beds_for_covid_19_patients - severe_cases_by_requested_time_severe
#
#   # challenge-3
#   """estimate ICU cases"""
#   cases_for_icu_by_requested_time_impact = 0.05 * infections_by_requested_time_impact
#   cases_for_icu_by_requested_time_severe = 0.05 * infections_by_requested_time_severe
#
#   """estimate ventilators required"""
#   cases_for_ventilators_impact = 0.02 * infections_by_requested_time_impact
#   cases_for_ventilators_severe = 0.02 * infections_by_requested_time_severe
#
#   """estimate dollars to be lost"""
#   dollars_in_flight_impact = int(infections_by_requested_time_impact * input_data['region']['avgDailyIncomeInUSD']* input_data['timeToElapse'])
#   dollars_in_flight_severe = int(infections_by_requested_time_severe * input_data['region']['avgDailyIncomeInUSD'] * input_data['timeToElapse'])
#
#   output = {
#     "data": input_data,
#     "impact": {
#       "currentlyInfected": currently_infected_impact,
#       "infectionsByRequestedTime": infections_by_requested_time_impact
#       # "severeCasesByRequestedTime": severe_cases_by_requested_time_impact,
#       # "hospitalBedsByRequestedTime": beds_impact,
#       # "casesForICUByRequestedTime": cases_for_icu_by_requested_time_impact,
#       # "casesForVentilatorsByRequestedTime":cases_for_ventilators_impact,
#       # "dollarsInFlight": dollars_in_flight_impact
#     },
#     "severeImpact": {
#       "currentlyInfected": currently_infected_severe,
#       "infectionsByRequestedTime": infections_by_requested_time_severe
#       # "severeCasesByRequestedTime": severe_cases_by_requested_time_severe,
#       # "hospitalBedsByRequestedTime": beds_severe,
#       # "casesForICUByRequestedTime": cases_for_icu_by_requested_time_severe,
#       # "casesForVentilatorsByRequestedTime":cases_for_ventilators_severe,
#       # "dollarsInFlight": dollars_in_flight_severe
#     }
#   }
#
#   return output


def estimator(data):
  impact = {}  # your best case estimation
  severe_impact = {}  # your severe case estimation
  # import pdb; pdb.set_trace()
  total_hospital_beds = int(0.35 * data['totalHospitalBeds'])

  # currently_infected
  impact['currently_infected'] = data['reportedCases'] * 10
  severe_impact['currently_infected'] = data['reportedCases'] * 50

  # infections_by_requested_time
  impact['infections_by_requested_time'] = impact['currently_infected'] * 512
  severe_impact['infections_by_requested_time'] = severe_impact['currently_infected'] * 512

  # severe_cases_by_requested_time
  impact['severe_cases_by_requested_time'] = int(0.15 * impact['infections_by_requested_time'])
  severe_impact['severe_cases_by_requested_time'] = int(0.15 * severe_impact['infections_by_requested_time'])

  # total_hospital_beds
  impact['hospital_beds_by_requested_time'] = total_hospital_beds - impact['severe_cases_by_requested_time']
  severe_impact['hospital_beds_by_requested_time'] = total_hospital_beds - severe_impact[
    'severe_cases_by_requested_time']

  # casesForICUByRequestedTime
  impact['cases_for_ICU_by_requested_time'] = int(0.05 * impact['infections_by_requested_time'])
  severe_impact['cases_for_ICU_by_requested_time'] = int(0.05 * severe_impact['infections_by_requested_time'])

  # cases_for_ventilators_by_requested_time
  impact['cases_for_ventilators_by_requested_time'] = int(0.02 * impact['infections_by_requested_time'])
  severe_impact['cases_for_ventilators_by_requested_time'] = int(0.02 * severe_impact['infections_by_requested_time'])

  # dollars_in_flight
  impact['dollars_in_flight'] = int((impact['infections_by_requested_time'] * 0.65 * 1.5) / 30)
  severe_impact['dollars_in_flight'] = int((severe_impact['infections_by_requested_time'] * 0.65 * 1.5) / 30)

  output = {
    "data": data,
    "impact": impact,
    "severe_impact": severe_impact
  }

  return output