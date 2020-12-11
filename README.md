# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## To Run
#### Warning: The pipeline only support a full run for one dataset now. Please reload the repo if you want to try another dataset (including test run).

### Docker
#### Note: The docker uses dsmlp base container. Please login to a dsmlp jumpbox before entering the command below.
```
launch-scipy-ml.sh -i joeyhou10/dsc180_docker_hw
```

### Default Run (run all the targets)
```
python run.py
```
##### Note: The first three targets' parameters could be changed in the corresponding configuration files
### Target 1: Prepare data
```
python run.py data_prep
```
### Target 2: Run autophrase
```
python run.py autophrase
```
**Note:Target 3&4 require the AutoPhrase results.**
### Target 3: Run EDA
The writings in the output html file explain the statistics of DBLP.txt dataset and its AutoPhrase results. Only look the graphs/tables if you use another dataset.
```
python run.py eda
```
### Target 4: Run Report 
The writings in the output html file explain and investigate AutoPhrase results of DBLP.txt dataset. Only look the graphs/tables if you use another dataset.
```
python run.py report
```
### Target 5: Run All previous targets on test data
```
python run.py test
```
### Target 6: Run All the targets
```
python run.py all
```
