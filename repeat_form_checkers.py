from dbTest import connect_db,  get_db




def repeat_scout_checker(form, mode = 'scout_only'):
    db = get_db()

    # check repeat form
    if mode == 'scout_only':
        db.execute('''
                                    select log_id
                                    from tech_main_log
                                    where tech_name = %s
                                    ''', (form.tech_name.data,))
        existing_sc = db.fetchone()
    elif mode == 'full_check':
        db.execute('''
                                    select log_id
                                    from tech_main_log
                                    where tech_name = %s
                                    and description = %s
                                    and impact = %s

                                    and asso_names = %s
                                    and emb_techs = %s
                                    and category = %s
                                    and desc_source = %s
                                    ''', (form.tech_name.data, form.description.data, form.impact.data, form.associate_names.data, form.embed_tech.data, form.category.data, form.sources.data))
        existing_sc = db.fetchone()

    elif mode == 'main_table':
        db.execute('''
                                    select log_id
                                    from tech_main
                                    where tech_name = %s
                                    ''', (form.tech_name.data,))
        existing_sc = db.fetchone()

    elif mode == 'final_table':
        db.execute('''
                                    select log_id
                                    from tech_main_final
                                    where tech_name = %s
                                    ''', (form.tech_name.data,))
        existing_sc = db.fetchone()

    return existing_sc

def repeat_story_checker(form):
    db = get_db()
    # check repeat form
    db.execute('''
                                select log_s_id
                                from tech_story_log
                                where story_year = %s
                                and story_date = %s
                                and milestone = %s
                                and story_content = %s
                                and sources = %s
                                ''', (form.story_year.data, form.story_date.data, form.milestone.data, form.story_content.data, form.sources.data))
    existing_ms = db.fetchone()
    return existing_ms


def repeat_checker(form, table_name):
    """
    This function requires that the field naming should be consistent in all tables and forms
    """
    db = get_db()
    form_data = [field.data for field in form]
    sql_where = 'where'
    for field in form[:-1]:
        sql_where += str(field.name) + ' = %s and '

    sql_where += str(form[-1].name) + ' = %s '

    db.execute('select * from' + str(table_name) + sql_where, form_data)
    existing = db.fetchone()

    return existing

def repeat_final_story(form):
    return False
