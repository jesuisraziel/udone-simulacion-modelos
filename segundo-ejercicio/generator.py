from random import randint

def create_age_list():
    ages = []
    for i in range(0,100):
        ages.append(randint(18,25))
    return ages

def generate_CSV():
    ages = create_age_list()
    try:
        with open("./datos.csv","w") as file:
            file.write("Edades\n")
            for edad in ages:
                file.write(str(edad) + '\n')
    except OSError:
        print(error)

if __name__ == "__main__":
    createCSV()