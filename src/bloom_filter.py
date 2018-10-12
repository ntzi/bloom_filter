# This class implements Bloom filter using 2 hash functions: FNV and Murmur.
# Both hash functions are in 32 bits.
# Input:
#   bit_vector_size: (integer) Determine the size of the bit array.
#
#
# More Info:
#
# Computational complexity: Read/Write = O(n)
#   That's because the complexity is growing linearly together with the number of hash functions used.
#
# The false positive rate will be approximately (1-e^(-kn/m))^k, where
# n: number of elements you expect to insert
# k: number of hash functions
# m: number of bits



import pyhash


class BloomFilter:

    def __init__(self, bit_vector_size):

        self.bit_vector_size = bit_vector_size

        # The size of the bit_vector must be positive
        if bit_vector_size <= 0:
            raise ValueError("Bit vector too small.")

        # Initialize vector with all zeros.
        self.bit_vector = [False] * self.bit_vector_size
        # Define the hash functions to use.
        self.hash_functions = [pyhash.fnv1_32(), pyhash.murmur1_32()]
        # Number of hash functions used.
        self.number_of_hashes = len(self.hash_functions)


    # Store a new string.
    def add(self, input_string):
        for i in range(self.number_of_hashes):
            # For the given input, calculate the index in the bit_vector it corresponds to.
            index = self.hash_functions[i](input_string) % self.bit_vector_size

            self.bit_vector[index] = True


    # Search if a string is stored.
    def search(self, input_string):
        for i in range(self.number_of_hashes):
            # Find the position in the bit_vector for the input string.
            true_bit_position = self.hash_functions[i](input_string) % self.bit_vector_size

            # If the position in bit_vector for at least one hash function is not True, then the string does not exist.
            if self.bit_vector[true_bit_position] is not True:
                print("No, the element isn't there.")
                return False

        # If the positions in bit_vector for all hash functions are True, then the string exists.
        print("Maybe the element is there.")
        return True





bloom = BloomFilter(bit_vector_size=10)
bloom.add("just_some_text")
bloom.search("just_some_text") # returns 'Maybe the element is there.'
bloom.search("new_text") # returns 'No, the element isn't there.'

# bloom.add("hey")
# bloom.add("car")
#
# # print(bloom.bit_vector)
# bloom.search("hi")
# bloom.search("hey")
# bloom.search("car")
# bloom.search("nsd")

# murmur_hash = bloom.hash_murmur(string)
# fnv_hash = bloom.hash_fnv(string)

# print(fnv_hash % 14)
# print(murmur_hash % 14)
#
# print(murmur_hash)
# print(fnv_hash)

