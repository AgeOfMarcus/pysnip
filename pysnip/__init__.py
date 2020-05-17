from importlib._bootstrap import spec_from_loader
import requests, sys

class PysnipImporter:
    """ 
    `from pysnip import hello_world` will search through pysnip.marcusweinberger.repl.co's db and attempt to download and import hello_world
    """
    API_URL = "https://pysnip.marcusweinberger.repl.co"

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        spec = spec_from_loader(fullname, cls, origin='hell')
        spec.__license__ = "MIT"
        spec._url = cls._fetch_url(spec.name)
        spec._code, spec.__author__ = cls._fetch_code(spec._url)
        return spec

    @classmethod
    def create_module(cls, spec):
        """Create a built-in module"""
        return spec

    @classmethod
    def exec_module(cls, module=None):
        """Exec a built-in module"""
        try:
            exec(module._code, module.__dict__)
        except:
            print(module._url)
            print(module._code)
            raise

    @classmethod
    def get_code(cls, fullname):
        return compile(cls._fetch_code((u:=cls._fetch_url(fullname))), u, 'exec')

    @classmethod
    def get_source(cls, fullname):
        return cls.get_code(fullname)

    @classmethod
    def is_package(cls, fullname):
        return False

    ############################

    @classmethod
    def _fetch_url(cls, query):
        query = query.replace("pysnip.", "")
        res = requests.get(cls.API_URL + "/search", params={
            'q':query,
        }).json()
        if (url:=res.get("url",False)):
            return url
        else:
            raise ImportError("Snip not found")

    @classmethod
    def _fetch_code(cls, url):
        q = requests.get(url)
        res = q.json()
        if not res == {}:
            return res['code'], res['author']
        else:
            raise ImportError("Error getting snip from url: " + url)


sys.meta_path.append(PysnipImporter())