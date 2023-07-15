import numpy as np
import pickle as pkl
import pandas as pd

def BNet_to_int(filetoconv):
    """
    filetoconv: BNet file to convert into list of int of BF outputs
    """
    node_num = {}
    in_edges = {}
    all_list = []
    all_list1 = []
    c=0
    with open(filetoconv, 'r') as file1:
        for line in file1.readlines()[1:]:
            all_list += line.split(',')
            line = line.replace('(',' ( ').replace(')',' ) ').replace('!',' ! ')
            all_list1.append(line.split())
            node_num[line.split(',')[0]] = c
            c+=1
        ss = ''.join(all_list)
        ss = ss.replace('|', '').replace('!', '').replace('&', '').replace('(', '').replace(')', '').replace('[','').replace(']','')
        g = ss.split('\n')
        w = []
        for ele in g:
            w += ele.split()
        w = list(set(w))
        no_inp_nodes = []
        for item in w:
            if item not in node_num.keys():
                node_num[item] = c
                c+=1
                no_inp_nodes.append(item)

        for row in all_list1:
            a = [k for k in row if k in node_num.keys()]
            b = str(row).split(',')[0][2:]
            in_edges[node_num[b]] = list(set([node_num[k] for k in a]))
        for item in no_inp_nodes:
            in_edges[node_num[item]] = [node_num[item]]
        #print(node_num)
        #print(in_edges)
    file1.close()

    file3 = open(filetoconv, 'r')
    g = file3.read()
    g = g.replace('&','and').replace('!','not ').replace('|', 'or')
    g1 = g.split('\n')
    g1.pop(0)
    if len(g1[-1]) == 0:
       g1.pop(-1)
    num_node = {v: k for k, v in node_num.items()}
    BF_int_list = []
    for i in range(len(num_node)):
        if num_node[i] not in no_inp_nodes:
            k = in_edges[i]
            z = [str(bin(i)[2:].zfill(len(k))) for i in range(2**len(k))]
            bfstr= ''
            ll = []
            for num in k:
                ll.append(num_node[num].replace('/','_'))
            for item in z:
                for no in range(len(ll)):
                   exec("%s = %d" % (ll[no],int(item[no])))
                Q = eval(g1[i].split(',')[1][1:].replace('/','_'))
                bfstr = bfstr + str(int(Q))
            BF_int_list.append(int(bfstr,2))
        else:
            BF_int_list.append(1)
    file3.close()
    return node_num, in_edges, BF_int_list, num_node

def BNet_to_signed_edgelist(in_edges, BF_int_list, num_node):
    """
    in_edges: dict where nodes as keys with input nodes as their values
    BF_int_list: list of BFs as integers
    num_node: dict mapping numbers to nodes in Boolean Network
    """
    frolist, tolist, signlist = [],[],[]
    edgelistdict = {'from':frolist, 'to':tolist, 'sign':signlist}
    for i in in_edges:
        f = bin(BF_int_list[i])[2:].zfill(2**len(in_edges[i]))
        a = check_if(len(in_edges[i]), f).is_UF()
        for j in range(len(a)):
            frolist.append(num_node[in_edges[i][j]] )
            tolist.append(num_node[i])
            signlist.append(a[j])
    return  pd.DataFrame(edgelistdict)

def int_to_DNF(k, BF_int, node_list, simplify = False):
    '''
    k: number of inputs to a node
    BF_int: Boolean function represented as a decimal number
    node_list: the list of nodes in Boolean Network
    returns a DNF expression of the BF
    '''
    f = np.binary_repr(BF_int, 2**k)
    indices = [bin(i)[2:].zfill(k) for i, bit in enumerate(f) if bit == '1']
    dnf = ''
    for ele in indices:
        s = ''
        for i in range(k):
            if ele[i] == '1':
                s += node_list[i]+' & '
            else:
                s += '!'+ node_list[i] +' & '
        s = s[:-3]
        dnf += '(' + s + ')' + ' | '
    dnf = dnf[:-3]

    if simplify == False:
        return dnf
    else:
        new_dnf = dnf.replace('!', '~')
        simplify_dnf = str(simplify_logic(parse_expr(new_dnf), 'dnf'))
        return simplify_dnf.replace('~', '!')

def ints_to_BNet(fname, node_num, in_edges, BF_int_list, simplify=False):
    '''
    path: Location to which the bnet file is to be saved
    Converts a list of boolean functions into a bnet file
    '''
    bnet = ['targets' + ',\t' + 'factors' + '\n']
    node_num = {node_num[ele]:ele for ele in node_num}
    for num in node_num:
        if len(in_edges[num]) == 0:
            bnet += [node_num[num] + ',\t' + f'({node_num[num]})' + '\n']
        else:
            inp_genes = [node_num[index] for index in in_edges[num]]
            bnet += [node_num[num] + ',\t' + int_to_DNF(len(in_edges[num]), BF_int_list[num], inp_genes, simplify) + '\n']
    with open(fname, 'w') as file:
        file.writelines(bnet)
    return f'BoolNet file saved at {fname}...'