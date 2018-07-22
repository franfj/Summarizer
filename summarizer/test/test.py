from summarizer.src.summarizer.algo.summ import Summ
from summarizer.src.summarizer.summarizer import summarizer


def main():
    with open("../../texts/test.txt") as f:
        input_text = f.readlines()[0]

    summarizer.text = input_text
    summarizer.algo = Summ.TEXT_RANK
    summarizer.percentage = 0.25

    # print(summarizer.summarize())
    print(summarizer.schematize())

if __name__ == "__main__":
    main()
