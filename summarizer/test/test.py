from summarizer.src.summarizer.algo.summ import Summ
from summarizer.src.summarizer.summarizer import summarizer


def main():
    summarizer._text("Test")
    summarizer._algo(Summ.DUMMY)
    summarizer._percentage(0.5)

    print(summarizer.run())


if __name__ == "__main__":
    main()
