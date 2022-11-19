class value:
    def __init__(self, data):
        self.data = data
        self.Left = None
        self.Right = None
def linkedlist(value):
    if(not value):
        return
    linkedlist(value.Left)
    print(value.data, end=" ")
    linkedlist(value.Right)
def insert(Mid, key):
    if(Mid == None):
        return None
    if(Mid.Left == None and Mid.Right == None):
        if(Mid.data == key):
            return None
        else:
            return Mid
    key_node = None
    value = None
    last = None
    s = []
    s.append(Mid)
    while(len(s)):
        value = s.pop(0)
        if(value.data == key):
            key_node = value
        if(value.Left):
            last = value
            s.append(value.Left)
        if(value.Right):
            last = value
            s.append(value.Right)
    if(key_node != None):
        key_node.data = value.data
        if(last.Right == value):
            last.Right = None
        else:
            last.Left = None
    return Mid
if __name__ == '__main__':
    Mid = value(50)
    Mid.Left = value(25)
    Mid.Left.Left = value(75)
    Mid.Right = value(30)
    Mid.Right.Left = value(60)
    Mid.Right.Right = value(40)
    key = 30
    Mid = insert(Mid, key)
    key = 75
    Mid = insert(Mid, key)
    key = 40
    Mid = insert(Mid, key)
    linkedlist(Mid)