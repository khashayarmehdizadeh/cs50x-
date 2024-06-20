def main():
    sentences = input("enter somthing:")
    convert(sentences)


def convert(sentences):
    new_sentences = sentences.replace(":)", "�").replace("(:", "===")
    print(new_sentences)


main()
