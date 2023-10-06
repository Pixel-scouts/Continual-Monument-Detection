import matplotlib.pyplot as plt

class_counts = {
    'kiranteshwor mahadev': 422,
    'charumati': 749,
    'kumaristhan': 669,
    'ume_maheshwara': 470,
    'jaya bageshwori': 739,
    'birupakshya': 581,
    'Naxal Bhagwati': 527,
    'Krishna_temple _kobahal': 486,
    'chakku bakku': 517,
    'golden temple': 802,
    'Ram Mandir': 598,
    'uma maheshwor': 398,
    'Maitidevi Temple': 597,
    'guyeshwori': 392,
    'nagarmandap shree kriti bihar': 432,
    'Jalbinayak': 275,
    'Ashok Stupa':694,
    'Chamundai Mai':599,    
    'Patan dhoka':529,
    'Sankha Statue':719,
    'Kumbeshwor Mahadev':601,
    'Budhha Stupa':692,
    'Bagh Bairav':409,
    'Lonha Dehar':327,
    'Nagarmandap Shree Kriti Bihar':432,
    'Mahadevsthan':859,
    'Mahayogi Guru Gorakshhyanath':733,
    'Naagpokhari':800,
    'Naxal Bhagwati':901,
    'Bal Nilkantha':763,
    'Bhubaneshwori Temple':838,
    'Bijeshwori Temple':507,
    'Buddha Statue':643,
    'Manamaiju Temple':398,
    'Pratapur Temple':879,
    'Red Gumba':644,
    'Shantidham':850,
    'Shovabhagwati Temple':605,
    'Swayambhunath':533,
    'Wishing well Swayambhu':445,
}


group2={'Chyasimdeval':217,
        'HariShankhar Temple':66,
        'Garud Statue':110,
        'Bhimsen Temple':350,
        'Mani Ganesh Temple':184,
        'Mani Mandap':35,        
        'Krishna Temple PDS':197,
        'Taleju Bell pds':211,
        'Taleju temple north':139,
        'Taleju temple south':75,
        'Vishwanath Temple':195,
        'Yog Narendra Malla Statue': 97,
        'ChaarNarayan':130,
       }

group1={'Chyasimdeval':346,
        'HariShankhar Temple':355,
        'Garud Statue':372,
        'Bhimsen Temple':379,
        'Mani Ganesh Temple':171,
        'Mani Mandap':249,        
        'Krishna Temple PDS':522,
        'Taleju Bell pds':247,
        'Taleju temple north':280,
        'Taleju temple south':209,
        'Vishwanath Temple':598,
        'Yog Narendra Malla Statue': 113,
        'Char Narayan Temple':328,
       }
test={'birupakshya':  58,
    'Ram Mandir':  59,
    'jaya bageshwori':  74,
    'charumati':  76,
    'kiranteshwor mahadev':  41,
    'guyeshwori':  66,
    'Maitidevi Temple':  61,
    'kumaristhan':  66,
    'Naxal Bhagwati':  52,
    'chakku bakku':  51,
    'ume_maheshwara':  47,
    'golden temple':  80,
    'Krishna_temple kobahal':  48,
    'uma maheshwor':  64,
    'Jalbinayak':  55,
    'nagarmandap shree kriti bihar':  43,
}

val={'birupakshya':  58,
    'Ram Mandir':  59,
    'jaya bageshwori':  74,
    'charumati':  75,
    'kiranteshwor mahadev':  42,
    'guyeshwori':  66,
    'Maitidevi Temple':  61,
    'kumaristhan':  66,
    'Naxal Bhagwati':  52,
    'chakku bakku':  51,
    'ume_maheshwara':  47,
    'golden temple':  80,
    'Krishna_temple _kobahal':  47,
    'uma maheshwor':  64,
    'Jalbinayak':  55,
    'nagarmandap shree kriti bihar':  43,
    }

train={
    'birupakshya':  465,
    'Ram Mandir':  477,
    'jaya bageshwori':  591,
    'charumati':  598,
    'kiranteshwor mahadev':  339,
    'guyeshwori':  532,
    'Maitidevi Temple':  489,
    'kumaristhan':  537,
    'Naxal Bhagwati':  424,
    'chakku bakku':  415,
    'ume_maheshwara':  376,
    'golden temple':  642,
    'Krishna_temple _kobahal':  391,
    'uma maheshwor':  515,
    'Jalbinayak':  440,
    'nagarmandap shree kriti bihar':  346,
}


