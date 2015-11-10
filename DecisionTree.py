from math import log

fields = {0 : "Age", 1 : "Sex", 2 : "Chest pain type", 3 : "Resting bp", 4 : "Cholesteral", 5 : "Fasting blood sugar", 6 : "Resting ecg", 7 : "Max Heart rate", 8 : "Angina", 9 : "Oldpeak", 10 : "Slope", 11 : "Colored Vessels", 12 : "Thal", 13 : "H/S"}

def process(fname):
    '''
    Process data file to replace unknown input parameters
    marked by "?" with "-ve"
    '''
    f = fopen(fname, "r")
    data = []
	for line in f:
		d = {}		
		l = line.split()
		n = 0
		for i in l:
			if i == "?":
				d[n] = "-ve"
			else:	
				d[n] = i
			n += 1
		data.append(d)
    return data

def probability(Data, attr):
    '''
    Return probability distribution of all unique values that attrubute 'attr'
    can take in the given data set
    '''
	freq = {}
	for x in Data:
		value = x[attr]
		if value != "-ve":
			if value in freq.keys():
				freq[value] += 1
			else:
				freq[value] = 1		
	for attribute, count in freq.items():
		freq[attribute] = count / len(Data)

	return freq

def entropy(Data, attr):
    '''
    Compute entropy of data with respect to given target attribute 'attr'
    x - all values that attribute can have
    p[x] - probability of value of an attribute
    H[x] - entropy of data wrt attribute x
    
    H[x] = - sum_over_all_x(p[x] * log_base2(p[x]))
    '''
	sum = 0
	p = probability(Data, attr)
	for value, prob in p.items():
		try:
			sum += prob * log(prob)
		except:
			pass
	return -1 * sum
			
def gain(Data, attr, target_attr):
    '''
    Information gain - Mutual information between input attribute A and target variable Y
    S - data sample
    A - input attribute A
    Y - target attribute
    v - all values of A
    Sv - subset of S with value of attribute A to be v

    Gain(S,A) = Entropy(S) - sum_over_v((|Sv| / |S|) * Entropy(Sv))
	'''
    Es = entropy(Data, target_attr)

	Esv = 0

	freq = {}	
	for record in Data:
		if record[attr] in freq.keys():
			freq[record[attr]] += 1
		else:
			freq[record[attr]] = 1
	
	for val in freq.keys():
		prob = freq[val] / sum(freq.values())
		subset_data = [record for record in Data if record[attr] == val]
		Esv += prob * entropy(subset_data, target_attr)
	return Es - Esv
		

def unique(data, target_attr):
    '''
    Return if target attribute have only one value in data set
    '''
	u = [record[target_attr] for record in data]
	if u.count(u[0]) == len(u):
		return u, 1
	else:
		return False, 0

def maximum_value(data, target_attr):
    '''
    Return maximum occurence of a unique value of target attribute in data
    '''
	vals = [record[target_attr] for record in data]
	count = {}
	for item in vals:
		if item in count.keys():
			count[item] += 1
		else:
			count[item] = 1
	return max(count.values())

def best_attribute(data, target_attr, attr):
    '''
    Return next best attribute
    This is the attribute for which data has maximum gain
    '''
	Gains={}
	for i in attr:
		Gains[i] = gain(data, i, target_attr)

	maxGain = max(Gains.values())
	for attribute, attrGain in Gains.items():
		if attrGain == maxGain:
			maxAttr = attribute
	return maxAttr
	
def ID3(data, target_attr, attr):
    '''
    ID3 algorithm for construction of decision tree
    This algorithm constructs the decision tree recursively
    '''

    #root of the decision tree
	tree = {}

    #check if all examples in data have single value of attribute
	record,truth = unique(data, target_attr)

    #all examples have same value of attribute in the data
	if truth != 0:
        #root node is that one value of the attribute
		tree = record
	
    #no more attributes to be considered
	elif len(attr)==0:
        #return tree with single node root labelled with most common value of target attribute in the data
		tree = maximum_value(data, target_attr)
		
    #otherwise
	else:
		#find best decision attribute A
		A = best_attribute(data, target_attr, attr)
		print("best attribute=",A)
		
        #root node labelled with best decision attribute
        tree={A:{}}

        #all unique values of A in data
		values=list(set([record[A] for record in data]))	#set of values = unique set of values of attribute A or all values of A including repititions?

		#print("No of ways of classifying attribute %s : %d"%(fields[A],len(values)))

        #for all values of A
		for vi in values:
            #find subset of data that have vi as attribute value of A
			examples = [rec for rec in data if rec[A] == vi]

			#should A be removed permanently from attribute list?
			#add subtree to tree
            tree[A][vi] = ID3(examples,target_attr, [a for a in attr if a != A])

	return tree
			
if __name__ == "__main__":
	level = 0
	node = 0
    nparams = 13    #no. of input parameters in data set
    fname = "data.txt"
	data = process(fname)
    
	Gain = {}
	for i in range(0, nparams):
		Gain[i] = gain(data, i, nparams)

	for i in Gain.keys():
		print("gain(%s)=%f"%(fields[i], Gain[i]))

	y = max(Gain.values())
	print(y,{x for x in Gain.keys() if Gain[x] == y})
	l = list(range(0, nparams))
	DecisionTree = ID3(data, nparams, l)

	print(DecisionTree)
