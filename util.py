import re
import heapq
from math import log10

def get_word(line):
    '''
    line has 'word:posting_list' format and we need to extract the word
    '''
    word = ''
    for ch in line:
        if (ch == ':'):
            break
        word += ch

    return word


def get_tf_value(posting):
    '''
    Returns the tf_value for a posting list
    Any posting is of the form <id>(<character><number>)+

    @param posting : C{str}
    @return : C{int}
    '''
    weight = {'t' : 2, 'b' : 1.5, 'c': 0.75, 'i' : 1.5, 'r' : 0.5, 'e' : 0.5}

    overall_freq = 0

    obj = posting.split('r')
    if len(obj) == 2:
        overall_freq += weight['r'] * int(obj[1])

    obj = obj[0].split('e')
    if len(obj) == 2:
        overall_freq += weight['e'] * int(obj[1])

    obj = obj[0].split('c')
    if len(obj) == 2:
        overall_freq += weight['c'] * int(obj[1])

    obj = obj[0].split('i')
    if len(obj) == 2:
        overall_freq += weight['i'] * int(obj[1])

    obj = obj[0].split('b')
    if len(obj) == 2:
        overall_freq += weight['b'] * int(obj[1])

    obj = obj[0].split('t')
    if len(obj) == 2:
        overall_freq += weight['t'] * int(obj[1])

    tf = log10(1 + overall_freq)

    return tf


def add_tfidf_value_posting(posting, tfidf_value):
    '''
    Any posting is of the form <id>(<character><number>)+
    Returns <id>,<ifidf_value>(<character><number>)+
    We also return the doc_id value so that we can sort based on that and
    merging the posting lists would be easier at query time
    '''

    # Finding the index just after the doc id ends
    for i in range(len(posting)):
        if not posting[i].isdigit():
            break

    doc_id = int(posting[:i])
    modified_posting = str(doc_id) + ',' + str(tfidf_value) + posting[i:]

    return (doc_id, modified_posting)


def get_champions_list(posting_list, total_number_documents, num_champions):
    '''
    This function takes the posting list for a term and for each posting
    adds the tf-idf value.
    num_champions denotes the maximum number of docs in the champion list

    @param posting_list : C{str}
    @return : C{str} representing the tfidf added posting list
    '''

    postings = posting_list.split('|')
    idf_value = log10(total_number_documents) - log10(len(postings))

    for i in range(len(postings)):
        tf_value = get_tf_value(postings[i])
        tfidf_value = round(tf_value * idf_value, 2)
        # Multiplying by -1 as there is no max heap in python
        postings[i] = (-1 * tfidf_value, postings[i])

    # Modified postings have the tfidf value present as part of posting
    modified_postings = []
    heapq.heapify(postings)
    for i in range(min(num_champions, len(postings))):
        posting_obj = heapq.heappop(postings)
        tfidf_value = posting_obj[0] * -1
        posting = posting_obj[1]
        modified_posting_obj = add_tfidf_value_posting(posting, tfidf_value)
        modified_postings.append(modified_posting_obj)

    # Below will make the champion list sort by the doc_id (As in tuple first entry is doc_id)
    modified_postings.sort()
    for i in range(len(modified_postings)):
        modified_postings[i] = modified_postings[i][1]
    modified_postings = '|'.join(modified_postings)

    return modified_postings
