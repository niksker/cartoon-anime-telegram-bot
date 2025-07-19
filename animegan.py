
import onnxruntime
import cv2
import numpy as np

def apply_anime_style(input_path, output_path, model_name="hayao"):
    model_path = f"models/{model_name.lower()}.onnx"
    session = onnxruntime.InferenceSession(model_path, providers=["CPUExecutionProvider"])

    img = cv2.imread(input_path)
    img = cv2.resize(img, (256, 256))
    img_input = img.astype(np.float32) / 127.5 - 1.0
    img_input = np.transpose(img_input, (2, 0, 1))[np.newaxis, :]

    inputs = {session.get_inputs()[0].name: img_input}
    output = session.run(None, inputs)[0][0]
    output = ((np.transpose(output, (1, 2, 0)) + 1) * 127.5).clip(0, 255).astype(np.uint8)
    output = cv2.resize(output, (img.shape[1], img.shape[0]))
    cv2.imwrite(output_path, output)
