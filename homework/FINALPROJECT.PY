#recipe project
#3 recipes
#cooking 


def main():
    
print('Recipe book')
    print('Use the numbers to navigate the menu.')
    settings = {'1': view_recipe,
               
               
               '2': add_recipe
               }
    for key in sorted(settings, key=int)  :
        print('{}) {}'.format(key, get_title(settings[key].__name__)))
    while True:
        
        
        choice = input(' > ')
        
        if choice in options:
          options[choice]()
         
            break

def view_recipe():
    path = get_file('Type in the number of the recipe you '
                    'would like to view and press enter.')
    print("\n")
   
    print('Reciple for', get_name(path))
    with open(path) as file:
        lines = filter(None, map(str.strip, file))
        for step in enumerate(takewhile('heading1'.__ne__, lines), 1):
            print('{}. {}'.format(*step))
        columns = OrderedDict((name.strip(), [])
                              for name in next(lines).split(','))
        max_split = len(columns) - 1
       
     for key, value in zip_longest(columns, fields, fillvalue=''):
      columns[key].append(value)
    ingredients = columns['ingredients']
    print("\n")
    weights = columns['weight']
    prin("\n")
    measurements = columns['measurement']
    print("\n")
    assert len(ingredients) == len(weights) == len(measurements)
    print('Ingredients')
    for specification in zip(ingredients, weights, measurements):
        print(*specification)

def add_recipe():
    raise NotImplementedError()


 for index, path in enumerate(files, 1):
 print('{}) {}'.format(index, get_name(path)))
    
    
    
print(' Enter the number of the recipes.')
return files[int(input('> ')) - 1]


def get_name(path):
return get_title(splitext(basename(path))[0])


def get_title(name):
return name.replace('_', ' ').title()































class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(First, Second):
    def __init__(self):
        print "third"
