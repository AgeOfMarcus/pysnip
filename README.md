# pysnip
Python snippets, easily accessable.

# upload a file

    python -m pysnip main.py --name my_package --author me

# upload code

    from pysnip import client

    client.publish("my_package", "password", "test = 'here'\nprint('hello world')", "me")

# import

    from pysnip import hello_world # finds closest match from server

    hello_world.hello()