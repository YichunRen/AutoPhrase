import os
import json
import sys

def data_prep():
	############  Downloading Resources ############
	print("========= Step 1. Collecting needed resources... =========")
	command = './resources.sh'
	os.system(command)

	############  Preparing Data ############
	print("========= Step 2. Running data preparation... =========")
	# Check if data-params.json is ready
	try:
		with open("config/data-params.json", "r") as read_file:
		    print("=> Loading data-params.json...")
		    data_params = json.load(read_file)
		read_file.close()
	except:
		print('=> Failed to read file: data-params.json')
		return

	# Check if 'default_data' exists
	default_data = False
	if 'default_data' in os.listdir('.'):
		default_data = True

	# Check if txt files are ready
	data_dir = data_params['data_dir']
	data_dict = data_params['data']
	found_lst = []
	unfount_lst = []
	download_needed = False
	for key, file_lst in data_dict.items():
		for filepath in file_lst:
			filepath = data_dir + filepath
			if default_data:
				filepath = filepath.replace('data', 'default_data')
			try:
				tmp_file = open(filepath, "r")
				tmp_file.close()
				found_lst.append(filepath)
			except:
				unfount_lst.append(filepath)
				if 'DBLP.txt' in filepath:
					download_needed = True

	if len(unfount_lst) == 0:
		print('=> Done checking txt files! All needed files are found!')
	else:
		print('=> Done checking txt files! The following files are not found!')
		for fp in unfount_lst:
			print('  - ' + fp.split('/')[-1])

	# Downloading data
	if download_needed:
		command = './data_prep.sh'
		# command = 'sudo docker run -v $PWD/models:/autophrase/models -it -e ENABLE_POS_TAGGING=1 -e MIN_SUP=30 -e THREAD=10 joeyhou10/autophrase_replication; ./auto_phrase.sh'

		os.system(command)
		print('  Finished downloading DBLP.txt!')

def main():
	if len(sys.argv) == 1:
		target = 'all'
	else:
		target = sys.argv[1]

	if target == "data_prep":
		data_prep()
	elif target == "all":
		data_prep()

main();
