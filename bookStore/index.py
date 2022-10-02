from requests_html import HTMLSession
import time
import csv

session = HTMLSession()
product_id = 1
with open('Books_toScrap.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product_id', 'Book_Name', 'Book_Price', 'Book_Stock'])
    for x in range(1, 50):
        print(f'Page Number {x}.....')
        page = session.get(
            f"https://books.toscrape.com/catalogue/page-{x}.html")

        print(page)

        Books = page.html.xpath(
            '/html/body/div/div/div/div/section/div[2]', first=True)

        for book in Books.absolute_links:
            book_page = session.get(book)
            try:
                book_name = book_page.html.find('h1', first=True).text
            except:
                print('Data Missed')
            try:
                book_price = book_page.html.find(
                    'p.price_color', first=True).text
            except:
                print('Data Missed')
            try:
                book_available = book_page.html.find(
                    'td', containing='stock', first=True).text
            except:
                print('Data Missed')
            # print(product_id, book_name, book_price, book_available)
            writer.writerow(
                [product_id, book_name, book_price, book_available])
            print(product_id)
            product_id += 1
            print('-----------------------------------------------------------')
