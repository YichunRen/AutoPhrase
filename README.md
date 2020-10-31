# DSC180A - Replication Assignment (Fall 2020)
- Note: this is a replication of [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) by Jingbo Shang.

## Checkpoint 1: Data Ingestion

### TO RUN
```
python run.py # This will check and prepare needed data for the project.
```

### Purpose
- The prepared data are stored in data folder for later training, with files for one language in seperate folders.


## Further Functions

### Entering Docker
```
sudo docker run -v $PWD/models:/autophrase/models -it -e ENABLE_POS_TAGGING=1 -e MIN_SUP=30 -e THREAD=10 joeyhou10/autophrase_replication
```

### Default Run
```
./auto_phrase.sh
```

### Responsibilities 

* Joey Hou is responsible for code.
* Yichun Ren is responsible for report.
* Group members discussed the problems together
