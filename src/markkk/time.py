import time


def timeit(func):
    def wrapped_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time

        if result:
            return elapsed, result
        else:
            return elapsed

    return wrapped_function


def timeitprint(func):
    def wrapped_function(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        time_elapsed = time_end - time_start
        hours, minutes = 0, 0
        if time_elapsed >= 3600:
            hours = int(time_elapsed // 3600)
            time_elapsed = time_elapsed - hours * 3600
        if time_elapsed >= 60:
            minutes = int(time_elapsed // 60)
            time_elapsed = time_elapsed - hours * 60
        seconds = round(time_elapsed, 3)
        func_name = func.__name__
        if hours:
            print(
                "====== Func '{}' finished in {} hrs, {} mins, {} secs ======\n".format(
                    func_name, hours, minutes, int(seconds)
                )
            )
        elif minutes:
            print(
                "====== Func '{}' finished in {} mins, {:.2f} secs ======\n".format(
                    func_name, minutes, seconds
                )
            )
        else:
            print(
                "====== Func <'{}'> finished in {:.6f} secs ======\n".format(
                    func_name, seconds
                )
            )

        if result:
            return result
        else:
            return

    return wrapped_function


if __name__ == "__main__":

    @timeitprint
    def tictok():
        a = 1000000
        for i in range(10000000):
            a -= 1
            b = a
        return

    tictok()
