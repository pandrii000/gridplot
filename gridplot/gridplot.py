import numpy as np


def plot_grid(images, cols, bwidth=25, fill_value=0):
    images = [img for img in images]
    rows = round(len(images) / cols + 0.49)
    shape = images[0].shape
    bshape = np.array([shape[0] + 2 * bwidth, shape[1] + 2 * bwidth, 3])
    dtype = images[0].dtype
    if len(images) != rows * cols:
        tmp = np.full(shape, fill_value, dtype)
        for _ in range(rows * cols - len(images)):
            images.append(tmp)
    if bwidth > 0:
        images_ = []
        for i in range(len(images)):
            img_ = np.full(bshape, fill_value, dtype)
            img_[bwidth: bwidth + shape[0], bwidth: bwidth + shape[1], :] = images[i]
            images_.append(img_)
        images = images_
    images = np.asarray(images)
    images = images.reshape(rows, cols, *bshape)
    res = np.concatenate(images[0], axis=1)
    for row in range(1, rows):
        res = np.concatenate([res, np.concatenate(images[row], axis=1)], axis=0)
    return res


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    blue = np.ones((100, 100, 3)) * np.array([[[0, 0, 1]]])
    red = np.ones((100, 100, 3)) * np.array([[[1, 0, 0]]])

    grid = [blue] * 3 + [red] * 3
    grid = plot_grid(grid, cols=2, bwidth=25, fill_value=0)

    plt.imshow(grid)
    plt.show()
