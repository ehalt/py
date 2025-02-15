def http_error(status):
    match status:
        case 400:
            return "bad request!"
        case 404:
            return "Not found"
        case 418:
            return "I'm  teapot"
        case _:
            return "something is wrong with the internet"
        

print(http_error(430))