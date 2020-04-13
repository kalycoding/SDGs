import math

def estimator(data):
    class Impact:
        def __init__(self):
            self.currentlyInf = []
            self.infectByTime = []
            self.severeCases = []
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
        def SevereCasesByRequestedTime(self):
            self.severeCases = int(0.15 * self.infectByTime)
            return self.severeCases
        def hospitalBedsByRequestedTime(self, bed):
            return int(0.35 * data['totalHospitalBeds'] - (0.15 * self.infectByTime))  
        def casesForICUByRequestedTime(self):
            return int(0.05 * self.infectByTime)
        def casesForVentilatorsByRequestedTime(self):
            return int(0.02 * self.infectByTime)
        def dollarsInFlight(self):
            return math.trunc((self.infectByTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) * data['timeToElapse'])

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
        def SevereCasesByRequestedTime(self):
            return int(0.15 * self.infectByTime)
        def hospitalBedsByRequestedTime(self, bed):
            return int(0.35 * data['totalHospitalBeds'] - (0.15 * self.infectByTime)) 
        def casesForICUByRequestedTime(self):
            return int(0.05 * self.infectByTime)
        def casesForVentilatorsByRequestedTime(self):
            return int(0.02 * self.infectByTime)
        def dollarsInFlight(self):
            if data['periodType'] == 'days':
                factor = data['timeToElapse'] * 1
            elif data['periodType'] == 'weeks':
                factor = factor = data['timeToElapse'] * 7
            else:
                factor = factor = data['timeToElapse'] * 30
            return math.trunc((self.infectByTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) * factor)
        
    impact = Impact()
    severe = SevereImpact()
    data = {
            "impact": {
                "currentlyInfected": impact.currentlyInfected(data['reportedCases']),
                "infectionsByRequestedTime": impact.infectionsByRequestedTime(data['timeToElapse']),
                "severeCasesByRequestedTime": impact.SevereCasesByRequestedTime(),
                "hospitalBedsByRequestedTime": impact.hospitalBedsByRequestedTime(data['totalHospitalBeds']),
                "casesForICUByRequestedTime": impact.casesForICUByRequestedTime(),
                "casesForVentilatorsByRequestedTime": impact.casesForVentilatorsByRequestedTime(),
                "dollarsInFlight": impact.dollarsInFlight()
            },
            "severeImpact": {
                "currentlyInfected": severe.currentlyInfected(data['reportedCases']),
                "infectionsByRequestedTime": severe.infectionsByRequestedTime(data['timeToElapse']),
                "severeCasesByRequestedTime": severe.SevereCasesByRequestedTime(),
                "hospitalBedsByRequestedTime": severe.hospitalBedsByRequestedTime(data['totalHospitalBeds']),
                "casesForICUByRequestedTime": severe.casesForICUByRequestedTime(),
                "casesForVentilatorsByRequestedTime": severe.casesForVentilatorsByRequestedTime(),
                "dollarsInFlight": severe.dollarsInFlight()
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
print(estimator(data))

