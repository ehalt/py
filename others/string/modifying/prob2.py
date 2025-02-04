
# my approach 

# text = input()
# splited = text.split()
# sum = 0
# for words in splited:
#     wrd = len(words)
#     sum = sum + wrd
        
# print(sum / len(splited))




# another approach 

sentence = input('enter a sentence: ')
words = sentence.split()
total_len = sum(len(word) for word in words)
num_words = len(words)
avg = total_len/num_words
print('average word length: ', avg)