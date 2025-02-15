text = "the quick brown fox jumps over the lazy dog the"

w_counts = {}
for word in text.split():
    if word in w_counts:
        w_counts[word] += 1
    else:
        w_counts[word] = 1

print(w_counts) 