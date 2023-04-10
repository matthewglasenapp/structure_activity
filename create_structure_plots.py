import os 

parent_dir = os.getcwd()
structure_directory = os.getcwd() + "/structure/"
structure_results_dir = os.getcwd() + "/structure_results/"
distruct_dir = os.getcwd() + "/distruct/"
distruct_results_dir = os.getcwd() + "/structure_plots/"

distruct = input("Enter name of your distruct exectuable program (case sensitive):")
structure = input("Enter the name of your structure executable program (case sensitive):")

def run_structure_iteratively():
	# Number of clusters to try. 
	k = [2,3,4,5,6]
	
	for n in k:
		os.system("./" + structure + " -m mainparams -e extraparams -K " + str(n) + " -L 6 -N 43 -i turtles.txt -o " + structure_results_dir + "turtles_" + str(n) + ".txt")

def create_file_of_results_files():
	os.system('find "$(pwd)" -name "*.txt_f" -type f > results_files.txt')
	os.system("mv results_files.txt " + parent_dir)

def parse_structure_output():
	for file_path in open("results_files.txt","r").read().splitlines():
		number_clusters = file_path.split(".txt")[0].split("turtles_")[1]
		with open(file_path) as file:
			inputs = file.read().splitlines()

			for index, item in enumerate(inputs):
				if "Number of" in item:
					start = index + 3
					stop = index + 8
			for line in inputs[start:stop]:
				with open(distruct_dir + "turtles_" + number_clusters + ".popq","a") as file3:
					file3.write(line + "\n")
					file3.close()
			
			for index, item in enumerate(inputs):
				if "Pop:  Inferred clusters" in item:
					start = index + 1
					stop = index + 44
			for line in inputs[start:stop]:
				with open(distruct_dir + "turtles_" + number_clusters + ".indivq","a") as file3:
					file3.write(line + "\n")
					file3.close()

def run_distruct_iteratively():
	k = [2,3,4,5,6]

	for n in k:
		os.system("./" + distruct + " -K " + str(n) + " -M 5" + " -N 43" + " -p turtles_" + str(n) + ".popq " + "-i turtles_" + str(n) + ".indivq " + " -b turtles.names" + " -o " + distruct_results_dir + "turtles_" + str(n) + "_figure")

def delete_intermediate_files():
	os.chdir(parent_dir)
	os.system('find ./distruct/ -type f -name "*.popq" -delete')
	os.system('find ./distruct/ -type f -name "*.indivq" -delete')
	os.system("rm results_files.txt")

def main():
	os.chdir(structure_directory)
	os.mkdir(structure_results_dir)
	run_structure_iteratively()
	os.chdir(structure_results_dir)
	create_file_of_results_files()
	os.chdir(parent_dir)
	parse_structure_output()
	os.chdir(distruct_dir)
	os.mkdir(distruct_results_dir)
	run_distruct_iteratively()
	delete_intermediate_files()
	

if __name__ == "__main__":
	main()
