import time
from datetime import datetime
from typing import Callable


def timeit(func: Callable) -> Callable:
    def wrapped_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        return elapsed, result

    return wrapped_function


def timeitprint(func: Callable) -> Callable:
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
            time_elapsed = time_elapsed - minutes * 60
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
                "====== Func '{}' finished in {:.10f} secs ======\n".format(
                    func_name, seconds
                )
            )

        return result

    return wrapped_function


def timestamp_seconds() -> str:
    """
    Return a timestamp in 15-char string format: {YYYYMMDD}'T'{HHMMSS}
    """
    now = str(datetime.now().isoformat(sep="T", timespec="seconds"))
    ts: str = ""
    for i in now:
        if i not in (" ", "-", ":"):
            ts += i
    return ts


def timestamp_microseconds() -> str:
    """
    Return a timestamp in 22-char string format: YYYYMMDD-HHMMSS-microseconds
    """
    now = str(datetime.now().isoformat(sep="T", timespec="microseconds"))
    ts: str = ""
    for i in now:
        if i in ("T", "."):
            ts += "-"
        elif i not in (" ", ":", "-"):
            ts += i
    return ts


if __name__ == "__main__":

    @timeitprint
    def tictok():
        a = 1000000
        for i in range(10000000):
            a -= 1
            b = a
        return

    tictok()
    print(timestamp_seconds())
    print(timestamp_microseconds())
