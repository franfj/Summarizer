class AbstractSummarizerAlgo(object):
    def run(self, text, percentage):
        raise NotImplementedError('subclasses must override run()!')
