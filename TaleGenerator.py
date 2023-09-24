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
        self.json_file_path = "/home/argulus/bots/tale_generator_bot/books/stories.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.json_file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"JSON file '{self.json_file_path}' not found.")
            self.data = {}

    def save_data(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def select_random_tale(self):
        book_title, book_data = random.choice(list(self.data.items()))
        max_counter = book_data.get('MaxCount')
        tales = book_data.get('Tales', [])
        valid_tales = [tale for tale in tales if tale.get(list(tale.keys())[0], {}).get('Counter', 0) < max_counter]

        if not valid_tales:
          book_data['MaxCount'] += 1
          self.save_data()              
          return "None" , "None"
        
        random_tale_info = random.choice(valid_tales)
        tale_name, tale_details = list(random_tale_info.items())[0]
        
        tale_details['Counter'] += 1
        
        # Save the updated data (including the incremented counter) to the JSON file
        self.save_data()
        
        summary = tale_details.get('Summary')
        image = tale_details.get('Image')
        
        return f"Book: {book_title}\nTale: {tale_name}\n{summary}", image


# Example usage:
if __name__ == "__main__":
    tales_selector = TalesSelector()
    summary_txt, image_filename = tales_selector.select_random_tale()
    while (summary_txt == "None"):
        summary_txt, image_filename = tales_selector.select_random_tale()
    print(summary_txt)
    print("Image Filename:", image_filename)
