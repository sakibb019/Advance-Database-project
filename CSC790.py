

from neo4j import GraphDatabase
import time

key = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234"))
session = key.session()


def begin():
    nodes = session.run(""" LOAD CSV WITH HEADERS FROM 'file:///Data.csv' AS line
                            merge(n:Hospital{name:line.Parent}) merge(m:Hospital{name:line.Child}) 
                            merge(n)-[r:RelationType{rType:line.`Relation`}]->(m)""")
# node1 = session.run("match (n) return n")


def leaf_nodes(val):
    tic = time.perf_counter()
    # leaf nodes
    node2 = session.run(
        "match (n) where not ((n)-[]->()) return distinct n  limit $x ", x=val)
    node3 = node2.data()
    x = []
    for record in node3:
        x.append(record['n']['name'])
    toc = time.perf_counter()
    t = (toc - tic)/60
    return x, t


def parent_node(val):
    tic = time.perf_counter()
    x = []
    parent = session.run(
        "match (n)-[]->() return distinct n limit $x", x=val)
    for i in parent.data():
        x.append(i['n']['name'])
    toc = time.perf_counter()
    t = (toc - tic)/60
    return x, t


def longest_path():
    tic = time.perf_counter()
    x = []
    longest = session.run(
        "MATCH p = (longest)-[*]->(shortest) RETURN p ORDER BY LENGTH(p) DESC LIMIT 1 ")
    for i in longest.data():
        x.append(i['p'][0]['name'])
        x.append(i['p'][-1]['name'])
    toc = time.perf_counter()
    t = (toc - tic)/60
    return x, t
# extra function


def smalles_path():
    tic = time.perf_counter()
    x = []
    longest = session.run(
        "MATCH p = (longest)-[*]->(shortest) RETURN p ORDER BY LENGTH(p) LIMIT 1 ")
    for i in longest.data():
        x.append(i['p'][0]['name'])
        x.append(i['p'][-1]['name'])
    toc = time.perf_counter()
    t = (toc - tic)/60
    return x, t
# Depth of the graph


def depth():
    tic = time.perf_counter()
    x = []
    longest = session.run(
        "MATCH d = (n:Hospital)- [r:RelationType*..]->(m:Hospital) with relationships(d) as r, length(d) as depth order by depth DESC limit 1 unwind r as relation return depth, id(relation) as id, relation.rType as type")
    for i in longest.data():
        x.append(i)
    toc = time.perf_counter()
    t = (toc - tic)/60
    return x, t


if __name__ == '__main__':
    # here we will begin the session
    # begin()
    # function to extract the leaf nodes
    a, t = leaf_nodes(10)
    print(f"1) The leaf nodes in the graph are {a}")
    print("")
    print(f"The total time taken for the opeation is {t} seconds")
    print(" ")
    # function to extract parent nodes
    b, t = parent_node(10)
    print(f"2) The parent nodes are {b}")
    print(" ")
    print(f"Total time taken for this operation is {t}")
    print(" ")
    # function to extract longest path
    c, t = longest_path()
    print(
        f"3) longest path starts from : {c[0]} and ends at : {c[1]} and the total time for this operation taken is {t} seconds")
    print(" ")
    # function to extract smallest path
    c, t = smalles_path()
    print(
        f"4) smallest path starts from : {c[0]} and ends at : {c[1]} and the total time for this operation taken is {t} seconds")
    print("")
    x, t = depth()
    print("5) Depth of the Graph:")
    for i in x:
        print(i)
    print(f"Time taken for this operation is {t} seconds")
