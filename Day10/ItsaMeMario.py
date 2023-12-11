from __future__ import annotations
import numpy as np
import dataclasses
import matplotlib.pyplot as plt

CONNECTING_TILES = {
    'NORTH': ['|', '7', 'F'],
    'EAST': ['-', '7', 'J'],
    'SOUTH': ['|', 'J', 'L'],
    'WEST': ['-', 'F', 'L']
}

NEXT_DIRECTION = {
    'NORTH' : {
        '|' : 'NORTH',
        '7' : 'WEST',
        'F' : 'EAST'
    },
    'EAST' : {
        '-' : 'EAST',
        '7' : 'SOUTH',
        'J' : 'NORTH'
    },    
    'SOUTH' : {
        '|' : 'SOUTH',
        'J' : 'WEST',
        'L' : 'EAST'
    },
    'WEST' : {
        '-' : 'WEST',
        'F' : 'SOUTH',
        'L' : 'NORTH'
    }
}

@dataclasses.dataclass
class Node:
    x: int
    y: int
    prev: Node = None
    next: Node = None
    next_direction: str = None
    distance: int = 0
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.distance}) -> {self.next_direction}'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.distance == other.distance

class Direction:
    NORTH = ('NORTH', -1, 0)
    SOUTH = ('SOUTH', 1, 0)
    EAST = ('EAST', 0, 1)
    WEST = ('WEST', 0, -1)
    
    def get_direction(dir: str) -> tuple[str, int, int]:
        match dir:
            case 'NORTH':
                return Direction.NORTH
            case 'SOUTH':
                return Direction.SOUTH
            case 'EAST':
                return Direction.EAST
            case 'WEST':
                return Direction.WEST 
    
with open('input.txt') as f:
    lines = f.readlines()

input = [[c for c in line.strip()] for line in lines]  
input  = np.array(input)  
x, y = np.where(input == 'S')

start = Node(x[0], y[0])
start_cnt = 0
for dir, x_offset, y_offset in (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST):
    
    if dir == 'NORTH' and start.y == 0 or \
        dir == 'EAST' and start.x == input.shape[1] - 1 or \
        dir == 'SOUTH' and start.y == input.shape[0] - 1 or \
        dir == 'WEST' and start.x == 0:
            continue
    
    tile = input[start.x + x_offset, start.y + y_offset]
    if tile in CONNECTING_TILES[dir]:
        if start_cnt == 0:
            start.next = Node(
                start.x + x_offset, 
                start.y + y_offset,
                prev=start,
                next_direction=NEXT_DIRECTION[dir][tile],
                distance=1
            )
            start_cnt += 1
        else:
            start.prev = Node(
                start.x + x_offset, 
                start.y + y_offset,
                prev=start,
                next_direction=NEXT_DIRECTION[dir][tile],
                distance=1                
            )
            break

node1 = start.next
node2 = start.prev

while node1 != node2:
    dir, x_offset, y_offset = Direction.get_direction(node1.next_direction)
    next_char = input[node1.x + x_offset, node1.y + y_offset]
    if next_char in CONNECTING_TILES[dir]:
        node1.next = Node(
            node1.x + x_offset,
            node1.y + y_offset,
            prev=node1,
            next_direction=NEXT_DIRECTION[dir][next_char],
            distance=node1.distance + 1
        )
        node1 = node1.next
    
    else:
        break
    
    dir, x_offset, y_offset = Direction.get_direction(node2.next_direction)
    next_char = input[node2.x + x_offset, node2.y + y_offset]
    if next_char in CONNECTING_TILES[dir]:
        node2.next = Node(
            node2.x + x_offset,
            node2.y + y_offset,
            prev=node2,
            next_direction=NEXT_DIRECTION[dir][next_char],
            distance=node2.distance + 1
        )
        node2 = node2.next
    
    else:
        break    

print(node1.distance)