
def estimator(data):

  # challenge-1
  reported_cases = int(input("Enter COVID-19 reported cases: "))

  """ estimate currently infected """
  impact = {"currently_infected":reported_cases * 10}
  severe_impact = {"currently_infected":reported_cases * 50}

  """ estimate projected infections """
  infections_by_requested_time_impact = impact['currently_infected'] * 512
  infections_by_requested_time_severe = severe_impact['currently_infected'] * 512

  # challenge-2
  """estimate severe positive cases that require hospitalization to recover"""
  severe_cases_by_requested_time_impact = 0.15 * infections_by_requested_time_impact
  severe_cases_by_requested_time_severe = 0.15 * infections_by_requested_time_severe

  """estimate beds available for covid-19 positive patients"""
  total_beds_for_covid_19_patients = 0.35 * 1380614
  beds_by_requested_time_impact = total_beds_for_covid_19_patients - severe_cases_by_requested_time_impact
  beds_by_requested_time_severe = total_beds_for_covid_19_patients - severe_cases_by_requested_time_severe

  # challenge-3
  """estimate ICU cases"""
  cases_for_icu_by_requested_time_impact = 0.05 * infections_by_requested_time_impact
  cases_for_icu_by_requested_time_severe = 0.05 * infections_by_requested_time_severe

  """estimate ventilators required"""
  cases_for_ventilators_bby_requested_time_impact = 0.02 * infections_by_requested_time_impact
  cases_for_ventilators_bby_requested_time_severe = 0.02 * infections_by_requested_time_severe

  """estimate dollars to be lost"""
  dollars_in_flight_impact = infections_by_requested_time_impact * avg_daily_income_in_USD * period
  dollars_in_flight_severe = infections_by_requested_time_severe * avg_daily_income_in_USD * period

  return data
