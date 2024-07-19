from PIL import Image
from pathlib import Path


# Diretório do script
ROOT_FOLDER = Path(__file__).parent

# Diretório dos arquivos
FILES_FOLDER = ROOT_FOLDER / 'files'

# Caminhos das imagens
IMG_ORIGINAL = FILES_FOLDER / 'Rs.png'
NEW_IMG = FILES_FOLDER / 'icone.ico'

image = Image.open(IMG_ORIGINAL)
image = image.resize((256, 256))

# Converter e salvar a imagem como ícone
image.save(NEW_IMG, format='ICO', sizes=[(256, 256)])