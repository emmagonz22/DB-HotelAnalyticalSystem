import tornado

class MainHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user") # use to verify if the user is log in

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Username: <input type="text" name="username">'
                   'Password: <input type="password" name="password">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("username"))
        self.redirect("/")

class RegisterHandler(MainHandler):
    def get(self):
        if self.current_user: # if the user is connected block the user from accesing this endpoint
            self.redirect("/")
            return
        self.write("This is a secret page")


class IndexHandler(MainHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.write("This is a secret page")

def create_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/login", LoginHandler),
        (r"/register", RegisterHandler),
    ], cookie_secret="YOUR_SECRET_HERE")

if __name__ == "__main__": # Running 
    app = create_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
