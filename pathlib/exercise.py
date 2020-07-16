import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import json
from pathlib import Path


BASE_URL = 'http://books.toscrape.com'
books_dir = Path() / 'books'
image_dir = books_dir / 'images'
image_dir.mkdir(parents=True, exist_ok=True)
ratings = ['', 'One', 'Two', 'Three', 'Four', 'Five']
books = []


def setup():
    for page in tqdm(range(1, 11)):
        response = requests.get(f'{BASE_URL}/catalogue/page-{page}.html')
        soup = BeautifulSoup(response.content, 'html.parser')
        Path.cwd().joinpath('file.txt').write_text('Where did I come from?')
        books.extend(soup.select('article.product_pod'))

    data = [
        {
            'page': book.select_one('a')['href'],
            'name': book.select_one('h3 a')['title'],
            'img': book.select_one('img')['src'],
            'rating': ratings.index(book.select_one('p.star-rating')['class'][1]),
            'price': float(book.select_one('p.price_color').text[1:]),
        }
        for book in books
    ]

    with open(books_dir / 'books.json', 'w') as f:
        json.dump(data, f)

    for pth in tqdm([book['img'][2:] for book in data]):
        with open(image_dir / Path(pth).name, 'wb') as f:
            for chunk in requests.get(f'{BASE_URL}{pth}'):
                f.write(chunk)

    
def cleanup():
    def rmdir(top: Path):
        for file in top.iterdir():
            if file.is_file():
                file.unlink()
            elif file.is_dir():
                rmdir(file)
        top.rmdir()
            
    for pth in [
        Path() / 'books',
        Path() / '../new',
    ]:
        if pth.exists():
            rmdir(pth)
            
    for file in [
        (Path() / '../example.txt'),
        (Path() / 'file.txt'),
    ]:
        if file.exists():
            file.unlink()


if __name__ == '__main__':
    cleanup()
