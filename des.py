import argparse
from math import log

import pandas as pd


IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S = [
        
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

CD_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

CD_2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

IP_FINAL = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

BYTESIZE = 8
MIN_V = 1 / 1000000


def string_to_bits(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)
        array.extend(binval)
    return array


def binvalue(val, bitsize): 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    
    binval = binval.rjust(bitsize, "0")
    return list(map(int, list(binval)))


def bits_to_string(array):
    res = "".join([chr(int(y,2)) for y in ["".join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])   
    return res


def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]


def bits_to_int(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit

    return out


def binary_entropy(array):
    p = array.count(array[0]) / len(array)
    q = 1 - p
    return round(-p*log(p + MIN_V) - q*log(q + MIN_V), 3)


def mean(array):
    return sum(array) / len(array)


class Des:

    pad_len = 0
    bit_entropy = None
    
    def encrypt(self, key, text):
        return self.run(key, text, encrypt=True)
    
    def decrypt(self, key, text):
        return self.run(key, text, encrypt=False)

    def run(self, key, text, encrypt=True, rounds_count=16):
        key, text_blocks = self.prepare_data(key, text, encrypt)
        keys = self.geretate_keys(key, rounds_count)
        result, intermediate_results = self.process_blocks(
            text_blocks,
            keys,
            encrypt,
            rounds_count
        )
        result = self.postprocessing(result, self.pad_len, encrypt)
        if encrypt:
            self.bit_entropy = self.get_bit_entorpy(intermediate_results)

        return result

    def prepare_data(self, key, text, encrypt=True, bitsize=64):
        if len(key) < BYTESIZE:
            raise "Key must be 8 bytes long!"
        elif len(key) > BYTESIZE:
            key = key[:BYTESIZE]

        if isinstance(key, str):
            key = string_to_bits(key)
        else:
            raise Exception("Key must be a string!")
        if isinstance(text, str):
            if encrypt:
                text, self.pad_len = self.add_padding(text)

            bits = string_to_bits(text)
            text_blocks = nsplit(bits, bitsize)
        else:
            raise Exception("Input data must be a string!")

        return key, text_blocks

    def check_consistency(self, key):
        if isinstance(key, str):
            key = string_to_bits(key)

        for e in range(BYTESIZE - 1, len(key), BYTESIZE):
            s = e - BYTESIZE + 1
            if key[e] == (sum(key[s:e]) + 1) % 2:
                continue
            else:
                return False
        
        return True

    def repair_key(self, key):
        if isinstance(key, str):
            key = string_to_bits(key)
            
        for e in range(BYTESIZE - 1, len(key), BYTESIZE):
            s = e - BYTESIZE + 1
            key[e] = (sum(key[s:e]) + 1) % 2

        return key

    def geretate_keys(self, key, rounds_count=16):
        key = self.permut(key, CD_1)
        left, right = nsplit(key, len(key) // 2)
        keys = []
        for i in range(rounds_count):
            left, right = self.shift(left, right, SHIFT[i])
            tmp = left + right
            keys.append(self.permut(tmp, CD_2))

        return keys

    def process_blocks(self, text_blocks, keys, encrypt=True, rounds_count=16):
        result = []
        intermediate_results = []
        for block in text_blocks:
            intermediate_results.append(block)

            block = self.permut(block, IP)
            left, right = nsplit(block, len(block) // 2)

            for i in range(rounds_count):
                right_expanded = self.permut(right, E)

                if encrypt:
                    index = i
                else:
                    index = rounds_count - 1 - i
                
                tmp = self.xor(keys[index], right_expanded)
                tmp = self.substitute(tmp)                
                tmp = self.permut(tmp, P)
                tmp = self.xor(left, tmp)
                left, right = right, tmp
                intermediate_results.append(right + left)

            result.extend(self.permut(intermediate_results[-1], IP_FINAL))
        
        return result, intermediate_results

    def postprocessing(self, bitlist, pad_len, encrypt=True):
        result = bits_to_string(bitlist)
        if not encrypt:
            result = self.remove_padding(result, pad_len)

        return result

    def get_bit_entorpy(self, blocks):
        res = []
        for block in blocks:
            bytes_ = nsplit(block, BYTESIZE)
            bytes_t = self.transpose(bytes_)
            res.append([binary_entropy(b) for b in bytes_t])

        return res
    
    def transpose(self, matrix):
        return list(map(list, zip(*matrix)))

    def add_padding(self, text):
        pad_len = (BYTESIZE - (len(text) % BYTESIZE)) % BYTESIZE
        return f"{text}{pad_len * chr(pad_len)}", pad_len

    def remove_padding(self, text, pad_len):
        if pad_len == 0:
            return text
        else:
            return text[:-pad_len]

    def permut(self, block, table):
        return [block[x - 1] for x in table]

    def shift(self, left, right, n):
        return left[n:] + left[:n], right[n:] + right[:n]

    def xor(self, t1, t2):
        return [x^y for x, y in zip(t1, t2)]

    def substitute(self, block, split_size=6):
        subblocks = nsplit(block, split_size)

        result = []
        for i, block in enumerate(subblocks):
            row = int(f"{block[0]}{block[-1]}", 2)
            col = bits_to_int(block[1:-1])
            bin_value = binvalue(S[i][row][col], 4)
            result.extend(bin_value)
        
        return result


def main(message_path, key_path, print_info=False, decrypt=False, repair=False):
    with open(message_path, "r") as f:
        message = f.read()

    with open(key_path, "r") as f:
        key = f.read()

    my_des = Des()

    if print_info:
        print("Key:         ", key)
        
        if not my_des.check_consistency(key):
            if repair:
                key = bits_to_string(my_des.repair_key(key))
                print("New key:     ", key)
            else:
                raise Exception("Corrupted key!")
            

        encrypted = my_des.encrypt(key, message)
        decrypted = my_des.decrypt(key, encrypted)
        print("Message:     ", message)
        print("Encrypted:   ", encrypted)    
        print("Decrypted:   ", decrypted)

        df = pd.DataFrame(my_des.bit_entropy)
        df.to_csv("bits.csv")
        # print("Mean entropy:", mean(my_des.bit_entropy))
        # print(*my_des.bit_entropy, sep="\n")
    else:
        if not my_des.check_consistency(key):
            if repair:
                key = bits_to_string(my_des.repair_key(key))
                with open(key_path, "w") as f:
                    f.write(key)
                    print("Keyword reparired.")
            else:
                raise Exception("Corrupted key!")

        if decrypt:
            with open("pad_len.txt", "r") as f:
                my_des.pad_len = int(f.read())
                print("Padding saved.")
            res = my_des.decrypt(key, message)
            path = message_path.replace(".txt", "_decrypted.txt")
        else:
            res = my_des.encrypt(key, message)
            path = message_path.replace(".txt", "_encrypted.txt")
            with open("pad_len.txt", "w") as f:
                f.write(str(my_des.pad_len))
                print("Padding saved.")

        with open(path, "w") as f:
            f.write(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run encryption with DES.")
    parser.add_argument(
        "-m", "--message", default="message.txt", dest="message", help="Message to enctrypt."
    )
    parser.add_argument(
        "-k", "--key", default="key.txt", dest="key", help="Key for the encryption."
    )
    parser.add_argument(
        "-i", "--print-info", dest="print_info", default=False, action="store_true"
    )
    parser.add_argument(
        "-d", "--decrypt", dest="decrypt", default=False, action="store_true"
    )
    parser.add_argument(
        "-r", "--repair", dest="repair", default=False, action="store_true"
    )

    args = parser.parse_args()
    main(args.message, args.key, args.print_info, args.decrypt, args.repair)
