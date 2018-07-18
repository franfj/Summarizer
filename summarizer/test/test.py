from summarizer.src.summarizer.algo.summ import Summ
from summarizer.src.summarizer.summarizer import summarizer


def main():
    with open("../../texts/DonQuixote.txt") as f:
        inputText = f.readlines()[0]

    summarizer.text = inputText
    summarizer.algo = Summ.DUMMY
    summarizer.percentage = 0.5

    print(summarizer.summarize())


if __name__ == "__main__":
    main()
