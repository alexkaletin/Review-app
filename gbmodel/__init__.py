"""
___ makes this a database package and can import in other code files
"""

"Choose which backend to run"
model_backend = 'datastore'
#model_backend = 'sqlite3'
#model_backend = 'pylist'

if model_backend == 'datastore':
    from .model_datastore import model
elif model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'pylist':
    from .model_pylist import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    """
    Returns database depending on which was selected on the top 
    """
    return appmodel
