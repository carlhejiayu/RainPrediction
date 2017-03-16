import pandas as pd

def getData():
    '''
    Retrieve 10 years of data
    1996-2003 data is used for trainning
    2004-2006 data is used for testing
    :return: a tuple (trainning, testing), where trainning/testing is a tuple which contain one dataframe of normalized data and one dataframe of lables
    '''
    startingYear = 1996;
    DataInYear = []
    for i in range (0, 10):
        FileName = 'data/'+str(startingYear+i) +'.csv'
        CSVData = pd.read_csv(FileName).fillna(0)
        Label = CSVData['Total Precip (mm)']
        processData  = CSVData.drop(['Date/Time', 'Month','Day','Total Precip (mm)','Dir of Max Gust Flag','Snow on Grnd Flag','Spd of Max Gust Flag'],1)
        processData['Total Rain Flag'] = processData['Total Rain Flag'].map({0:0, 'T':1 ,'M':2 })
        processData['Total Snow Flag'] = processData['Total Snow Flag'].map({0: 0, 'T': 1, 'M': 2})
        processData['Total Precip Flag'] = processData['Total Precip Flag'].map({0: 0, 'T': 1, 'M': 2})
        processData['Spd of Max Gust (km/h)'] = processData['Spd of Max Gust (km/h)'].replace(['<31'],1)
        DataInYear.append( (processData,Label))
    TrainningSet = DataInYear[0:7]
    TestingSet = DataInYear [7:10]

    TrainningDataFrameSet =[]
    TrainningLableFrameSet =[]
    for train in TrainningSet:
        TrainningDataFrameSet.append((train[0]))
        TrainningLableFrameSet.append((train[1]))

    Trainning = (pd.concat(TrainningDataFrameSet), pd.concat(TrainningLableFrameSet))

    TestingDataFrameSet =[]
    TestingLableFrameSet =[]
    for train in TestingSet:
        TestingDataFrameSet.append((train[0]))
        TestingLableFrameSet.append((train[1]))

    Testing = (pd.concat(TestingDataFrameSet), pd.concat(TestingLableFrameSet))

    return Trainning, Testing