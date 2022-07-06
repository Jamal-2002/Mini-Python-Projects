
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def damages_to_float(integer_list):
  another_list = []
  for element in integer_list:
    if element == 'Damages not recorded':
      another_list.append(element)
    elif element[-1]=='M':
      element = element.replace('M','')
      element = float(element) * 1000000
      another_list.append(element)
    elif element.endswith('B'):
      element = element.replace('B','')
      element = float(element) * 1000000000
      another_list.append(element)  
  return another_list     
# test function by updating damages
new_damages_list = (damages_to_float(damages))



hurricanes = {}
def dict_maker(names,months,years,max_sustained_winds,areas_affected,new_damages_list,deaths):
  global hurricanes
  for i in range(34):
    hurricanes[names[i]] = {
      'Name' : names[i],
      'Month' : months[i],
      'Year' : years[i],
      'Max Sustained Wind' : max_sustained_winds[i],
      'Areas Affected' : areas_affected[i],
      'Damages': new_damages_list[i],
      'Death' : deaths[i]  
    }
  return hurricanes  


dict_maker(names,months,years,max_sustained_winds,areas_affected,new_damages_list,deaths)

def year_dict(year):
  global hurricanes
  year_list = []
  for name in hurricanes:
    if hurricanes[name]['Year'] == year:
      year_list.append(hurricanes[name])
  return year_list

from collections import Counter
def affected_areas_counter(affected_areas):
  counted_areas = [area for sublist in affected_areas for area in sublist]
  return Counter(counted_areas)

def most_affected_area(list_of_areas):
  inverted_dict = {k:y for y,k in list_of_areas.items()}
  max_area =  max(inverted_dict)
  max_area_count = inverted_dict[max_area]
  return f"The most affected area was {max_area_count} with a count of {max_area}"



dict_death_count = {}
def most_deaths():
  global names,deaths
  global dict_death_count
  
  list_death_count = zip(names,deaths)
  dict_death_count =  dict(list_death_count)
  inverted_dict = {k:y for y,k in dict_death_count.items()}
  max_death =  max(inverted_dict)
  deadliest_hurricane = inverted_dict[max_death]
  return f"The hurricane that caused the most deaths was {deadliest_hurricane} with a count of {max_death}"

(most_deaths())
(dict_death_count)

def mortality_rate():
  global dict_death_count
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  #mortality_scale = {0: 0,
                   #1: 100,
                   #2: 500,
                   #3: 1000,
                   #4: 10000}
  for name,count in dict_death_count.items():
    if count <0:
      hurricanes_by_mortality[0].append(name)
    elif count <100:
      hurricanes_by_mortality[1].append(name)
    elif count <500:
      hurricanes_by_mortality[2].append(name)
    elif count <1000:
      hurricanes_by_mortality[3].append(name)
    elif count <10000:
      hurricanes_by_mortality[4].append(name) 
    else:
      hurricanes_by_mortality[5].append(name)

  return  hurricanes_by_mortality      

#print(mortality_rate())     
dict_most_damage = {}
def most_damage():
  global names,damages
  global dict_most_damage
  global hurricanes
  
  max_damaging_hurricane = ''
  max_damage = 0

  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damages'] == 'Damages not recorded':
      continue
    if hurricanes[hurricane]['Damages'] > max_damage:
        max_damage = hurricanes[hurricane]['Damages']
        max_damaging_hurricane = hurricanes[hurricane]['Name']
          
  return max_damaging_hurricane,max_damage
(most_damage())


def damage_scaled(hurricanes):

    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}

    for hurricane in hurricanes:

        rate = 0
        damage = hurricanes[hurricane]['Damages']

        if damage == 'Damages not recorded':
            continue
        elif damage < 100000000:
            rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in damage_scale:
            damage_scale[rate] = hurricanes[hurricane]
        else:
            damage_scale[rate].append(hurricanes[hurricane]['Name'])

    return damage_scale

damage_scale = damage_scaled(hurricanes)

