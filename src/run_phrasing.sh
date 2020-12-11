#!/bin/bash

# Note: this is the file that handles the running time

######### Setting runtime variables #########
DATA_DIR=data
MODELS_DIR=data/models/
MODEL=${MODEL:- ${MODELS_DIR}/DBLP}
DEFAULT_TRAIN=${DATA_DIR}/raw/DBLP.txt
RAW_TRAIN=$1
#RAW_TRAIN=${RAW_TRAIN:- $DEFAULT_TRAIN}

FIRST_RUN=${FIRST_RUN:- 1}
ENABLE_POS_TAGGING=${ENABLE_POS_TAGGING:- 1}
MIN_SUP=${MIN_SUP:- 10}
THREAD=${THREAD:- 10}
MAX_POSITIVES=-1
LABEL_METHOD=DPDN

# mkdir /autophrase/data/EN
# cp /autophrase/data/raw/* /autophrase/data/EN/

mkdir data/EN
cp data/raw/* data/EN/
cp test/testdata/* data/EN/

# ln -s data/tmp tmp
# echo 'Model dir:'
# echo ${MODEL}

######### Tokenization #########
TOKENIZER="-cp .:resources/AutoPhrase/tools/tokenizer/lib/*:tools/tokenizer/resources/:tools/tokenizer/build/ Tokenizer"
TOKEN_MAPPING=tmp/token_mapping.txt

if [ $FIRST_RUN -eq 1 ]; then
    echo ${green}===Tokenization===${reset}
    TOKENIZED_TRAIN=tmp/tokenized_train.txt
    echo -ne "Current step: Tokenizing input file...\033[0K\r"
    time java $TOKENIZER -m train -i $RAW_TRAIN -o $TOKENIZED_TRAIN -t $TOKEN_MAPPING -c N -thread $THREAD
fi

LANGUAGE=`cat tmp/language.txt`
#LABEL_FILE=tmp/labels.txt
LABEL_FILE=$2

if [ $FIRST_RUN -eq 1 ]; then
    echo -ne "Detected Language: $LANGUAGE\033[0K\n"
    TOKENIZED_STOPWORDS=tmp/tokenized_stopwords.txt
    TOKENIZED_ALL=tmp/tokenized_all.txt
    TOKENIZED_QUALITY=tmp/tokenized_quality.txt
    STOPWORDS=$DATA_DIR/$LANGUAGE/stopwords.txt
    ALL_WIKI_ENTITIES=$DATA_DIR/$LANGUAGE/wiki_all.txt
    QUALITY_WIKI_ENTITIES=$DATA_DIR/$LANGUAGE/wiki_quality.txt
    echo -ne "Current step: Tokenizing stopword file...\033[0K\r"
    java $TOKENIZER -m test -i $STOPWORDS -o $TOKENIZED_STOPWORDS -t $TOKEN_MAPPING -c N -thread $THREAD
    echo -ne "Current step: Tokenizing wikipedia phrases...\033[0K\n"
    java $TOKENIZER -m test -i $ALL_WIKI_ENTITIES -o $TOKENIZED_ALL -t $TOKEN_MAPPING -c N -thread $THREAD
    java $TOKENIZER -m test -i $QUALITY_WIKI_ENTITIES -o $TOKENIZED_QUALITY -t $TOKEN_MAPPING -c N -thread $THREAD
fi

######### POS Tagging #########

if [[ $RAW_LABEL_FILE = *[!\ ]* ]]; then
	echo -ne "Current step: Tokenizing expert labels...\033[0K\n"
	java $TOKENIZER -m test -i $RAW_LABEL_FILE -o $LABEL_FILE -t $TOKEN_MAPPING -c N -thread $THREAD
else
	echo -ne "No provided expert labels.\033[0K\n"
fi

if [ ! $LANGUAGE == "JA" ] && [ ! $LANGUAGE == "CN" ]  && [ ! $LANGUAGE == "OTHER" ]  && [ $ENABLE_POS_TAGGING -eq 1 ] && [ $FIRST_RUN -eq 1 ]; then
    echo ${green}===Part-Of-Speech Tagging===${reset}
    RAW=tmp/raw_tokenized_train.txt
    export THREAD LANGUAGE RAW
    bash resources/AutoPhrase/tools/treetagger/pos_tag.sh
    mv tmp/pos_tags.txt tmp/pos_tags_tokenized_train.txt
fi

######### AutoPhrasing #########

echo ${green}===AutoPhrasing===${reset}

if [ $ENABLE_POS_TAGGING -eq 1 ]; then
    time ./bin/segphrase_train \
        --pos_tag \
        --thread $THREAD \
        --pos_prune ${DATA_DIR}/BAD_POS_TAGS.txt \
        --label_method $LABEL_METHOD \
		--label $LABEL_FILE \
        --max_positives $MAX_POSITIVES \
        --min_sup $MIN_SUP
else
    time ./bin/segphrase_train \
        --thread $THREAD \
        --label_method $LABEL_METHOD \
		--label $LABEL_FILE \
        --max_positives $MAX_POSITIVES \
        --min_sup $MIN_SUP
fi

echo ${green}===Saving Model and Results===${reset}

cp tmp/segmentation.model ${MODEL}/segmentation.model
cp tmp/token_mapping.txt ${MODEL}/token_mapping.txt
cp tmp/language.txt ${MODEL}/language.txt

#########  Generating Output #########

echo ${green}===Generating Output===${reset}
java $TOKENIZER -m translate -i tmp/final_quality_multi-words.txt -o ${MODEL}/AutoPhrase_multi-words.txt -t $TOKEN_MAPPING -c N -thread $THREAD
java $TOKENIZER -m translate -i tmp/final_quality_unigrams.txt -o ${MODEL}/AutoPhrase_single-word.txt -t $TOKEN_MAPPING -c N -thread $THREAD
java $TOKENIZER -m translate -i tmp/final_quality_salient.txt -o ${MODEL}/AutoPhrase.txt -t $TOKEN_MAPPING -c N -thread $THREAD
