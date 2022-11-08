class HashTable:
    def __init__(self, num_buckets):
        self.internalArray = [[] for _ in range(num_buckets)]

    def get(self, key):
        total_key = self.calc_key(key)
        total_key %= len(self.internalArray)
        for i in range(0, len(self.internalArray[total_key])):
            if self.internalArray[total_key][i] == [key]:
                return self.internalArray[total_key][i]
        return self.internalArray[total_key]

    def put(self, key, value):
        total_key = self.calc_key(key)
        bucket_index = total_key % len(self.internalArray)

        self.internalArray[bucket_index].append((key, value))

    def calc_key(self, key):
        parts_of_key = []
        total_key = 0
        for i in range(0, len(key)):
            parts_of_key += [ord(key[i])]

        for i in range(0, len(parts_of_key)):
            total_key += parts_of_key[i] * (31 ^ i)

        return total_key

    def __str__(self):
        return self.internalArray.__str__()


ht = HashTable(127)
ht.put("Hello", "I said Hello")
ht.put("dog", "Woof")
ht.put("eat", "Yummy")

print(ht.get("Hello"))
print(ht.get("dog"))
print(ht)
