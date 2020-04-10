def estimator(data):
  class Impact:
    def __init__(self):
        self.currentlyInf = []
        self.infectByTime = []
    def currentlyInfected(self, reportCases):
        self.currentlyInf = reportCases * 10
        return self.currentlyInf
    def infectionsByRequestedTime(self, days):
        if data['data']['periodType'] == 'days':
            factor = days // 3
        elif data['data']['periodType'] == 'weeks':
            days = days * 7
            factor = days // 3
        else:
            days = days * 30
            factor = days // 3
        self.infectByTime = self.currentlyInf * (2 ** factor)
        return self.infectByTime
    def SevereCasesByRequestedTime(self):
        return int(0.15 * self.infectByTime)
    def hospitalBedsByRequestedTime(self, bed):
        return int(0.35 * (bed - self.infectByTime * 0.15))
    def casesForICUByRequestedTime(self):
        return int(0.05 * self.infectByTime)
    def casesForVentilatorsByRequestedTime(self):
        return int(0.02 * self.infectByTime)
    def dollarsInFlight(self, population, dollar, days):
        if data['data']['periodType'] == 'days':
            days = 30
        elif data['data']['periodType'] == 'weeks':
            days = days * 7
        else:
            days = days * 30
        return (self.infectByTime * population * dollar * days)

  class SevereImpact:
    def __init__(self):
        self.currentlyInf = []
        self.infectByTime = []
    def currentlyInfected(self, reportCases):
        self.currentlyInf = reportCases * 50
        return self.currentlyInf
    def infectionsByRequestedTime(self, days):
        if data['data']['periodType'] == 'days':
            factor = days // 3
        elif data['data']['periodType'] == 'weeks':
            days = days * 7
            factor = days // 3
        else:
            days = days * 30
            factor = days // 3
        self.infectByTime = self.currentlyInf * (2 ** factor)
        return self.infectByTime
    def SevereCasesByRequestedTime(self):
        return int(0.15 * self.infectByTime)
    def hospitalBedsByRequestedTime(self, bed):
        return int(0.35 * (bed - self.infectByTime * 0.15))
    def casesForICUByRequestedTime(self):
        return int(0.05 * self.infectByTime)
    def casesForVentilatorsByRequestedTime(self):
        return int(0.02 * self.infectByTime)
    def dollarsInFlight(self, population, dollar, days):
        if data['data']['periodType'] == 'days':
            days = 30
        elif data['data']['periodType'] == 'weeks':
            days = days * 7
        else:
            days = days * 30
        return (self.infectByTime * population * dollar * days)
  
  impacting = Impact()
  severeImpacting = SevereImpact()
  impact = {
    "estimate": {
      "impact": {
    "currentlyInfected": impacting.currentlyInfected(data['data']['reportedCases']),
    "infectionsByRequestedTime": impacting.infectionsByRequestedTime(data['data']['timeToElapse']),
    "severeCasesByRequestedTime": impacting.SevereCasesByRequestedTime(),
    "hospitalBedsByRequestedTime": impacting.hospitalBedsByRequestedTime(data['data']['totalHospitalBeds']),
    "casesForICUByRequestedTime": impacting.casesForICUByRequestedTime(),
    "casesForVentilatorsByRequestedTime": impacting.casesForVentilatorsByRequestedTime(),
    "dollarsInFlight": impacting.dollarsInFlight(data['data']['region']['avgDailyIncomePopulation'],data['data']['region']['avgDailyIncomeInUSD'], data['data']['timeToElapse'])
  },
    "severeImpact": {
    "currentlyInfected": severeImpacting.currentlyInfected(data['data']['reportedCases']),
    "infectionsByRequestedTime": severeImpacting.infectionsByRequestedTime(data['data']['timeToElapse']),
    "severeCasesByRequestedTime": severeImpacting.SevereCasesByRequestedTime(),
    "hospitalBedsByRequestedTime": severeImpacting.hospitalBedsByRequestedTime(data['data']['totalHospitalBeds']),
    "casesForICUByRequestedTime": severeImpacting.casesForICUByRequestedTime(),
    "casesForVentilatorsByRequestedTime": severeImpacting.casesForVentilatorsByRequestedTime(),
    "dollarsInFlight": severeImpacting.dollarsInFlight(data['data']['region']['avgDailyIncomePopulation'],data['data']['region']['avgDailyIncomeInUSD'], data['data']['timeToElapse'])
        }
    }
  }
  return data

estimator(data = {
  "data": {
    "region": {
      "name": "Africa",
      "avgAge": 19.7,
      "avgDailyIncomeInUSD": 4,
      "avgDailyIncomePopulation": 0.73
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874
  }
})


