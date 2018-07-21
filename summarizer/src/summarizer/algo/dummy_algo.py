from abstract_summarizer_algo import AbstractSummarizerAlgo


class DummySummarizerAlgo(AbstractSummarizerAlgo):
    """
    DummySummarizerAlgo is a dummy text summarization algorithm implementation for testing purposes.
    """

    def run(self, text, percentage):
        return "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."
