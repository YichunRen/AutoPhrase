# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## To Run
#### Warning: The pipeline only support a full run for one dataset now. Please reload the repo if you want to try another dataset (including test run).

### Docker
#### Note: The docker use dsmlp base container. Please login to a dsmlp jumpbox before entering the command below.
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
### Target 3: Run EDA
```
python run.py eda
```
### Target 4: Run All the targets
```
python run.py all
```
### Target 5: Run All the targets on test data
```
python run.py test
