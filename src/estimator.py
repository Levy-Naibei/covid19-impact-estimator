def estimator(data):
  impact = {}  # your best case estimation
  severe_impact = {}  # your severe case estimation
  # import pdb; pdb.set_trace()
  total_hospital_beds = (0.35 * data['totalHospitalBeds'])
  time_to_elapse = (2 ** (data['timeToElapse'] / 3))

  # currentlyInfected
  impact['currentlyInfected'] = (data['reportedCases'] * 10)
  severe_impact['currentlyInfected'] = (data['reportedCases'] * 50)

  # infectionsByRequestedTime
  impact['infectionsByRequestedTime'] = (impact['currentlyInfected'] * time_to_elapse)
  severe_impact['infectionsByRequestedTime'] = (severe_impact['currentlyInfected'] * time_to_elapse)

  # # severeCasesByRequestedTime
  # impact['severeCasesByRequestedTime'] = (0.15 * impact['infectionsByRequestedTime'])
  # severe_impact['severeCasesByRequestedTime'] = (0.15 * severe_impact[
  #                                                 'infectionsByRequestedTime'])
  #
  # # total_hospital_beds
  # impact['hospitalBedsByRequestedTime'] = total_hospital_beds - impact[
  #                                         'severeCasesByRequestedTime']
  # severe_impact['hospitalBedsByRequestedTime'] = total_hospital_beds - severe_impact[
  #                                                 'severeCasesByRequestedTime']
  #
  # # casesForICUByRequestedTime
  # impact['casesForICUByRequestedTime'] = (0.05 * impact['infectionsByRequestedTime'])
  # severe_impact['casesForICUByRequestedTime'] = (0.05 * severe_impact[
  #                                                'infectionsByRequestedTime'])
  #
  # # casesForVentilatorsByRequestedTime
  # impact['casesForVentilatorsByRequestedTime'] = (0.02 * impact['infectionsByRequestedTime'])
  # severe_impact['casesForVentilatorsByRequestedTime'] = (0.02 * severe_impact[
  #                                                        'infectionsByRequestedTime'])
  #
  # # dollarsInFlight
  # impact['dollarsInFlight'] = ((impact['infectionsByRequestedTime'] * 0.65 * 1.5) / 30)
  # severe_impact['dollarsInFlight'] = ((severe_impact[
  #                                        'infectionsByRequestedTime'] * 0.65 * 1.5) / 30)

  output = {
    "data": data,
    "impact": impact,
    "severeImpact": severe_impact
  }

  return output