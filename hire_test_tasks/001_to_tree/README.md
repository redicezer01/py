 #### my version of code:  
 
<code>   
def to_tre(source):    
  1     """return a tree (dictionary)"""    
  2     root = {}    
  3     nested = dict()    
  4    
  5     # generating tree
  6     for k, v in source:
  7         if k is None:
  8             # links between root and nested
  9             if nested.get(v) is None:
 10                 nested[v] = dict()
 11             root[v] = nested[v]
 12             continue
 13
 14         if nested.get(k) is None:
 15             nested[k] = dict()
 16
 17         # links nested
 18         if nested.get(v) is None:
 19             nested[k][v] = dict()
 20             nested[v] = nested[k][v]
 21         else:
 22             nested[k][v] = nested[v]
 23
 24     return root
</code>   
  
#### improved code after feedback:  
  
<code>  
def to_tree(source):
  1     """return a tree (dictionary)"""
  2     root = {}
  3
  4     # generating tree
  5     for k, v in source:
  6
  7         if k not in root:
  8             root[k] = {}
  9
 10         if v not in root:
 11             root[k][v] = {}
 12             root[v] = root[k][v]
 13         else:
 14             root[k][v] = root[v]
 15
 16     return root[None]
</code>  
  
#### diffs  

<code>  
  33d32
  1 <     nested = dict()
  2 37,42d35
  3 <         if k is None:
  4 <             # links between root and nested
  5 <             if nested.get(v) is None:
  6 <                 nested[v] = dict()
  7 <             root[v] = nested[v]
  8 <             continue
  9 44,45c37,38
 10 <         if nested.get(k) is None:
 11 <             nested[k] = dict()
 12 ---
 13 >         if k not in root:
 14 >             root[k] = {}
 15 47,50c40,42
 16 <         # links nested
 17 <         if nested.get(v) is None:
 18 <             nested[k][v] = dict()
 19 <             nested[v] = nested[k][v]
 20 ---
 21 >         if v not in root:
 22 >             root[k][v] = {}
 23 >             root[v] = root[k][v]
 24 52c44
 25 <             nested[k][v] = nested[v]
 26 ---
 27 >             root[k][v] = root[v]
 28 54c46
 29 <     return root
 30 ---
 31 >     return root[None]
</code>  
  
  
#### Resume:  
- Using "in" operator instead .get() method. It's more readable, fast and make sense
- Using 1 dict "root" instead of 2 (second is "nested")
  
This two changes makes code much more shorter
