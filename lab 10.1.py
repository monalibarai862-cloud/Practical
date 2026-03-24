import pandas as pd

data = {
    "title": ["Book1", "Book2", "Book3", "Book4", "Book5"],
    "author": ["AuthorA", "AuthorB", "AuthorA", "AuthorC", "AuthorB"],
    "edition": [1, 2, 1, 3, 2],
    "year": [2015, 2018, 2020, 2012, 2019],
    "publisher": ["ABC", "XYZ", "ABC", "PQR", "XYZ"],
    "price": [250, 300, 450, 200, 500]
}

df = pd.DataFrame(data)

print("\nComplete Book Details:")
print(df)

author_name = input("\nEnter author name: ")
print(df[df['author'] == author_name])

publisher_name = input("\nEnter publisher name: ")
print(df[df['publisher'] == publisher_name])

print("\nCheapest Book:")
print(df[df['price'] == df['price'].min()])

print("\nCostliest Book:")
print(df[df['price'] == df['price'].max()])

print("\nBooks Sorted by Year:")
print(df.sort_values(by='year'))