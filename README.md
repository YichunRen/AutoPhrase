# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

### Docker: joeyhou10/dsc180_docker_hw
#### Note: The docker uses dsmlp base container. Please login to a dsmlp jumpbox before entering the command below.
```
launch-scipy-ml.sh -i joeyhou10/dsc180_docker_hw
```

### Default Run (run all the targets)
```
python run.py
```
##### Note: The first four targets' parameters could be changed in the corresponding configuration files
### Target 1: Prepare data
```
python run.py data_prep
```
### Target 2: Run autophrase
```
python run.py autophrase
```

### Target 3: Run EDA
The writings in the output html file explain the statistics of DBLP.txt dataset and its AutoPhrase results. Only look the graphs/tables if you use another dataset.
```
python run.py eda
```
### Target 4: Run Report 
- Note: 
  - This report is futher exploration on AutoPhrase results. Paper report link is stored in references.
  - Report requires manual labeling high-quality phrases. The result CSV file for DBLP.txt is stored in references directory and the result CSV file for test_raw.txt is stored in test directory.
- The writings in the output html file explain and investigate AutoPhrase results of DBLP.txt dataset. Only look the graphs/tables if you use another dataset.
```
python run.py report
```
### Target 5: Test All previous targets on test data
Note: For the test run, raw test data is in test/testdata directory.
```
python run.py test
```
### Target 6: Run All the targets
```
python run.py all
```

### Target 7: Reset
Reset the run if you want to rerun the whole repo or start a new run with another dataset
```
python run.py reset
```
models/domains directory contains the autophrase results for different scientific domains and topics

## Responsbilities: Yichun and Joey equally contributed to the repo.
