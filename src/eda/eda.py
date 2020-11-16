import pandas as pd
import numpy as np
import seaborn as sns
from collections import defaultdict
from scipy.stats import skew
from tqdm import tqdm # Visualization of loop progress
import matplotlib.pyplot as plt
import os

# import data
raw_train_fp = 'data/raw/DBLP.txt'
dblp_raw = open(raw_train_fp, 'r')
# result
output_dir = 'data/out/DBLP/'
multi_word = open(output_dir + 'AutoPhrase_multi-words.txt').readlines()
single_word = open(output_dir + 'AutoPhrase_single-word.txt').readlines()

print(' => Generating Data for eda')
#save the count result into a dataframe and convert it into csv
def count_frequency(outdir):
    print('  => Checking raw frequency count...')
    #find all documents
    tmp_doc = ''
    all_doc = []
    # for sent in tqdm(dblp_raw):
    while True:
        sent = dblp_raw.readline()
        if not sent:
            break
        if sent == '.\n':
            if len(tmp_doc) != 0:
                all_doc.append(tmp_doc.replace('\n', ' '))
            tmp_doc = ''
        elif sent != '\n':
            tmp_doc += sent

    #find all sentences
    all_sent = []
    for doc in tqdm(all_doc):
        for sent in doc.split('. '):
            if len(sent) != 0:
                all_sent.append(sent)

    #find all tokens
    all_token = []
    for sent in tqdm(all_sent):
        for token in sent.split():
            if len(token) != 0:
                all_token.append(token)

    df_counts = pd.DataFrame()
    df_counts['Type'] = ['Document', 'Sentence', 'Token']
    df_counts['Count'] = [len(all_doc), len(all_sent), len(all_token)]

    df_doc = pd.DataFrame()
    df_doc['Document'] = all_doc
    df_sent = pd.DataFrame()
    df_sent['Sentence'] = all_sent
    #df_token = pd.DataFrame(all_token)

    df_counts.to_csv(os.path.join(outdir, 'count_stats.csv'))
    df_doc.to_csv(os.path.join(outdir, 'all_doc.csv'))
    df_sent.to_csv(os.path.join(outdir, 'all_sent.csv'))
    #df_token.to_csv(os.path.join(outdir, 'all_token.csv'))

    return df_doc, df_sent


def check_doc_dist(df_doc, outdir):
    print('  => Checking document info...')
    all_doc = list(df_doc['Document'])
    doc_length = [len(doc.split()) for doc in tqdm(all_doc)]
    skew_value = skew(doc_length)
    perc_10, perc_25, perc_50, perc_75, perc_90 = np.percentile(doc_length, 10), np.percentile(doc_length, 25), np.percentile(doc_length, 50), np.percentile(doc_length, 75), np.percentile(doc_length, 90)
    doc_mean = np.mean(doc_length)
    outlier_cutoff = perc_75 + 1.5 * (perc_75 - perc_25)
    outlier_count = 0
    outlier_samples = []
    for i in tqdm(range(len(doc_length))):
        if doc_length[i] > outlier_cutoff:
            outlier_count += 1
            if len(outlier_samples) < 20:
                outlier_samples.append(all_doc[i])

    df_doc_stats = pd.DataFrame()
    df_doc_stats['Statistics'] = ['Skewness', 'Percentile_10', 'Percentile_25', 'Percentile_50',
                                  'Percentile_75', 'Percentile_90', 'Mean', 'Outlier_Cutoff', 'Num_Outliers']
    df_doc_stats['Value'] = [skew_value, perc_10, perc_25, perc_50, perc_75, perc_90, doc_mean, outlier_cutoff, outlier_count]
    df_doc_stats.to_csv(os.path.join(outdir, 'doc_stats.csv'))


