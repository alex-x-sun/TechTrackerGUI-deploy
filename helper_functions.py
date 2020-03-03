from datetime import datetime, timedelta
import time
from random import randrange
from app import *

def random_date(year):
    """
    This function will return a random datetime in a year
    """
    start = datetime.strptime(str(year) + '/01/01', '%Y/%m/%d')
    end = datetime.strptime(str(year+1) + '/01/01', '%Y/%m/%d')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)



def redirect_marker(table, row_id, mode = None):
    if table == 'tech_story_final':
        return (url_for('edit_final_log', story_id = row_id))
    elif table in ['tech_main_final', 'tech_wiki_final']:
        return (url_for('edit_final_scout', id = row_id))
    elif table == 'tech_main_log':
        if mode == 'edit':
            return (url_for('view_scout', log_id = row_id, mode = 'edit'))
        else:
            return (url_for('view_scout', log_id = row_id))
    elif table == 'tech_story_log':
        if mode == 'edit':
            return (url_for('view_log', log_s_id = row_id, mode = 'edit'))
        else:
            return (url_for('view_log', log_s_id = row_id))

def text_pretty(varchar):
    return varchar.replace('_', ' ').strip().title()

def textlist_pretty(varchar):
    return '; '.join(list(map(text_pretty, varchar.split(';'))))

def ToMachineReadable(char):
    """
    Change a string into standard format
    """
    try:
        return char.lower().strip().replace(' ', '_')
    except:
        return None







#
