from array import array
# documentation here > https://docs.python.org/2/library/array.html

new_array = array('i')

try:

    new_array.fromlist([1,2,223])
    print(new_array)
    print(type(new_array))
except Exception as e:
    print(e)

