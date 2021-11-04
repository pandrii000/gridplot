import numpy as np
import matplotlib.pyplot as plt


def figure_to_image(figure):
    figure.canvas.draw()
    image = np.frombuffer(figure.canvas.tostring_rgb(), dtype=np.uint8)
    image = image.reshape(figure.canvas.get_width_height()[::-1] + (3,))
    return image


def plot_lgrid(images, labels, cols, axis=True):
    rows = round(len(images) / cols + 0.49)

    fig, axs = plt.subplots(rows, cols)
    axs = axs.ravel()

    for ax, image, label in zip(axs, images, labels):
        ax.imshow(image)
        ax.set_title(label)

        if not axis:
            ax.axis('off')

    plt.tight_layout()

    grid = figure_to_image(fig)

    plt.clf()
    plt.cla()

    return grid


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    blue = np.ones((100, 100, 3)) * np.array([[[0, 0, 1]]])
    red = np.ones((100, 100, 3)) * np.array([[[1, 0, 0]]])

    images = [blue] * 3 + [red] * 3
    labels = [('blue' if i < 3 else 'red') for i in range(6)]

    grid = plot_lgrid(images, labels, 4, axis=False)

    plt.imshow(grid)
    plt.show()
