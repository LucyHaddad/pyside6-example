#you can use workers to send jobs to different threads, how i do it:

from PySide6.QtCore import QRunnable, QObject, Slot, Signal
import sys, traceback

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)

class Worker(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
    @Slot()
    def run(self):
        try:
            result = self.function(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

#example: 

# threadpool = QThreadpool()

# def fn(a=1, b=2):
#   new = a+b
#   result = {"new": a+b}
#   return result

# def another_fn(**result):
#   done = result.keys()
#   print(done)

# def finished_fn: print("DONE!")

# def send_job():
#   worker = Worker(fn, *args, **kwargs)
#   worker.signals.result.connnect(another_fn)
#   worker.signals.finished.connect(finished_fn)
#   threadpool.start(worker)
