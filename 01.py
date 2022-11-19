class value():
    def __init__(self, data):
        self.key = data
        self.Left = None
        self.Right = None
def insert(value,key):
    if not value:
        Mid = value(key)
        return
    q = []
    q.append(value)
    while (len(q)):
        value = q[0]
        q.pop(0)
 
        if (not value.Left):
            value.Left = value(key)
            break
        else:
            q.append(value.Left)
 
        if (not value.Right):
            value.Right = value(key)
            break
        else:
            q.append(value.Right)
def linkedlist(value):
    if (not value):
        return
    linkedlist(value.Left)
    print(value.key,end = " ")
    linkedlist(value.Right)

if __name__ == '__main__':
    Mid = value(50)
    Mid.Left = value(25)
    Mid.Left.Left = value(75)
    Mid.Right = value(30)
    Mid.Right.Left = value(60)
    Mid.Right.Right = value(40)
    linkedlist(Mid)

