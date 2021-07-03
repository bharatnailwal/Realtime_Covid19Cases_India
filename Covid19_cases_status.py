import requests

def data(api):
    res = requests.get(api).json()
    for i in res:
        print(i)
    stateName = input("Please select the state name from the following ")
    for i in res[stateName]['districtData']:
        print(i)
    distName = input("Please select the district name from the following ")
    for i in res[stateName]['districtData'][distName]:
        print(i)
    status = input("""Please select the status from the following\n
                confirmed\n
                migratedother\n
                deceased\n
                recovered\n """)

    print("Total number of "+status+" cases in "+distName+" in "+stateName +" state "+" are ")
    print(res[stateName]['districtData'][distName][status])

if __name__ == "__main__":
    api = "https://api.covid19india.org/state_district_wise.json"
    data(api)
