text = input("请输入一段英文文字：")
# 词频统计器 - 输入英文文字，统计每个单词出现次数
words = text.lower().split()
word_count = {}
for word in words:
    if word.isalpha():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")