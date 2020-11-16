# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## To Run

### Entering Docker
```
sudo docker run -v $PWD/models:/autophrase/models -it -e ENABLE_POS_TAGGING=1 -e MIN_SUP=30 -e THREAD=10 joeyhou10/autophrase_replication
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
