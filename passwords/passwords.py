'''
    conversions.py
    Jeff Ondich, 6 May 2022

    Shows how to compute a SHA-256 hash and manipulate the
    relevant Python types.

    Note that when you want to do a new hash, you need to
    call hashlib.sha256() again to get a fresh sha256 object.
'''
# Lane Maitland
# with code adapted from Jeff Ondich

import hashlib
import binascii

# # --- part 1 ---
words = [line.strip().lower() for line in open('words.txt')]
words_hash = []
for word in words:
    encoded = word.encode('utf-8')
    hasher = hashlib.sha256(encoded)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    words_hash.append(digest_as_hex_string)

passwords1 = [line.strip().lower() for line in open('passwords1.txt')]
cracked1 = {}
for info in passwords1:
    info_split = info.split(":")
    username = info_split[0]
    password = info_split[1]
    index = words_hash.index(password)
    decoded = words[index]
    cracked1[username] = decoded

cracked1_file = open("cracked1.txt", "a")
for username, decoded in cracked1.items():
    cracked1_file.write(f"{username} : {decoded}\n")
cracked1_file.close()

num_hash = len(words_hash)
num_cracked1 = len(cracked1)

# # --- part 2 ---
# # this did not work ("zsh: killed ")
# words = [line.strip().lower() for line in open('words.txt')]
# words_concat = []
# words_hash = []
# for word1 in words:
#     for word2 in words:
#         concat = word1 + word2
#         words_concat.append(concat)
#         encoded = concat.encode('utf-8')
#         hasher = hashlib.sha256(encoded)
#         digest = hasher.digest()
#         digest_as_hex = binascii.hexlify(digest)
#         digest_as_hex_string = digest_as_hex.decode('utf-8')
#         words_hash.append(digest_as_hex_string)

# passwords2 = [line.strip().lower() for line in open('passwords2.txt')]
# cracked2 = {}
# for info in passwords2:
#     info_split = info.split(":")
#     username = info_split[0]
#     password = info_split[1]
#     index = words_hash.index(password)
#     decoded = words_concat[index]
#     cracked2[username] = decoded

# cracked2_file = open("cracked2.txt", "a")
# for username, decoded in cracked2.items():
#     cracked2_file.write(f"{username} : {decoded}\n")
# cracked2_file.close()

# num_hash = len(words_hash)
# num_cracked2 = len(cracked2)

# # --- part 2 ---
# # not trying to crack all passwords
# words = [line.strip().lower() for line in open('words.txt')]
# words_concat = []
# words_hash = []
# num_hash = 0
# while num_hash < 10: # I tried changing this many times, but even 10 hashes took too long
#     for word1 in words:
#         for word2 in words:
#             concat = word1 + word2
#             words_concat.append(concat)
#             encoded = concat.encode('utf-8')
#             hasher = hashlib.sha256(encoded)
#             digest = hasher.digest()
#             digest_as_hex = binascii.hexlify(digest)
#             digest_as_hex_string = digest_as_hex.decode('utf-8')
#             words_hash.append(digest_as_hex_string)
#             num_hash += 1
        
# passwords2 = [line.strip().lower() for line in open('passwords2.txt')]
# cracked2 = {}
# for info in passwords2:
#     info_split = info.split(":")
#     username = info_split[0]
#     password = info_split[1]
#     if password in words_hash:
#         index = words_hash.index(password)
#         decoded = words_concat[index]
#         cracked2[username] = decoded

# cracked2_file = open("cracked2.txt", "a")
# for username, decoded in cracked2.items():
#     cracked2_file.write(f"{username} : {decoded}\n")
# cracked2_file.close()

# num_cracked2 = len(cracked2)

# # --- part 3 ---
# words = [line.strip().lower() for line in open('words.txt')]
# passwords3 = [line.strip().lower() for line in open('passwords3.txt')]
# cracked3 = {}
# for info in passwords3:
#     info_split = info.split(":")
#     username = info_split[0]
#     salt_concat = info_split[1]
#     salt_concat_split = salt_concat.split("$")
#     salt = salt_concat_split[1]
#     concat = salt_concat_split[2]
#     num_hash = 0
#     for word in words:
#         salt_word = salt + word
#         encoded = salt_word.encode('utf-8')
#         hasher = hashlib.sha256(encoded)
#         digest = hasher.digest()
#         digest_as_hex = binascii.hexlify(digest)
#         digest_as_hex_string = digest_as_hex.decode('utf-8')
#         num_hash += 1
#         if digest_as_hex_string == concat:
#             cracked3[username] = word

# cracked3_file = open("cracked3.txt", "a")
# for username, decoded in cracked3.items():
#     cracked3_file.write(f"{username} : {decoded}\n")
# cracked3_file.close()

# num_cracked3 = len(cracked3)