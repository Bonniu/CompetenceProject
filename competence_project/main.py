from model.hotspot import Hotspot
from model.trace import Trace
from model.user import User

print("Competence Project - Set up Python project #2: ✓")
print("Class models in Python #14: ✓")

print(Hotspot("hotspot_1", 1.232, 11.22))
print(User())
print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))
