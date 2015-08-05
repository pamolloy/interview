Given a tree, which may not be binary or balanced, and a query, return all nodes that match the query. The query will include a set of paths. For example, `(1,2,5)` would return a node object with value 5 while `(1,4)` would return a node object with value 4. A set of queries would return the union of those nodes. For example, `(1, 2, 5), (1, 4)` would return `4, 5`.

```
      (1)
     / | \
   (2)(3)(4)
  /
(5)
```

Problem from an interview at a large technology company.
