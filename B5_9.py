import time

class Timecheck:
    def __init__(self, function_to_run):
        self.num_runs = 100
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(f'Среднее время запуска функции "{fn}" за {self.num_runs} повторений: {avg:.4f} сек.')
        return self.func_to_run(*args, **kwargs)


@Timecheck
def test_time_run(n):
    for i in range(n):
        pass

test_time_run(10000)