
### Instruction
#### Step one: start the [Neo4j desktop](https://neo4j.com/download-center/#desktop) 
#### Step two: Create a new project and then create a local DBMS connection with a password as "1234" and click on start which will navigate to the Neo4j browser.
#### Step three: come back to the Neo4j desktop and Copy the data.csv file provided in the zip folder to the import folder which can be done by clicking the open_folder - import
#### Step four: run the csc790.py file as python [csc790.py](https://github.com/sakibb019/Advance-Database-project/blob/main/CSC790.py) and you will see the results. 

### Result
#### 1. The leaf nodes in the graph are ```['Dr.Asif', 'Dr.Mohammed', 'Dr.MVRao', 'Dr.Sayeed', 'Dr.Sai', 'Dr.Ganesh', 'Dr.mallesh', 'Dr.Mallikaarjun', 'Dr.Shahed', 'Dr.Jani'] ```. The total time taken for the opeation is 0.03423326499760151 seconds
#### 2. The parent nodes are ``` ['Apollo_Hospital', 'Redhills', 'Madhapur', 'Banjarahills', 'Jubliehills', 'Block_R1', 'Block_R2', 'Block_R3', 'Block_R4', 'Block_R5'] ``` Total time taken for this operation is 5.088833471139272e-05
#### 3. longest path starts ``` from : Apollo_Hospital ``` and ends ``` at : Pitbull```  and the total time for this operation taken is 0.0005533333324516813 seconds
#### 4. smallest path starts ``` from : Apollo_Hospital ``` and ``` ends at : Jubliehills ``` and the total time for this operation taken is 0.00035224000457674266 seconds 

#### 5. Depth of the Graph
| Depth| id| type|
|:-----:|----:|-----:|
|10|0|location|
|10|9|Building|
|10|33|Department|
|10|57|Department head|
|10|81|Doctor|
|10|89|Jr. Doctor|
|10|93|Nurse|
|10|97|Assigned rooms|
|10|101|Patient|
|10|105|Care taker|

Time taken for this operation is 0.00014359999913722278 seconds
