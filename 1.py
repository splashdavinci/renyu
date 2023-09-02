def count_and_replace(file):
    file = "file_to_read.txt"
    with open(file, 'r') as f:
        text = f.read()

    # 计算单词"terrible"出现的总次数
    word_count = text.count("terrible")

    # 替换每个偶数次出现的"terrible"为"pathetic"，每个奇数次出现的"terrible"为"marvellous"
    replaced_text = ''
    occurrence_count = 1
    for word in text.split():
        if word == "terrible":
            if occurrence_count % 2 == 0:
                replaced_text += "pathetic "
            else:
                replaced_text += "marvellous "
            occurrence_count += 1
        else:
            replaced_text += word + " "

    # 将替换后的文本写入新文件result.txt
    with open("result.txt", 'w') as f:
        f.write(replaced_text)

    return word_count

# 调用函数并打印结果
file = "file_to_read.txt"
word_count = count_and_replace(file)
print("The total number of times the word 'terrible' appears:", word_count)
