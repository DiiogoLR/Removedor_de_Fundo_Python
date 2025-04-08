from rembg import remove 
from PIL import Image
import io

# Lê a imagem como bytes
with open('imgfundo.jpg', 'rb') as img_file:
    input_bytes = img_file.read()

# Remove o fundo da imagem
output_bytes = remove(input_bytes)

# Converte os bytes de volta para uma imagem
output_image = Image.open(io.BytesIO(output_bytes))

# Salva o resultado
output_image.save('img1.png')
