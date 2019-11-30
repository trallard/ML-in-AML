import os
import math
import numpy as np
from six.moves.urllib.request import urlretrieve


def download(data_path):
    mnist_file = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    target = os.path.join(data_path, "mnist.npz")
    if not os.path.exists(target):
        print("downloading {} ...".format(mnist_file))
        file, output = urlretrieve(mnist_file, target)
    else:
        print("{} already exists, skipping step".format(str(target)))
    return target


def get_data():
    file = download("data")
    with np.load(file) as f:
        x_train, y_train = f["x_train"], f["y_train"]
        x_test, y_test = f["x_test"], f["y_test"]

    size = x_train.shape[1] * x_train.shape[2]
    return {"X": x_train.reshape(x_train.shape[0], size) / 255.0, "y": y_train}


if __name__ == "__main__":
    s = get_data()
    print(s["X"].shape, s["y"].shape)

