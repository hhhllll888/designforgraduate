from keras.models import load_model
import tensorflow as tf
import numpy as np
from pathlib import Path
# 加载模型 这个模块耗时较长，需要多线程

# 获取当前运行脚本的文件路径
Model_folder=r"model\20230704.h5" #模型文件夹包括模型文件
########以下代码不需要动########

current_script_path = Path(__file__).resolve()
model_path = str(current_script_path.parent)+"\\"+Model_folder
try:
    model = load_model(model_path)
    
except OSError as e:
    raise FileNotFoundError("模型文件获取错误") from e
class_names = {0:'飞机', 1:'汽车', 2:'鸟', 3:'猫', 4:'鹿',
               5:'狗', 6:'青蛙', 7:'马', 8:'船', 9:'卡车'}
def predict(image_path)->dict:
    """预测图片
    Args:
        image_path (str): 图片文件路径
    """
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        # decoded_image = tf.image.decode_jpeg(image_data)
        decoded_image=tf.image.decode_jpeg(image_data,channels=3)
        image = tf.cast(decoded_image, tf.float32) / 255.0
        image = tf.image.resize(image, [32, 32])
        image = np.array(image)
        image=image.reshape((1,32,32,3))
        result = model.predict(image)
        result = result * 100 
        result = ["{:.2f}%".format(value) for value in result.flatten()]
        max_result = np.argmax(result)
        return {"code":0,"result":class_names[max_result],"details":result,"class_name":class_names}
    except Exception as err:
        return {"code":-1,"msg":err}
    
if __name__=="__main__":# 测试代码，不影响
    print(predict(r"E:\learning\exam\cifar10_images\0\29.jpg"))
    