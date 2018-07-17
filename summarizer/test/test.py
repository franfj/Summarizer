from summarizer.src.summarizer.algo.summ import Summ
from summarizer.src.summarizer.summarizer import summarizer


def main():
    summarizer.text = "Test"
    summarizer.algo = Summ.DUMMY
    summarizer.percentage = 0.5

    print(summarizer.summarize())


if __name__ == "__main__":
    main()
