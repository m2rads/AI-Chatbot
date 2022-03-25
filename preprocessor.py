"""
Statement custom pre-processors.

"""
from extract_data import extractData
data = extractData('./static/data/menu.json')

def extract_menu_items(statement): 
    """
        detects if a menu item is present in the 
        statement, and if yes passes down the menu item
        
    """
    statement_count = []
    
    if data != 'failed':
        for i in data:
            for j in range(0, len(data[i])):
                if data[i][j]['name'].lower() in statement.lower():
                    statement_count.append(data[i][j]['name'])
                    print(statement.lower())
    if (len(statement_count) < 1 ):
        return statement
    else: 
        return statement_count
        
