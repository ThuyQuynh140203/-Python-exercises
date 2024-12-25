class Movie:
    def __init__(self, title, director, actor, year, rating):
        self.title = title
        self.director = director
        self.actor = actor
        self.year = year
        self.rating = rating

    def read(self):
        num_directions = len(self.director.split(", "))
        num_actors = len(self.actor.split(", "))
        return num_directions, num_actors

    def __str__(self):
        return f"{self.title} được sản xuất vào năm {self.year} có điểm đánh giá là {self.rating}"


if __name__ == '__main__':
    # Tạo đối tượng cho movie
    movie = Movie(title="Những thiên thần của Charlie", director="Elizabeth Banks",
                  actor="Christen Stewart, Naomi Scott, Ella Balinska", year=2021, rating=4.5)
    num_directors, num_actors = movie.read()
    print(f'So luong dao dien {num_directors} và so luong dien vien {num_actors}')
    print(movie)