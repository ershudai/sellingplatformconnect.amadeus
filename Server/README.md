This is the server side

IDE: Python 3.9.6 
Depend on the package: 
    Name: requests
    Version: 2.25.1
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache 2.0
    Requires: certifi, chardet, idna, urllib3
    Required-by: browsermob-proxy
    
    Name: fastapi
    Version: 0.70.0
    Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
    Home-page: https://github.com/tiangolo/fastapi
    Author: Sebastián Ramírez
    Author-email: tiangolo@gmail.com
    Requires: pydantic, starlette
    
    Name: pydantic
    Version: 1.8.2
    Summary: Data validation and settings management using python 3.6 type hinting
    Home-page: https://github.com/samuelcolvin/pydantic
    Author: Samuel Colvin
    Author-email: s@muelcolvin.com
    License: MIT
    Requires: typing-extensions
    Required-by: fastapi
    
    Name: uvicorn
    Version: 0.15.0
    Summary: The lightning-fast ASGI server.
    Home-page: https://www.uvicorn.org/
    Author: Tom Christie
    Author-email: tom@tomchristie.com
    License: BSD
    Requires: asgiref, click, h11
    
    Name: urllib3
    Version: 1.26.6
    Summary: HTTP library with thread-safe connection pooling, file post, and more.
    Home-page: https://urllib3.readthedocs.io/
    Author: Andrey Petrov
    Author-email: andrey.petrov@shazow.net
    License: MIT
    Required-by: requests, selenium
