from file_operations import get_data_as_dict, write_stats 
from descriptive import get_descriptive_stats
from generator import generate_CSV

if __name__ == "__main__":
	print("Hello, world!")
	generate_CSV()
	data = get_data_as_dict("./datos.csv")
	processed_data = get_descriptive_stats(data, "edades")
	print(processed_data)
	write_stats("./datos.csv", processed_data)
