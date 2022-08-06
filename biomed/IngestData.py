# Ingest data from the arff file and create getter functions
import sys
from Sample import Sample

def get_sample_data():
	data =  []
	biodata = open('cleanData.arff', 'r')
	while True:
		entry = biodata.readline()
		if not entry:
			break
		entry = entry.split(",")
		data.append(Sample(entry))
	biodata.close()
	return data	

# get_subset_data(data, attribute, attr_value) ==> give me all samples with attribute == attr_value
# default gives you all the data
def get_subset_data(data,attribute = "class_type",attr_value=None):
	if attr_value is None:
		return data
	i = 0
	subset = []
	while i < len(data):
		if getattr(data[i],attribute) == attr_value:
			subset.append(data[i])
		i+=1
	return subset

def get_observations(attribute = "class_type",attr_value=None):
        data = get_subset_data(get_sample_data(),attr_value)
        observations = []
        i = 0
        while i < len(data):
                observations.append(data[i].observation)
                i+=1
        return observations
def get_ids(attribute = "class_type",attr_value=None):
        data = get_subset_data(get_sample_data(),attribute,attr_value)
        ids = []
        i = 0
        while i < len(data):
                ids.append(data[i].id)
                i+=1
        return ids
def get_ages(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	ages = []
	i = 0
	while i < len(data):
		ages.append(data[i].age)
		i+=1
	return ages
def get_sample_dates(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)        
	sample_dates = []
	i = 0
	while i < len(data):
		sample_dates.append(data[i].sample_date)
		i+=1
	return sample_dates
def get_m1s(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	m1s = []
	i = 0
	while i < len(data):
		m1s.append(data[i].m1)
		i+=1
	return m1s
def get_m2s(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	m2s = []
	i = 0
	while i < len(data):
		m2s.append(data[i].m2)
		i+=1
	return m2s
def get_m3s(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	m3s = []
	i = 0
	while i < len(data):
		m3s.append(data[i].m3)
		i+=1
	return m3s	
def get_m4s(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	m4s = []
	i = 0
	while i < len(data):
		m4s.append(data[i].m4)
		i+=1
	return m4s
def get_class_types(attribute = "class_type",attr_value=None):
	data = get_subset_data(get_sample_data(),attribute,attr_value)
	class_types = []
	i = 0
	while i < len(data):
		class_types.append(data[i].class_type)
		i+=1
	return class_types
