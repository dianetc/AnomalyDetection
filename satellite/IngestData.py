# Ingest data from the csv file and create getter functions
import sys
import csv
from Satellite import Satellite

def get_sample_data():
	data =  []
	satellitedata = open('data.csv', 'r')
	entries = csv.reader(satellitedata,delimiter=',')
	for entry in entries:
		data.append(Satellite(entry))
	satellitedata.close()
	return data	

def get_subset_data(data,attribute = 'type',attr_value=None):
	if attr_value is None:
		return data
	i = 0
	subset = []
	while i < len(data):
		if getattr(data[i],attribute) == attr_value:
			subset.append(data[i])
		i+=1
	return subset

def get_ids(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        ids = []
        i = 0
        while i < len(data):
                ids.append(data[i].id)
                i+=1
        return ids
def get_operator_countries(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        operator_countries = []
        i = 0
        while i < len(data):
                operator_countries.append(data[i].operator_country)
                i+=1
        return operator_countries
def get_users(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        users = []
        i = 0
        while i < len(data):
                users.append(data[i].user)
                i+=1
        return users
def get_purposes(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        purposes = []
        i = 0
        while i < len(data):
                purposes.append(data[i].purpose)
                i+=1
        return purposes
def get_classes(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	classes = []
	i = 0
	while i < len(data):
		classes.append(data[i].class_type)
		i+=1
	return classes
def get_types(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        types = []
        i = 0
        while i < len(data):
                types.append(data[i].type)
                i+=1
        return types
def get_perigees(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        perigees = []
        i = 0
        while i < len(data):
                perigees.append(data[i].perigee)
                i+=1
        return perigees	
def get_apogees(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        apogees = []
        i = 0
        while i < len(data):
                apogees.append(data[i].apogee)
                i+=1
        return apogees
def get_eccentricities(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        eccentricities = []
        i = 0
        while i < len(data):
                eccentricities.append(data[i].eccentricity)
                i+=1
        return eccentricities
def get_periods(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        periods = []
        i = 0
        while i < len(data):
                periods.append(data[i].period)
                i+=1
        return periods
def get_launch_masses(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        launch_masses = []
        i = 0
        while i < len(data):
                launch_masses.append(data[i].launch_mass)
                i+=1
        return launch_masses
def get_dry_masses(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        dry_masses = []
        i = 0
        while i < len(data):
                dry_masses.append(data[i].dry_mass)
                i+=1
        return dy_masses
def get_powers(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        powers = []
        i = 0
        while i < len(data):
                powers.append(data[i].power)
                i+=1
        return powers
def get_dates(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        dates = []
        i = 0
        while i < len(data):
                dates.append(data[i].date)
                i+=1
        return dates
def get_expected_lifetimes(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        expected_lifetimes = []
        i = 0
        while i < len(data):
                expected_lifetimes.append(data[i].expected_lifetime)
                i+=1
        return expected_lifetimes
def get_contractor_countries(attribute = 'type',attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        contractor_countries = []
        i = 0
        while i < len(data):
                contractor_countries.append(data[i].contractor_country)
                i+=1
        return contractor_countries
def get_launch_sites(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	launch_sites = []
	i = 0
	while i < len(data):
		launch_sites.append(data[i].launch_site)
		i+=1
	return launch_sites
def get_launch_vehicles(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	launch_vehicles = []
	i = 0
	while i < len(data):
		launch_vehicles.append(data[i].launch_vehicle)
		i+=1
	return launch_vehicles
def get_sources(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	sources = []
	i = 0
	while i < len(data):
		sources.append(data[i].source)
		i+=1
	return sources
def get_longitudes(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	longitudes = []
	i = 0
	while i < len(data):
		longitudes.append(data[i].longitude)
		i+=1
	return longitudes
def get_inclinations(attribute = 'type',attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	inclinations = []
	i = 0
	while i < len(data):
		inclinations.append(data[i].inclination)
		i+=1
	return inclinations
