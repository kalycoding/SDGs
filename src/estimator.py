import json

def estimator(data):
    class Impact:
        def __init__(self):
            self.currentlyInf = []
            self.infectByTime = []
        def currentlyInfected(self, reportCases):
            self.currentlyInf = reportCases * 10
            return self.currentlyInf
        def infectionsByRequestedTime(self, days):
            if data['periodType'] == 'days':
                factor = days // 3
            elif data['periodType'] == 'weeks':
                days = days * 7
                factor = days // 3
            else:
                days = days * 30
                factor = days // 3
            self.infectByTime = self.currentlyInf * (2 ** factor)
            return self.infectByTime

    class SevereImpact:
        def __init__(self):
            self.currentlyInf = []
            self.infectByTime = []
        def currentlyInfected(self, reportCases):
            self.currentlyInf = reportCases * 50
            return self.currentlyInf
        def infectionsByRequestedTime(self, days):
            if data['periodType'] == 'days':
                factor = days // 3
            elif data['periodType'] == 'weeks':
                days = days * 7
                factor = days // 3
            else:
                days = days * 30
                factor = days // 3
            self.infectByTime = self.currentlyInf * (2 ** factor)
            return self.infectByTime
    impact = Impact()
    severe = SevereImpact()
    data = {
        "estimate": {
            "impact": {
                "currentlyInfected": impact.currentlyInfected(data['reportedCases']),
                "infectionsByRequestedTime": impact.infectionsByRequestedTime(data['timeToElapse']),
            }
        }
    }
    
    return data

data = {
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
estimator(data)

