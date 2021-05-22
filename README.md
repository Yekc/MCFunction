# MCFunction
Python package for creating minecraft datapacks (Still a work in progress)

What it will most likely look like in the future: (also most likely will change)
```python
from mcfunction.decorators import tick, load
from mcfunction.commands import say
from mcfunction.project import create

@tick
def spamHello():
  say(text="Hello!")
  
create(path="C:\Users\PC_USER\AppData\Roaming\.minecraft\saves\New World\datapacks", namespace="myDatapack", description="My datapack", pack_format="6")
```
