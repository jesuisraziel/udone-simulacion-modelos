import statistics
from math import sqrt

def calculate_mean(data_list):
	return statistics.mean(data_list)

def calculate_median(data_list):
	return statistics.median(data_list)

def calculate_mode(data_list):
	return statistics.mode(data_list)

def calculate_variance(data_list, mean=None):
	return statistics.variance(data_list)

def calculate_range(data_list):
	return abs(max(data_list) - min(data_list))

def get_descriptive_stats(labeled_input_dict,label):
	
	local_dict_copy = dict(labeled_input_dict)

	data_list = local_dict_copy[label]

	mean = calculate_mean(data_list)
	median = calculate_median(data_list)
	mode = calculate_mode(data_list)
	variance = calculate_variance(data_list, mean)
	std_deviation = sqrt(variance)
	dataset_range = calculate_range(data_list)

	stats = {
		"central_tendency": {
			"mean":mean,
			"median":median,
			"mode":mode,
		},
		"dispersion": {
			"range":dataset_range,
			"variance":variance,
			"std_deviaton":std_deviation
		}
	}

	local_dict_copy["stats"] = stats

	return local_dict_copy