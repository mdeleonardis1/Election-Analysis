print("hello World")

counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties[0])
print(len(counties))

counties_dict = {}

counties_dict["arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print(counties_dict.keys())
print(counties_dict.values())

print(counties_dict.get("Denver"))
print(counties_dict['arapahoe'])

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829}) 
voting_data.append({"county":"Denver", "registered_voters": 463353}) 
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)


if counties[1] == 'Denver':
    print(counties[1])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for v in counties_dict.values():
    print(v)

for key, value in counties_dict.items():
    print(key, value)

for i in voting_data:
    print(i)
#  use the range() function to iterate over the list of dictionaries and print the counties in voting_data

for i in range(len(voting_data)):
      print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")