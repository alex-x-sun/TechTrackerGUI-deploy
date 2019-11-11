import pandas as pd
# import sqlite3
import os
from sqlalchemy import create_engine



milestones_0 = ['none',\
 'inception',\
 'conceptual_design',\
 'prototype',\
 'academic_thesis',\
 'published_paper',\
 'book_mention',\
 'university_lab',\
 'private_r&d',\
 'patent_filed',\
 'patent_issued',\
 'first_commercial_product',\
 'competing_products_enter_the_market',\
 'first_commercial_product_failure',\
 'incorporated_into_other_technologies',\
 'national_standards_body',\
 'regulatory_requirements',\
 'word_in_the_dictionary']

def text_pretty(varchar):
    return varchar.replace('_', ' ').title()

def ToMachineReadable(char):
    """
    Change a string into standard format
    """
    return char.lower().strip().replace(' ', '_')

milestones_tuplist = [('none', 'None Milestone Story')] + [(ms, text_pretty(ms)) for ms in milestones_0[1:]]



# milestones = list(map(text_pretty, milestones_0))
# milestones
milestones = ['None',\
 'Inception',\
 'Conceptual Design',\
 'Prototype',\
 'Academic Thesis',\
 'Published Paper',\
 'Book Mention',\
 'University Lab',\
 'Private R&D',\
 'Patent Filed',\
 'Patent Issued',\
 'First Commercial Product',\
 'Competing Products Enter The Market',\
 'First Commercial Product Failure',\
 'Incorporated Into Other Technologies',\
 'National Standards Body',\
 'Regulatory Requirements',\
 'Word In The Dictionary']





###################### Insert into the database ################################















#
