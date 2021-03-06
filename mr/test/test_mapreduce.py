# test_mapreduce.py
#
# Used to test the mr.py MapReduce library's mapreduce functionality.
#
# The program has two parameters: n, and cluster_size, defined in the first
# two lines of code.  The program computes the sum of j*j over the range j 
# from 1 to n, using a MapReduce job running on cluster_size machines.
#
# The result should be n*(n+1)*(2n+1)/6

n = 500
cluster_size = 1

import mr
cluster = mr.cluster(cluster_size)
cluster.create_dict("integers.dict",xrange(n))
cluster.create_dict("sum_of_squares.dict",[0])
cluster.mr("test_mapreduce_fn.py",[],[],"integers.dict","sum_of_squares.dict","answer")

print "Computing the sum of squares of integers from 1 to "+str(n)+"."
print "The correct answer should be "+str(n*(n+1)*(2*n+1)/6)+"."
print "The MapReduce job returns "+str(cluster.get_dict_value("sum_of_squares.dict",0)["answer"])+"."
cluster.shutdown()