def check_sent_dist(df_sent, outdir):
    print('  => Checking sentence info...')
    all_sent = list(df_sent['Sentence'])
    sent_length = [len(sent.split()) for sent in tqdm(all_sent)]
    skew_value = skew(sent_length)
    perc_10, perc_25, perc_50, perc_75, perc_90 = np.percentile(sent_length, 10), np.percentile(sent_length, 25), np.percentile(sent_length, 50), np.percentile(sent_length, 75), np.percentile(sent_length, 90)
    sent_mean = np.mean(sent_length)
    outlier_cutoff = perc_75 + 1.5 * (perc_75 - perc_25)
    outlier_count = 0
    outlier_samples = []
    for i in tqdm(range(len(sent_length))):
        if sent_length[i] > outlier_cutoff:
            outlier_count += 1
            if len(outlier_samples) < 20:
                outlier_samples.append(all_sent[i])

    df_sent_stats = pd.DataFrame()
    df_sent_stats['Statistics'] = ['Skewness', 'Percentile_10', 'Percentile_25', 'Percentile_50',
                                  'Percentile_75', 'Percentile_90', 'Mean', 'Outlier_Cutoff', 'Num_Outliers']
    df_sent_stats['Value'] = [skew_value, perc_10, perc_25, perc_50, perc_75, perc_90, sent_mean, outlier_cutoff, outlier_count]
    df_sent_stats.to_csv(os.path.join(outdir, 'sent_stats.csv'))


def check_token_dist(df_sent, outdir):
    print('  => Checking token info...')
    all_sent = list(df_sent['Sentence'])
    token_count = defaultdict(lambda : 0)
    for sent in tqdm(all_sent):
        for token in sent.split():
            token_count[token] += 1

    token_count_dict = dict(token_count)
    token_count_lst = [pair[1] for pair in tqdm(token_count_dict.items())]
    perc_10, perc_25, perc_50, token_mean, perc_75, perc_90, skew_value = np.percentile(token_count_lst, 10), np.percentile(token_count_lst, 25), np.percentile(token_count_lst, 50), np.mean(token_count_lst),np.percentile(token_count_lst, 75), np.percentile(token_count_lst, 90), skew(token_count_lst)

    in_frequent_tokens = []
    all_token_count = []

    for token_pair in tqdm(token_count_dict.items()):
        all_token_count.append(token_pair[1])
        if token_pair[1] < 5:
            in_frequent_tokens.append(token_pair[0])


    df_all_token = pd.DataFrame()
    df_all_token['Count'] = all_token_count
    #df_infrequent_token = pd.DataFrame(in_frequent_tokens)

    df_all_token.to_csv(os.path.join(outdir, 'all_token_counts.csv'))
    #df_infrequent_token.to_csv(os.path.join(outdir, 'infrequent_token_counts.csv'))

    num_infrequent = len(in_frequent_tokens)
    infrequent_rate = len(in_frequent_tokens) / len(all_token_count)
    num_token = len(all_token_count)
    num_frequent = num_token - num_infrequent

    df_token_stats = pd.DataFrame()
    df_token_stats['Statistics'] = ['Skewness', 'Percentile_10', 'Percentile_25', 'Percentile_50',
                                  'Percentile_75', 'Percentile_90', 'Mean_Count', 'Num_Infrequent',
                                    'Infrequent_Ratio', 'Num_Frequent']
    df_token_stats['Value'] = [skew_value, perc_10, perc_25, perc_50, perc_75, perc_90, token_mean,
                               num_infrequent, infrequent_rate, num_frequent]
    df_token_stats.to_csv(os.path.join(outdir, 'token_stats.csv'))


def check_scores(outdir):
    print('  => Checking output quality scores...')
    multi_word_scores = []
    single_word_scores = []
    for line in multi_word:
        multi_word_scores.append(float(line.split()[0]))
    for line in single_word:
        single_word_scores.append(float(line.split()[0]))

    df_multi_score = pd.DataFrame()
    df_single_score = pd.DataFrame()
    df_multi_score['Scores'] = multi_word_scores
    df_single_score['Scores'] = single_word_scores
    df_multi_score.to_csv(os.path.join(outdir, 'multi_score.csv'))
    df_single_score.to_csv(os.path.join(outdir, 'single_score.csv'))

def generate_stats(outdir, **kwargs):

    os.makedirs(outdir, exist_ok=True)
    df_doc, df_sent = count_frequency(outdir)
    check_doc_dist(df_doc, outdir)
    check_sent_dist(df_sent, outdir)
    check_token_dist(df_sent, outdir)
    check_scores(outdir)

    return
