from flask import  g, session, flash


from dbTest import connect_db,  get_db


def get_current_user():
    user_result = None

    if 'user' in session:
        user_email = session['user']

        db = get_db()
        db.execute('select user_id, email, password, can_scout, can_analyse, can_edit, admin, final_editor from users where email = %s', (user_email,))
        user_result = db.fetchone()

    return user_result




























#
