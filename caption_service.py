from core.model import ModelWrapper
import os

def caption(img):
    model_wrapper = ModelWrapper()
    preds = model_wrapper.predict(img)
    return preds


def predict(file_name, doc=False):

    preds = caption(file_name)

    result = {}
    full_res = [{'caption': p[1], 'probability': p[2]}
                   for p in [x for x in preds]]
    text_res = [{'caption': p[1]}
                   for p in [x for x in preds]]
    if doc:
        response = {
            "full_res": full_res,
            "text_res": text_res
        }
    else:
        response = {
            "file_name": file_name,
            "full_res": full_res,
            "text_res": text_res,
            "is_doc_type": False
        }
        
    os.remove(file_name)

    return response