classes = list(test.keys())
count1 = list(train.values())
count2 = list(test.values())
count3 = list(val.values())
fig, ax = plt.subplots(figsize=(8,6))
sum_values = [count1_val + count2_val+ count3_val for count1_val, count2_val,count3_val in zip(count1, count2,count3)]
a=ax.bar(classes, sum_values)
ax.bar_label(a,padding=5,fontsize=8)
ax.set_ylim(0,1000)
ax.set_xlabel('monuments', fontweight='bold')
ax.set_ylabel('no of instances', fontweight='bold')





# class1=list(group1.keys())
# count1=list(group1.values())
# class2=list(group2.keys())
# count2=list(group2.values())
# fig, ax=plt.subplots()
# # ax.bar(class1, count1)
# # ax.bar(class1, count2)

# ax.set_xlabel('monument')
plt.xticks(rotation=90,fontsize=8)
# ax.set_ylabel('no of instances')
ax.set_title('Total dataset')
plt.tight_layout()
plt.savefig("total.png", dpi=None, bbox_inches='tight', format='png')


plt.show()





# # Get the common keys from both group1 and group2
# common_keys = list(set(group1.keys()) & set(group2.keys()))

# # Sort the keys for consistent plotting
# common_keys.sort()

# # Get the values corresponding to the common keys
# count1 = [group1[key] for key in common_keys]
# count2 = [group2[key] for key in common_keys]

# # Set the width of the bars
# bar_width = 0.4

# fig, ax = plt.subplots()

# # Calculate the positions for the bars in group1 and group2
# pos_group1 = [pos - bar_width/2 for pos in range(len(common_keys))]
# pos_group2 = [pos + bar_width/2 for pos in range(len(common_keys))]

# # Plot the bars for group1 and group2
# ax.bar(pos_group1, count1, width=bar_width, label='Existed dataset')
# ax.bar(pos_group2, count2, width=bar_width, label='Extended dataset')

# ax.set_xlabel('Monument Classes')
# plt.xticks(range(len(common_keys)), common_keys, rotation=90, fontsize=8)
# ax.set_ylabel('Classes Count')
# plt.legend()
# plt.tight_layout()
# plt.show()



# # Get the common keys from both group1 and group2
# common_keys = list(set(group1.keys()) & set(group2.keys()))

# # Sort the keys for consistent plotting
# common_keys.sort()

# # Get the values corresponding to the common keys
# count1 = [group1[key] for key in common_keys]
# count2 = [group2[key] for key in common_keys]

# # Calculate the sum of values from group1 and group2
# sum_values = [count1_val + count2_val for count1_val, count2_val in zip(count1, count2)]

# # Set the width of the bars
# bar_width = 0.4

# fig, ax = plt.subplots()

# # Calculate the positions for the bars in group1 and group2
# pos_group1 = [pos - bar_width/2 for pos in range(len(common_keys))]
# pos_group2 = [pos + bar_width/2 for pos in range(len(common_keys))]

# # Plot the bars for group1 and group2
# ax.bar(pos_group1, count1, width=bar_width, label='Group 1')
# # ax.bar(pos_group2, count2, width=bar_width, label='Group 2')

# # Plot the bars for the sum
# ax.bar(pos_group2, sum_values, width=bar_width, label='Sum', alpha=0.5)


# ax.set_xlabel('Monument Classes')
# plt.xticks(range(len(common_keys)), common_keys, rotation=90, fontsize=8)
# ax.set_ylabel('Classes Count')
# plt.legend()
# plt.tight_layout()
# plt.show()



# import matplotlib.pyplot as plt
# classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']
# count = [20, 45, 30, 80, 50]
# fig, ax = plt.subplots()
# ax.bar(classes, count)

# ax.set_xlabel('Monument Classes')
# plt.xticks(rotation=45)
# ax.set_ylabel('Classes count')

# plt.tight_layout()
# plt.show()

# import os
# import xml.etree.ElementTree as ET
# import matplotlib.pyplot as plt

# def count_images_by_class(directory_path):
#     class_counts = {}

#     for filename in os.listdir(directory_path):
#         if filename.endswith('.xml'):
#             xml_file_path = os.path.join(directory_path, filename)
#             tree = ET.parse(xml_file_path)
#             root = tree.getroot()

#             # Get the class name from the XML file
#             class_name = root.find('object').find('name').text

#             # Count the class occurrences
#             class_counts[class_name] = class_counts.get(class_name, 0) + 1

#     return class_counts

# if __name__ == '__main__':
#     directory_path = 'D:\Major\Dataset\check_for_plot'
#     class_counts = count_images_by_class(directory_path)

#     # Plot the class counts using a bar plot
#     plt.bar(class_counts.keys(), class_counts.values())
#     plt.xlabel('Class')
#     plt.ylabel('Count')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()