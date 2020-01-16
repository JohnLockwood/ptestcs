# ptestcs

The name ptestcs comes from "Package Test - Codesolid".  Yes, that could 
be clearer. :)
            
## Building 

'''
make init
make publish
'''

## Run the tests

'''
make test
'''


## Installing from Github

```
pipenv install -e git+https://github.com/JohnLockwood/ptestcs.git@v0.2#egg=ptestcs
pipenv shell
python3 # Important.  For some reason "python" doesn't work, even if they resolve to the same binary!
import ptestcs
print(ptestcs.readme())
```

The above should print __this__ readme from github, 
 c.f. https://github.com/JohnLockwood/ptestcs/blob/master/README.md
