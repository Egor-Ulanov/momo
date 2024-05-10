from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image

def generate():
    prompt = "HQ human"  # Предположим, вы имели в виду "bunny" (заяц)

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token="YOUR_HUGGINGFACE_TOKEN",  # Замените на ваш токен
        force_download=True
    ).to("cuda")

    with autocast("cuda"):
        # Генерация изображения с помощью нейросети
        result = pipe(prompt)
        image = result.images[0]

        # Проверяем, что объект является изображением PIL и сохраняем его
        if isinstance(image, Image.Image):
            image.save("C:/Users/Lenovo/PycharmProjects/forNeiro/mysite/main/static/img/img2.png")
        else:
            print("Ошибка: полученный объект не является изображением PIL.")
