from essential_generators import DocumentGenerator


def random_sentence(min_n_words=15, max_n_words=20):
    return DocumentGenerator().gen_sentence(min_n_words, max_n_words)



