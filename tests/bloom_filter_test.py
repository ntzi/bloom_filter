# Test the Bloom filter by validating the final results for random strings.

import sys
sys.path.insert(0, '../src')
import random
import string
import logging
from bloom_filter import BloomFilter


# Set up the log file
logging.basicConfig(format='[%(asctime)s] %(message)s', filename='tests.log', level=logging.DEBUG)


# The the whole bloom filter
class BloomFilterTest:

    def __init__(self):
        return



    # Test the whole filter.
    def general_test(self):
        # Set the size of the bit vector.
        bit_vector_size = 20

        # Words to be added.
        words_saved = ["this", "nonsense", "senior", "story", "jokes", "a", "young", "a", "one", "to", "impress", "dev", "with",
                       "trying", "a", "is", "of"]

        # Words that will not be added.
        words_not_saved = ["These", "words", "do", "not", "exist", "in", "the", "filter"]

        bloom = BloomFilter(bit_vector_size)

        # Add words to the filter.
        for word in range(len(words_saved)):
            bloom.add(words_saved[word])



        number_of_true_positive = 0
        number_of_true_negative = 0
        number_of_false_positive = 0
        number_of_false_negative = 0

        # Check all the added words.
        for i in range(len(words_saved)):
            # If the word is found the we have true positive result.
            if bloom.search(words_saved[i]):
                number_of_true_positive += 1
            # If the word is not found then there is a bug in the implementation.
            else:
                number_of_false_negative += 1


        # Check all the non added words
        for i in range(len(words_not_saved)):
            # If the word is found the we have false positive result.
            if bloom.search(words_not_saved[i]):
                number_of_false_positive += 1
            # If the word is not found the we have true negative result.
            else:
                number_of_true_negative += 1


        print("Number of true positive results: ", number_of_true_positive)
        print("Number of true negative results: ", number_of_true_negative)
        print("Number of false positive results: ", number_of_false_positive)
        print("Number of false negative results: ", number_of_false_negative)

        # A bloom filter should never return false negative, if it does raise an error.
        if number_of_false_negative != 0:
            logging.error("general_test: FAIL. Bloom filter return false negative.")
            return

        logging.info("general_test: PASS")



    # Test the add() function by adding multiple alphanumeric strings in a variety of sizes.
    def add_test(self):
        try:
            for i in range(1000):
                # Pick a random number for string size.
                string_size = random.randrange(0, 10000)
                # Create random alphanumeric strings.
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_size))

                # The size of the filter is not important in this test.
                bloom = BloomFilter(bit_vector_size = 10)
                # Add the random string to the filter.
                bloom.add(random_string)

            logging.info("add_test: PASS")

        except ValueError:
            logging.error("add_test: FAIL. A random string caused an error.")






if __name__ == '__main__':
    BloomFilterTest().general_test()
    BloomFilterTest().add_test()