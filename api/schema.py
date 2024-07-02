import graphene
import requests

class PopulationData(graphene.ObjectType):
    state = graphene.String()
    year = graphene.Int()
    population = graphene.Int()

class VehicleData(graphene.ObjectType):
    vehicles_available = graphene.String()
    households = graphene.Int()

class Query(graphene.ObjectType):
    population_data = graphene.List(PopulationData)
    vehicle_data = graphene.List(VehicleData)

    def resolve_population_data(root, info):
        url = 'https://datausa.io/api/data?drilldowns=State&measures=Population'
        response = requests.get(url)
        data = response.json()
        results = []
        for item in data['data']:
            year = int(item['Year'])  # Convert year to integer
            if year >= 2013 and year <= 2021 and item['State'] in ['Alabama', 'Florida', 'California']:
                results.append(PopulationData(
                    state=item['State'],
                    year=year,
                    population=item['Population']
                ))
        return results

    def resolve_vehicle_data(root, info):
        url = 'https://zircon.datausa.io/api/data?measure=Commute%20Means%20by%20Gender&geo=01000US&drilldowns=Vehicles%20Available'
        response = requests.get(url)
        data = response.json()
        results = []
        for item in data['data']:
            if item['Year'] == '2021':  # Filter for the year 2021
                results.append(VehicleData(
                    vehicles_available=item['Vehicles Available'],
                    households=item['Commute Means by Gender']  # Assuming 'Commute Means by Gender' represents households
                ))
        return results

schema = graphene.Schema(query=Query)
