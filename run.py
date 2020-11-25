import os
import json
import sys
sys.path.insert(0, 'src/eda')
from utils import convert_notebook

def initialization():

    try:
        with open("src/runtime.json", "r") as read_file:
            print("=> Loading runtime status...")
            runtime_status = json.load(read_file)
        read_file.close()
    except:
        print('=> Failed to read runtime status! Check if you have "runtime.json in config/ !"')
        return

    if runtime_status['initialzed'] == 0:
        # Setting up environment
        print(">>>>>>>>>>>>>>>>>>>>>>>> Initialization... <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        command = './src/setup/running_resources.sh'
        os.system(command)
        runtime_status['initialzed'] = 1

    # Saving runtime status
    with open("src/runtime.json", "w") as outfile:
        json.dump(runtime_status, outfile)
    return runtime_status

def data_prep(runtime_status):
    if runtime_status['data_prep'] == 0:
        print('  => building data_prep...')
        runtime_status['data_prep'] = 1
    else:
        print('  => data_prep has been built already!')
        return

    ############  Preparing Data ############
    print(">>>>>>>>>>>>>>>>>>>>>>>> Running data preparation... <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
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
        command = './src/data/data_prep.sh'

        os.system(command)
        print('  Finished downloading DBLP.txt!')

def compile(runtime_status):
    if runtime_status['data_prep'] == 0:
        print('  => build data_prep first...')
        data_prep(runtime_status)
        runtime_status['data_prep'] = 1
    print(">>>>>>>>>>>>>>>>>>>>>>>> Preparing model & compiling... <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    command = 'cp src/setup/compile.sh . ;\
                bash compile.sh; rm compile.sh'
    os.system(command)

def autophrase(runtime_status):
    # Check compiling status
    if runtime_status['compile'] == 0:
        print('  => compile first...')
        compile(runtime_status)
        runtime_status['compile'] = 1

    # parsing run time parameters
    try:
        with open("config/method-params.json", "r") as read_file:
            print("=> Loading method-params.json...")
            method_params = json.load(read_file)
        read_file.close()
    except:
        print('=> Failed to read file: method-params.json')
        return
    print(">>>>>>>>>>>>>>>>>>>>>>>> Running AutoPhrase... <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    
    if runtime_status['testing'] == 1:
        print(" => Running test data...")
        method_params['RAW_TRAIN'] = "data/EN/test_raw.txt"
        
    command = 'cp src/run_phrasing.sh . ; ./run_phrasing.sh '
    for key in method_params.keys():
        command += key
        command += '='
        command += str(method_params[key])
        command += ' '
    print('  => Running command:', command)
    os.system(command)


    runtime_status['autophrase'] = 1

def cleanup():
    command = './src/setup/cleanup.sh'
    os.system(command)
    os.system('rm -rf models')
    os.system('rm -rf data/raw')
    os.system('rm -rf data/models')
    os.system('mv data/out/DBLP data/out/AutoPhrase_Result')

def run_eda(runtime_status):
    if runtime_status['autophrase'] == 0:
        print('  => run autophrase first...')
        autophrase(runtime_status)
        runtime_status['autophrase'] = 1
    command = 'cp -r data/models/* data/out/'
    os.system(command)

    print(">>>>>>>>>>>>>>>>>>>>>>>> Running EDA... <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    from eda import generate_stats
    eda_config = json.load(open('config/eda-params.json'))
    
    if runtime_status['testing'] == 1:
        #eda_config['data_path'] = "test/testdata/test_raw.txt"
        eda_config['data_path'] = "/EN/test_raw.txt"
    
    generate_stats(**eda_config)
    # execute notebook / convert to html
    convert_notebook(**eda_config)

    cleanup()

def main():
    model_name = 'DBLP'
    runtime_status = initialization()

    # Getting the target
    # If no target is given, then run 'all'
    if len(sys.argv) == 1:
        target = 'all'
    else:
        target = sys.argv[1]

    # Building corresponding target
    if target == "data_prep":
        data_prep(runtime_status)

    # run the method
    elif target == "autophrase":
        autophrase(runtime_status)

    #run eda, the result will be saved as html in data/out
    elif target == "eda":
        run_eda(runtime_status)


    elif target == "all":
        run_eda(runtime_status)
        
    elif target == "test":
        runtime_status['testing'] = 1
        run_eda(runtime_status)
        runtime_status['testing'] = 0
        print(" => Done! See your test result in data directory.")
        
    #reset the repo
    elif target == "reset_run":
        os.system('git reset --hard')
            
    # Saving runtime status
    with open("src/runtime.json", "w") as outfile:
        json.dump(runtime_status, outfile)

main();
