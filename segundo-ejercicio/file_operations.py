import csv

def prepare_rows(output_dict):
	entries = output_dict["edades"]
	stats = output_dict["stats"]
	rows = []
	first = True
	stat_array = []

	for stat_category_label in stats:
			stat_category = stats[stat_category_label]
			for stat_label in stat_category:
				stat = stat_category[stat_label]
				stat_array.append(stat)

	for age in entries:
		if first == True:
			row = [age] + [""] + stat_array
			first = False
		else:
			row = [age]
		rows.append(row)

	return rows


def get_data_as_dict(csv_file_path):
	with open(csv_file_path, "r") as file:
		csv_reader = csv.reader(file)
		first = True
		data = {"edades":[]}
		for row in csv_reader:
			if first == True:
				first = False
				continue
			converted_entry = int(row[0])
			data["edades"].append(converted_entry)
		return data

def write_stats(csv_file_path, output_dict):
	with open(csv_file_path, "w", newline='') as file:
		rows = prepare_rows(output_dict)
		statwriter = csv.writer(file)
		statwriter.writerow(["Edades", "", "Media", "Mediana", "Moda", "Rango", "Varianza", "Desviación Estándar"])
		statwriter.writerows(rows)