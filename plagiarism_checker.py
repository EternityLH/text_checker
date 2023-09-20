import sys
import jieba
from nltk.corpus import stopwords


def calculate_similarity(original_file, copied_file):
    with open(original_file, 'r', encoding='utf-8') as f1, open(copied_file, 'r', encoding='utf-8') as f2:
        original_text = f1.read()
        copied_text = f2.read()

    # 使用jieba进行中文分词
    original_words = jieba.lcut(original_text)
    copied_words = jieba.lcut(copied_text)

    # 去除停用词
    stop_words = set(stopwords.words('chinese'))  # 使用中文停用词表
    original_words = [word for word in original_words if word not in stop_words]
    copied_words = [word for word in copied_words if word not in stop_words]

    original_set = set(original_words)
    copied_set = set(copied_words)

    common_words = original_set.intersection(copied_set)
    similarity = len(common_words) / len(original_set) * 100

    return round(similarity, 2)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <original_file> <copied_file> <output_file>")
        sys.exit(1)

    original_file = sys.argv[1]
    copied_file = sys.argv[2]
    output_file = sys.argv[3]

    similarity = calculate_similarity(original_file, copied_file)

    with open(output_file, 'w') as f:
        f.write(str(similarity))

    print(f"Similarity: {similarity}%")