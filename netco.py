from googlesearch import search
def netconn():
    try:
        for url in search("Google",num_results=1):
            pass
        return 1
    except Exception as e:
        return 0
