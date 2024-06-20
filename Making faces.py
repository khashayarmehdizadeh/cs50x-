def main():
    sentences =input ("enter a something:")
    convert(sentences)


def convert(sentences):
    new_sentences = sentences.replace(":)", "🙂").replace(":(", "🙁")
    print(new_sentences)


main()
