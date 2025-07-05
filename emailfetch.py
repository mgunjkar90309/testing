p = ['test@gmail.com','sample@yahoo.com','python@test.com']

def email_fetch():
    e = []
    for i in p:
        if i.endswith('@gmail.com'):
            e.append(i)
    return e