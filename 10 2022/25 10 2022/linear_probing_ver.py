class HashTable:
    def __init__(self, num_buckets):
        self.internalArray = [[] for _ in range(num_buckets)]

    def get(self, key):
        total_key = self.calc_key(key)
        bucket_index = total_key % len(self.internalArray)
        original_index = bucket_index
        done = False
        count = 0
        while done is False:
            if self.internalArray[bucket_index] == []:
                pass
            else:
                if (self.internalArray[bucket_index])[0][0] == key:
                    done = True

            if done is True:
                return self.internalArray[bucket_index]

            elif bucket_index == len(self.internalArray) - 1:
                bucket_index = 0

            else:
                bucket_index += 1

            if bucket_index == original_index and count >= 1:
                return "The specified key is not in this hash table"
            count += 1
        return self.internalArray[bucket_index]

    def put(self, key, value):
        total_key = self.calc_key(key)
        bucket_index = total_key % len(self.internalArray)
        original_index = bucket_index
        done = False
        while done is False:
            done = self.check_index_X(bucket_index, [])
            if done is True:
                done = True
                self.internalArray[bucket_index].append((key, value))

            elif bucket_index == len(self.internalArray) - 1:
                bucket_index = 0

            else:
                bucket_index += 1

            if bucket_index == original_index:
                done = True

    def calc_key(self, key):
        parts_of_key = []
        total_key = 0
        for i in range(0, len(key)):
            parts_of_key += [ord(key[i])]

        for i in range(0, len(parts_of_key)):
            total_key += parts_of_key[i] * (31 ^ i)

        return total_key

    def check_index_X(self, bucket_index, X):
        if self.internalArray[bucket_index] == X:
            return True
        else:
            return False

    def __str__(self):
        return self.internalArray.__str__()


ht = HashTable(10)
ht.put("Hello", "I said Hello")
ht.put("dog", "Woof")
ht.put("eat", "Yummy")

print(ht.get("Hello"))
print(ht.get("dog"))
print(ht.get("eat"))
print(ht)
