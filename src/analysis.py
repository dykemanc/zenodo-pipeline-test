"""Toy analysis step: z-score normalisation of a numeric series."""
import statistics

MAX_ITERATIONS = 25


def load_data():
    return [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]


def preprocess_data(values):
    mu = statistics.mean(values)
    sd = statistics.stdev(values)
    return [(v - mu) / sd for v in values]


def summarize(values):
    return {"n": len(values), "mean": statistics.mean(values)}


if __name__ == "__main__":
    print(summarize(preprocess_data(load_data())))
