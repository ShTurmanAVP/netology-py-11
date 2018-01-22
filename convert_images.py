import os
import subprocess
from multiprocessing import Pool

# ради использования pool.map пришлось вынести их из параметров convert_image() в глобальные переменные. Это ок?
source_dir = 'Source'
result_dir = 'Result'


def convert_image(image_name):
    source_file = os.path.join(source_dir, image_name)
    result_file = os.path.join(result_dir, image_name)
    print('start', image_name)
    p = subprocess.Popen('convert {source_file} -resize 200 {result_file}'.format(source_file=source_file, result_file=result_file))
    # print('pid =', p.pid)
    # p.wait()
    print('end  ', image_name)


def jpg_images_generator():
    return (jpg_image
            for jpg_image in os.listdir(source_dir)
            if os.path.isfile(os.path.join(source_dir, jpg_image)) and jpg_image.endswith('.jpg'))

if __name__ == '__main__':

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    images = jpg_images_generator()

    pool = Pool(processes=4)
    pool.map(convert_image, images)
    pool.close()
    pool.join()
