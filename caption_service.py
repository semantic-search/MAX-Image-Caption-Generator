import requests
import os
import json

def caption_api(file_name):
    with open(file_name, 'rb') as f:
        read_data = f.read()
    files = {
        'image': read_data,
    }
    response = requests.post('http://api:5000/model/predict', files=files)
    print("api res", response)
    data = response.content.decode()
    print("decoded data", data)
    data = json.loads(data)
    print(data)
    return data.predictions

def predict(file_name):
    try:
        preds = caption_api(file_name)
        final_labels = []
        final_scores = []

        [final_labels.append(p[1]) for p in [x for x in preds]]
        [final_scores.append(float(p[2])) for p in [x for x in preds]]

        final_result = {
        "labels": final_labels,
        "scores": final_scores
        }
        os.remove(file_name)
        return final_result

    except Exception as e:
        print(f"{e} Exception in predict")
        error_result = {
        "labels": [],
        "scores": []
        }
        return error_result