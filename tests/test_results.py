from utils.readingJson import readJsonData
import pytest

searchData = "testData/searchData.json"
# testData = readJsonData(searchData)
testdata ="hello"

@pytest.mark.parametrize("testData,tesdat2", [("hello", "hi"), ("hello2", "h12") ])
def test_searchDataValues(testData, tesdat2):
    print("testData",testData)
    print("testData2", tesdat2)
    # print(testData["testData3"]["subData1"])


    
   