import requests


class TestChuckNorrisJokes:
    def __init__(self, base_url):
        self.base_url = base_url
        self.list_joke_categories = self.get_list_joke_categories()

    # получение всех категорий
    def get_list_joke_categories(self):
        path_to_categories = "/categories"
        full_path_to_categories = self.base_url + path_to_categories
        return requests.get(full_path_to_categories).json()

    # получить шутку из категории
    def get_joke_from_category(self, joke_category):
        full_path_to_joke_from_category = self.base_url + "/random?category=" + joke_category
        result_response = requests.get(full_path_to_joke_from_category).json()
        joke_from_category = result_response["value"]
        return joke_from_category

    # получение по одной шутке из каждой категории
    def get_one_joke_from_each_category(self):
        for joke_category in self.list_joke_categories:
            print(
                f"Шутка из категории \"{joke_category}\":\n"
                f"{self.get_joke_from_category(joke_category)}"
            )


if __name__ == "__main__":
    base_url = "https://api.chucknorris.io/jokes"
    start_test = TestChuckNorrisJokes(base_url)
    start_test.get_one_joke_from_each_category()
