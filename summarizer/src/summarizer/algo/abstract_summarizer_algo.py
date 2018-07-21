class AbstractSummarizerAlgo(object):
    """
    AbstractSummarizerAlgo defines the run method that every text summarization must implement.
    """

    def run(self, text, percentage):
        raise NotImplementedError('Subclasses must override run()!')
