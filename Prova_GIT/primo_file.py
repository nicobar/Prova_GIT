#import ciscoconfparse as c

#po_vlan_string = '7-11,13,14,18,19,22,23,31,32,37,38,43,45,47,49-57,65,69,74-78,91-97,105,130,143,145,156,170-181,184,192-197,260,261,289,299,322-324,327-329,536,537,600-609,614,615,631-639,643-654,721,740,741,820-827,830,831,868,869,878'

po_vlan_string = '7,20,22,23,25-27,38,46-51,58,60,127,128,130,135,140,145,156,195-197,299,322-324,327-329,600-603,610-613,632,634-636,639-650,660-665,820-822,850,870-872'

# def get_all_vlan_list(conf)
#     parse = c.CiscoConfParse(conf)
#
#     list_obj = parse.find_objects('vlan')
#
#     for obj in list_obj:
# CIAO
# uno master and uno pippo


def primo_commit_in_dev_081117():
    pass


def secondo_commit_in_master():  # change
    pass


def terzo_commit_in_master():
    pass


def primo_commit_in_dev():
    pass


def secondo_commit_in_dev():
    pass


def primo_commit_in_dev_dopo_merge():
    pass


def from_range_to_list(range_str):

    l = []

    h_l = range_str.split('-')
    start = int(h_l[0])
    stop = int(h_l[1])
    for x in range(start, stop + 1):
        l.append(x)
    return l


vlan_l = po_vlan_string.split(',')
vlan_set = set()


for v in vlan_l:

    if v.find('-') > 0:
        help_l = from_range_to_list(v)
        for elem in help_l:
            vlan_set.add(int(elem))
    else:
        vlan_set.add(int(v))

lst = list(vlan_set)
lst.sort()
print(lst)
for i in lst:
    print(i)
