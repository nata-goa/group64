
def update_and_popitem(d):
    d.update({"age": 14})
    removed_item = d.popitem()
    print("Updated dictionary:", d)
    print("Removed item:", removed_item)

student = {"name": "ნატალი", "grade": "10"}
update_and_popitem(student)