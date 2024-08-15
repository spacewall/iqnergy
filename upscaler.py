from cachetools import cached

import cv2
from cv2 import dnn_superres

@cached({})
def get_scaler(model_path: str) -> dnn_superres.DnnSuperResImpl:
    scaler = dnn_superres.DnnSuperResImpl.create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)

    return scaler

def upscale(input_path: str, output_path: str, model_path: str = 'EDSR_x2.pb') -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path: путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = get_scaler(model_path)
    image = cv2.imread(input_path)
    result = scaler.upsample(image)
    cv2.imwrite(output_path, result)

def example():
    upscale('test.png', 'test_upscaled.png')

if __name__ == '__main__':
    example()