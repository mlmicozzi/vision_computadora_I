# imports
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from typing import List
import os
from typing import Optional

def read_images(path: str, flags: int = cv.IMREAD_COLOR) -> List :
    """
    Lee las imágenes de un path determinado

    :param path: path de las imágenes
    :type path: str
    :param flags: modo de lectura de la imagen, por defecto cv.IMREAD_COLOR
    :type flags: int
    :returns: lista de imágenes leídas
    :rtype: list
    """
    images = []

    for file in os.listdir(path):
        if file.endswith('.jpg') or file.endswith('.png'):
            full_path = os.path.join(path, file)
            image = cv.imread(full_path, flags)
            images.append(image)

    return images


def read_image(path: str, filename: str, flags: int = cv.IMREAD_COLOR) -> Optional:
    """
    Lee una imagen de un path determinado

    :param path: path donde se encuentra la imagen
    :type path: str
    :param filename: nombre de la imagen a leer
    :type filename: str
    :param flags: modo de lectura de la imagen, por defecto cv.IMREAD_COLOR
    :type flags: int
    :returns: imagen leída o None si no se encuentra
    :rtype: numpy.ndarray or None
    """
    
    full_path = os.path.join(path, filename)

    if os.path.isfile(full_path) and (filename.endswith('.jpg') or filename.endswith('.png')):
        image = cv.imread(full_path, flags)
        return image

    return None

def show_images(images: List, titles: List[str] = None) -> None:
    """
    Muestra una lista de imágenes en una cuadrícula.
    Conversión de BGR a RGB.

    :param images: Lista de imágenes a mostrar
    :type images: List
    :param titles: Lista de títulos para cada imagen
    :type titles: List[str]
    """
    num_images = len(images)
    cols = num_images
    rows = 1

    _, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))

    if num_images == 1:
        axes = [axes]

    for i, (ax, img) in enumerate(zip(axes, images)):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        ax.imshow(img_rgb)
        if titles and i < len(titles):
            ax.set_title(titles[i], fontsize=14)

    plt.tight_layout()
    plt.show()

def show_images_grey_scale(images: List, titles: List[str] = None) -> None:
    """
    Muestra una lista de imágenes en una cuadrícula.
    Escala de grises

    :param images: Lista de imágenes a mostrar
    :type images: List
    :param titles: Lista de títulos para cada imagen
    :type titles: List[str]
    """
    num_images = len(images)
    cols = num_images
    rows = 1

    _, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    for i, (ax, img) in enumerate(zip(axes, images)):
        ax.imshow(img, cmap='gray')
        if titles and i < len(titles):
            ax.set_title(titles[i], fontsize=14)

    plt.tight_layout()
    plt.show()