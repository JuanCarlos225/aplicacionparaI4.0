import web
render = web.template.render('mvc/views/')
class Contactos:
    def GET(self):
        try:
            return render.contactos()
        except Exception as e:
            print(f"Error 101- contactos {e.args}")
            return "Ups algo salio mal con los contactos"
        
    