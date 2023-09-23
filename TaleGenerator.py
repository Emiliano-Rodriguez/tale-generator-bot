import json
import random

######### Twitter Tale Generator ##########
#      twitter developer application  
#      for twitter bot purposes 
#                              created: 2023_09_23
#########  


# Init tale selector class from stories.json 
class TalesSelector:
    def __init__(self):
        self.json_file_path = "./books/stories.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.json_file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"JSON file '{self.json_file_path}' not found.")
            self.data = {}

    # Selects random tale from stories.json 
    def select_random_tale(self):
        book_title = list(self.data.keys())[0]
        tales = self.data[book_title]['Tales']
        random_tale = random.choice(tales)
        tale_name = list(random_tale.keys())[0]
        summary = random_tale[tale_name]['Summary']
        image = random_tale[tale_name].get('Image', '')  # Get the image filename (if available)
        return f"Book: {book_title} \nTale: {tale_name}\n{summary}", image

# Example usage:
if __name__ == "__main__":
    tales_selector = TalesSelector()
    summary_txt, image_filename = tales_selector.select_random_tale()
    print(summary_txt)
    print("Image Filename:", image_filename)