def handle_uploaded_files(f):
    with open('djangoforms/static/upload'+f.name,'wb+')as destination:
        for chumk in f.chunks():
            destination.write(chumk)
