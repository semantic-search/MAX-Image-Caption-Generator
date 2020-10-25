from caption_service import predict, caption_api

resp = caption_api("/app/test_image/aron3.jpg")
print(resp)