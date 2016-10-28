

def extract_all_ngram(string, n):
    '''Extract all n-gram from the string

    Parameters
    ---------------
    string : str
    n : integer

    Returns
    ---------------
    iterator of n-gram
    length of iterator
    '''
    tuples_ngram = zip(*[string[i:] for i in range(n)])
    return (map(lambda x: ''.join(x), tuples_ngram), len(string) - n + 1)


def extract_topn_ngram(lines_str, width_ngram, n_extract):
    '''

    Example
    --------------
    vocabulary_all_true = []
    for width, n_extract in n_extract_tuple:
        all_ngrams = extract_topn_ngrams(lines_str, width_ngram=width, n_extract=n_extract)
        vocabulary_all_true.extend(all_ngrams)

    size_vocabulary_all_true = len(vocabulary_all_true)
    dict_vocabulary_all_true = dict(zip(vocabulary_all_true, range(size_vocabulary_all_true)))

    len(set(vocabulary_all_true) & set(vocabulary_all))/len(vocabulary_all)
    '''
    ngrams, n_ngrams = extract_all_ngram(lines_str, n=width_ngram)
    counter = Counter(ngrams)
    common_counter = counter.most_common(n_extract)
    vocabulary = [c for c, n in common_counter]
    n_all_ngrams = len(counter)
    coverage = sum([n for c, n in common_counter]) / n_ngrams

    print('min count   :', common_counter[-1])
    print('# of {0}-gram : {1}'.format(width_ngram, n_all_ngrams))
    print('Coverage    : {0}\n'.format(coverage))

    return vocabulary


def extract_topn_ngram_lossycounting(line_str, width_ngram, n_extract_tuple):
    def each_n_ngram(l):
        width = l[0]
        n_extract = l[1]

        lc = sembei.utils.counting.lossycounting_ngram(
            lines_str, n_ngram=width_ngram, epsilon=1e-6, support_threshold=1e-6)

        count_dict_sorted = sorted(lc.count_dict.items(), key=lambda x: x[1], reverse=True)
        count_dict_extracted = count_dict_sorted[0:n_extract]
        vocabulary = [k for k, v in count_dict_extracted]

        coverage = sum([v for k, v in count_dict_extracted]) / lc.n_char

        min_count = count_dict_extracted[-1]

        print('min count   :', min_count, lc.error_dict[min_count[0]])
        print('# of {0}-gram : {1}'.format(width, len(lc.count_dict)))
        print('Coverage    : {0}\n'.format(coverage))

        return vocabulary

    try:
        pool = multiprocessing.Pool(7)
        callback = pool.map(each_n_ngram, n_extract_tuple)
    finally:
        pool.close()
        pool.join()

    vocabulary_all = []
    for c in callback:
        vocabulary_all.extend(c)
