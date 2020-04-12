def estimator(data):
  impact = {}  # your best case estimation
  severe_impact = {}  # your severe case estimation
  # import pdb; pdb.set_trace()
  total_hospital_beds = int(0.35 * data['totalHospitalBeds'])
  time_to_elapse = int(2 ** (data['timeToElapse'] / 3))

  # currentlyInfected
  impact['currentlyInfected'] = int(data['reportedCases'] * 10)
  severe_impact['currentlyInfected'] = int(data['reportedCases'] * 50)

  # infectionsByRequestedTime
  impact['infectionsByRequestedTime'] = int(impact['currentlyInfected'] * time_to_elapse)
  severe_impact['infectionsByRequestedTime'] = int(severe_impact['currentlyInfected'] * time_to_elapse)

  # # severeCasesByRequestedTime
  # impact['severeCasesByRequestedTime'] = int(0.15 * impact['infectionsByRequestedTime'])
  # severe_impact['severeCasesByRequestedTime'] = int(0.15 * severe_impact['infectionsByRequestedTime'])
  #
  # # total_hospital_beds
  # impact['hospitalBedsByRequestedTime'] = total_hospital_beds - impact[
  #                                         'severeCasesByRequestedTime']
  # severe_impact['hospitalBedsByRequestedTime'] = total_hospital_beds - severe_impact[
  #                                                 'severeCasesByRequestedTime']
  #
  # # casesForICUByRequestedTime
  # impact['casesForICUByRequestedTime'] = int(0.05 * impact['infectionsByRequestedTime'])
  # severe_impact['casesForICUByRequestedTime'] = int(0.05 * severe_impact['infectionsByRequestedTime'])
  #
  # # casesForVentilatorsByRequestedTime
  # impact['casesForVentilatorsByRequestedTime'] = int(0.02 * impact['infectionsByRequestedTime'])
  # severe_impact['casesForVentilatorsByRequestedTime'] = int(0.02 * severe_impact['infectionsByRequestedTime'])
  #
  # # dollarsInFlight
  # impact['dollarsInFlight'] = int((impact['infectionsByRequestedTime'] * 0.65 * 1.5) / 30)
  # severe_impact['dollarsInFlight'] = int((severe_impact['infectionsByRequestedTime'] * 0.65 * 1.5) / 30)

  output = {
    "data": data,
    "impact": impact,
    "severeImpact": severe_impact
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