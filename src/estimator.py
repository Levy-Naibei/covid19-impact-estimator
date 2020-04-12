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
#   currentlyInfected_impact = int(input_data['reportedCases'] * 10)
#   currentlyInfected_severe = int(input_data['reportedCases'] * 50)
#
#   """ estimate projected infections """
#   time_to_elapse = 2 ** int(input_data['timeToElapse'] / 3)
#   infectionsByRequestedTime_impact = int(currentlyInfected_impact * time_to_elapse)
#   infectionsByRequestedTime_severe = int(currentlyInfected_severe * time_to_elapse)
#
#   # challenge-2
#   """estimate severe positive cases that require hospitalization to recover"""
#   severeCasesByRequestedTime_impact = 0.15 * infectionsByRequestedTime_impact
#   severeCasesByRequestedTime_severe = 0.15 * infectionsByRequestedTime_severe
#
#   """estimate beds available for covid-19 positive patients"""
#   total_beds_for_covid_19_patients = 0.35 * input_data['totalHospitalBeds']
#   beds_impact = total_beds_for_covid_19_patients - severeCasesByRequestedTime_impact
#   beds_severe = total_beds_for_covid_19_patients - severeCasesByRequestedTime_severe
#
#   # challenge-3
#   """estimate ICU cases"""
#   cases_for_icu_by_requested_time_impact = 0.05 * infectionsByRequestedTime_impact
#   cases_for_icu_by_requested_time_severe = 0.05 * infectionsByRequestedTime_severe
#
#   """estimate ventilators required"""
#   cases_for_ventilators_impact = 0.02 * infectionsByRequestedTime_impact
#   cases_for_ventilators_severe = 0.02 * infectionsByRequestedTime_severe
#
#   """estimate dollars to be lost"""
#   dollarsInFlight_impact = int(infectionsByRequestedTime_impact * input_data['region']['avgDailyIncomeInUSD']* input_data['timeToElapse'])
#   dollarsInFlight_severe = int(infectionsByRequestedTime_severe * input_data['region']['avgDailyIncomeInUSD'] * input_data['timeToElapse'])
#
#   output = {
#     "data": input_data,
#     "impact": {
#       "currentlyInfected": currentlyInfected_impact,
#       "infectionsByRequestedTime": infectionsByRequestedTime_impact
#       # "severeCasesByRequestedTime": severeCasesByRequestedTime_impact,
#       # "hospitalBedsByRequestedTime": beds_impact,
#       # "casesForICUByRequestedTime": cases_for_icu_by_requested_time_impact,
#       # "casesForVentilatorsByRequestedTime":cases_for_ventilators_impact,
#       # "dollarsInFlight": dollarsInFlight_impact
#     },
#     "severeImpact": {
#       "currentlyInfected": currentlyInfected_severe,
#       "infectionsByRequestedTime": infectionsByRequestedTime_severe
#       # "severeCasesByRequestedTime": severeCasesByRequestedTime_severe,
#       # "hospitalBedsByRequestedTime": beds_severe,
#       # "casesForICUByRequestedTime": cases_for_icu_by_requested_time_severe,
#       # "casesForVentilatorsByRequestedTime":cases_for_ventilators_severe,
#       # "dollarsInFlight": dollarsInFlight_severe
#     }
#   }
#
#   return output


def estimator(data):
  impact = {}  # your best case estimation
  severe_impact = {}  # your severe case estimation
  # import pdb; pdb.set_trace()
  total_hospital_beds = int(0.35 * data['totalHospitalBeds'])

  # currentlyInfected
  impact['currentlyInfected'] = data['reportedCases'] * 10
  severe_impact['currentlyInfected'] = data['reportedCases'] * 50

  # infectionsByRequestedTime
  impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * 512
  severe_impact['infectionsByRequestedTime'] = severe_impact['currentlyInfected'] * 512

  # severeCasesByRequestedTime
  impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
  severe_impact['severeCasesByRequestedTime'] = int(0.15 * severe_impact['infectionsByRequestedTime'])

  # total_hospital_beds
  impact['hospitalBedsByRequestedTime'] = total_hospital_beds - impact['severeCasesByRequestedTime']
  severe_impact['hospitalBedsByRequestedTime'] = total_hospital_beds - severe_impact[
    'severeCasesByRequestedTime']

  # casesForICUByRequestedTime
  impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
  severe_impact['casesForICUByRequestedTime'] = int(0.05 * severe_impact['infectionsByRequestedTime'])

  # casesForVentilatorsByRequestedTime
  impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
  severe_impact['casesForVentilatorsByRequestedTime'] = int(0.02 * severe_impact['infectionsByRequestedTime'])

  # dollarsInFlight
  impact['dollarsInFlight'] = int((impact['infectionsByRequestedTime'] * 0.65 * 1.5) / 30)
  severe_impact['dollarsInFlight'] = int((severe_impact['infectionsByRequestedTime'] * 0.65 * 1.5) / 30)

  output = {
    "data": data,
    "impact": impact,
    "severe_impact": severe_impact
  }

  return output

data = {
    "region": {
      "name": "Africa",
      "avgAge": 19.7,
      "avgDailyIncomeInUSD": 5,
      "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}

print(estimator(data))