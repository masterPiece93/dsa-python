# Graphs

A network of nodes is called `Graph` .
    - A node is a memory block containing data .
    - We Join and arrange this network in a fashion that suits & solves our problem .

These graphs are classified based on following criterias :

- direction of link between these nodes
- weight of link between these nodes
- comprehensive


Based on `direction of link between these nodes` :

- directed graph ( _unidirectional_ )
- un-directd graph ( _bidirectional_ )

Based on `weight of link between these nodes` :

- weighted graph
- un-weighted graph

Comprehensive :

- directed & weighted graph
- directed & un-weighted graph
- un-directd & weighted graph
- un-directd & un-weighted graph

> weight is just an integer number , that act as a prefrencing/prioritising factor in quantitative calculations

- meaning of weight differ based on whatever you associate it with in your algorithm
    - it can be `cost`
    - it can be `penalty`
    - it can be `reward`
    - it can be `priority`
    - etc... etc...




## BFS

breadth first search

> Slogan of Bfs : reach to the immmedeate neighbors first .

```
jo pehle mil jaye , usko pehle use kro
```

Run :

```sh
cd graphs # skip if already in that dir
```

```sh
python3 -m traversal.bfs
```

## DFS

depth first search

> Slogan of Dfs : reach to the immmedeate neighbors first .

```
jo milta jaye , usko use kro aur ussi ke aage find kro
```

Run :

```sh
cd graphs # skip if already in that dir
```

```sh
python3 -m traversal.dfs
```


## Study Links

- [Graphs Traversals](https://www.puppygraph.com/blog/graph-traversal)