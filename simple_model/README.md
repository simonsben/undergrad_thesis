# Three node graph

This is a simplification of the model with three nodes.
The current code runs a *gradient descent* algorithm on the nodes until the exposure is maximized for time 1.
The pseudo code is:

```
while exposure is increasing:
    take gradient of each node
    remove ball from min gradient
    
    take gradient of each node
    add ball to max gradient node
```

The gradient is taken twice because it was found that when it was only taken once (to find the min and max), 
the optimal solution was not found.
This is because the exposure gradient was based on the addition of one ball, not the addition and removal.
