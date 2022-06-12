from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('İsim')
    user_email = Col('Mail Adresi')
    user_password = Col('Parola', show=False)
    edit = LinkCol('Duzenle', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Sil', 'delete_user', url_kwargs=dict(id='user_id'))
