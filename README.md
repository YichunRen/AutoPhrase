# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## To Run

### Docker
```

docker run joeyhou10/dsc180_docker_hw

```

### Default Run (run all the targets)
```
python run.py
```
##### Note: All the targets' parameters could be changed in the corresponding configuration files
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
