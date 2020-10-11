def announce(f):
    print("running announce")

    def wrapper():
        print("running wrapper")
        f()
        print("end of wrapper")

    print("end of announce")
    return wrapper


@announce
def hello():
    print("Hello, World!")


hello()


print("#######")
def login(f):
    print("Running login")

    def verifiy_credentials():
        print("credentials are correct")
        return verifiy_token()

    def verifiy_token():
        print("token are corret")
        return redirect_user()

    def redirect_user():
        print("redirecting the user")
        return try_login(f)

    return verifiy_credentials


@login
def login_successfully():
    print("login successfully")


def try_login(f):
    print("Trying login...")
    f()


login_successfully()
