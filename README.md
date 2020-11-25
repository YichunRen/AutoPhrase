# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## To Run

### Entering Docker
```
sudo docker run -v $PWD/data/out:/autophrase/data/out -it joeyhou10/autophrase_replication

docker run yichunren/dsc180a_docker

```

### Default Run (run all the targets)
**Use python3 instead of python because the default python on the docker is python2**
```
python3 run.py
```
##### Note: All the targets' parameters could be changed in the corresponding configuration files
### Target 1: Prepare data
```
python3 run.py data_prep
```
### Target 2: Run autophrase
```
python3 run.py autophrase
```
### Target 3: Run EDA
**The minimum memory of Docker need to be 8GB to run the code now. We will modify the way to read files in the future**
```
python3 run.py eda
```
### Target 4: Run All the targets
```
python3 run.py all
```
