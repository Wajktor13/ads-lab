from egz1btesty import runtests


class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None     # pole do wykorzystania przez studentow

def wideentall( T ):
    if T is None:
        return None

    vertices_on_height = [1]
    T.x = [0, None]

    set_heights(T, vertices_on_height)

    best_height = 0
    for h in range(1, len(vertices_on_height)):
        if vertices_on_height[h] >= vertices_on_height[best_height]:
            best_height = h    

    set_state(T, best_height)
    
    return count_edges_to_remove(T, best_height)


def set_heights(node, vertices_on_height):
    if node.left is not None:
        node.left.x = [node.x[0] + 1, None]
        if len(vertices_on_height) - 1 < node.left.x[0]:
            vertices_on_height.append(1)
        else:
            vertices_on_height[node.left.x[0]] += 1
        
        set_heights(node.left, vertices_on_height)
    
    if node.right is not None:
        node.right.x = [node.x[0] + 1, None]
        if len(vertices_on_height) - 1 < node.right.x[0]:
            vertices_on_height.append(1)
        else:
            vertices_on_height[node.right.x[0]] += 1
        
        set_heights(node.right, vertices_on_height)


def set_state(node, best_height):
    if node is not None:
        if node.x[0] >= best_height:
            return True
        else:
            left, right = set_state(node.left, best_height), set_state(node.right, best_height)
            node.x[1] = left or right

            return node.x[1]

    return False


def count_edges_to_remove(node, best_height):
    to_remove = 0

    if node is not None:
        if node.x[0] == best_height:
            if node.left is not None:
                to_remove += 1
            if node.right is not None:
                to_remove += 1
        elif not node.x[1]:
            to_remove += 1
        else:
            to_remove += count_edges_to_remove(node.left, best_height) +\
                         count_edges_to_remove(node.right, best_height)

    return to_remove

    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )
