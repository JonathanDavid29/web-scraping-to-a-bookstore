# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class UltimatescraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names = adapter.field_names() # con adapter obtenemos todos los field_names
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip() # para cada value que es != de description quitamos los espacios en blanco
        
        ## Category & Product Type -> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower() 

        ## price -> convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)
        
        ## availability -> extract number of books in stock
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        ## Reviews -> convert string to number
        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)

        ## Stars -> convert text to number
        stars_string = adapter.get('stars')
        split_stars_array = stars_string.split(' ')
        star_text_value = split_stars_array[1].lower()
        if star_text_value == 'zero':
            adapter['stars'] = 0
        elif star_text_value == 'one':
            adapter['stars'] = 1
        elif star_text_value == 'two':
            adapter['stars'] = 2
        elif star_text_value == 'three':
            adapter['stars'] = 3
        elif star_text_value == 'four':
            adapter['stars'] = 4
        elif star_text_value == 'five':
            adapter['stars'] = 5

        return item
        
