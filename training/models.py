from django import forms


def p_holder(tag):
    return forms.TextInput(attrs={'placeholder': tag})


DB = {'Boot': []}


class FormData(forms.Form):
    firstname = forms.CharField(max_length=32, widget=p_holder('Firstname'))
    lastname = forms.CharField(max_length=32, widget=p_holder('Lastname'))
    email = forms.CharField(max_length=32, widget=p_holder('Email'))
    profession = forms.CharField(max_length=32, widget=p_holder('Profession'))

    def load_data(self, form):
        data = {
            'firstname': form['firstname'],
            'lastname': form['lastname'],
            'profession': form['profession'],
            'email': form['email'],
            'csrfmiddlewaretoken': form['csrfmiddlewaretoken']
        }
        return data

    def create(self, formData):
        if FormData(formData).is_valid():
            DB['Boot'].append(self.load_data(formData))

    def update(self, form, index):
        DB['Boot'][index].update(self.load_data(form))

    def delete(self, id):
        for item in DB['Boot']:
            if item['csrfmiddlewaretoken'] == id:
                index = DB['Boot'].index(item)
                del DB['Boot'][index]
