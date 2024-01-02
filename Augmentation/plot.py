import matplotlib.pyplot as plt

train = {
'Akash Bhairav': 850,
'ashok stupa': 1112,
'Badrinath': 545,
'Bagbairav': 628,
'Balkumari, Bhaktapur': 817,
'BalNilkantha': 832,
'basantapur tower': 697,
'Bhadrakali Temple': 909,
'bhairavnath temple': 803,
'bhaktapur tower': 773,
'bhimeleshvara': 740,
'Bhimsen Temple': 612,
'bhupatindra malla column': 685,
'bhuvana lakshmeshvara': 549,
'birupakshya': 930,
'Buddha Statue': 798,
'chakku bakku': 615,
'chamunda mai': 962,
'Chandeshwori Temple': 828,
'Char Narayan Temple': 608,
'charumati': 1201,
'chasin dega': 591,
'Chayasilin Mandap': 729,
'Dakshin Barahi': 814,
'degu tale': 930,
'Dharahara': 802,
'Fasidega Temple': 1140,
'Garud Statue': 576,
'garud': 1068,
'Ghantaghar': 1214,
'golden gate': 617,
'golden temple': 963,
'Gopinath Krishna Temple': 810,
'guyeshwori': 895,
'hanuman idol': 709,
'Harishankar Temple': 608,
'indrapura': 542,
'Isckon Temple': 702,
'jagannatha temple': 395,
'Jalbinayak': 876,
'Jamachen Monastry': 852,
'jame masjid': 842,
'jaya bageshwori': 889,
'kala-bhairava': 686,
'kasthamandap': 532,
'kavindrapura sattal': 588,
'Kedamatha Tirtha': 587,
'Khumbeshwor mahadev': 843,
'kiranteshwor mahadev': 673,
'kirtipur tower': 782,
'Kotilingeshvara': 909,
'Krishna mandir PDS': 618,
'Krishna_temple _kobahal': 781,
'Kumari Ghar': 602,
'kumaristhan': 806,
'kumbheshwor mahadev': 717,
'lalitpur tower': 678,
'lokeshwor temple bhaktapur': 994,
'Lumadhi Bhadrakali Temple Sankata': 1120,
'Mahabauddha Asan': 716,
'Mahadev Temple': 876,
'Maipi Temple': 686,
'Maitidevi Temple': 978,
'manamaiju temple': 640,
'nagarmandap shree kriti bihar': 692,
'narayan temple': 533,
'National Gallery': 692,
'Naxal Bhagwati': 847,
'Nyatapola temple': 847,
'Palace of 55 Windows': 506,
'Panchamukhi Hanuman': 875,
'Patan Dhoka': 850,
'Pilot Baba': 801,
'PimBahal Gumba': 831,
'pratap malla column': 874,
'pratappur temple': 1257,
'Ram Mandir': 957,
'Ranipokhari': 959,
'red gumba': 774,
'sahid gate': 928,
'Sankha Statue': 1006,
'Sano Pashupati': 864,
'Santaneshwor Mahadev': 1026,
'shantidham': 592,
'Shiva Temple': 753,
'shveta bhairava': 616,
'Siddhi Lakshmi temple': 1034,
'simha sattal': 539,
'Swoyambhunath': 949,
'taleju bell pds': 536,
'taleju bell_BDS': 804,
'taleju bell_KDS': 1036,
'taleju temple': 597,
'taleju_temple_south': 561,
'trailokya mohan': 688,
'Tridevi Temple': 1034,
'uma maheshwor': 1070,
'ume_maheshwara': 752,
'Vastala Temple': 706,
'vishnu temple': 537,
'Wakupati Narayan Temple': 674,
'wishing well budhha statue': 714,
'Yetkha Bahal': 872,
'yog_narendra_malla_statue': 558
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

test={
'Akash Bhairav': 106,
'ashok stupa': 138,
'Badrinath': 66,
'Bagbairav': 60,
'Balkumari, Bhaktapur': 101,
'BalNilkantha': 104,
'basantapur tower': 86,
'Bhadrakali Temple': 112,
'bhairavnath temple': 99,
'bhaktapur tower': 93,
'bhimeleshvara': 93,
'Bhimsen Temple': 102,
'Bhupatindra Malla Column': 80,
'bhuvana lakshmeshvara': 71,
'birupakshya': 116,
'Buddha Statue': 98,
'chakku bakku': 51,
'chamunda mai': 118,
'Chandeshwori Temple': 102,
'Char Narayan Temple': 54,
'charumati': 149,
'chasin dega': 74,
'Chayasilin Mandap': 96,
'Dakshin Barahi': 100,
'degu tale': 113,
'Dharahara': 98,
'Fasidega Temple': 135,
'Garud Statue': 62,
'garud': 134,
'Ghantaghar': 141,
'golden gate': 55,
'golden temple': 120,
'Gopinath krishna Temple': 97,
'guyeshwori': 132,
'hanuman idol': 90,
'Harishankar Temple': 62,
'indrapura': 53,
'Isckon Temple': 86,
'jagannatha temple': 48,
'Jalbinayak': 110,
'Jamachen Monastry': 106,
'jame masjid': 104,
'jaya bageshwori': 111,
'kala-bhairava': 54,
'kasthamandap': 65,
'kavindrapura sattal': 72,
'Kedamatha Tirtha': 60,
'Khumbeshwor mahadev': 102,
'kiranteshwor mahadev': 85,
'kirtipur tower': 98,
'Kotilingeshvara': 114,
'Krishna mandir PDS': 68,
'Krishna_temple _kobahal': 96,
'Kumari Ghar': 48,
'kumaristhan': 99,
'kumbheshwor mahadev': 66,
'lalitpur tower': 55,
'lokeshwor temple bhaktapur': 124,
'Lumadhi Bhadrakali Temple Sankata': 140,
'Mahabauddha Asan': 88,
'mahadev temple': 108,
'Maipi Temple': 46,
'Maitidevi Temple': 122,
'manamaiju temple': 78,
'nagarmandap shree kriti bihar': 86,
'narayan temple': 53,
'National Gallery': 60,
'Naxal Bhagwati': 104,
'Nyatapola temple': 130,
'Palace of 55 Windows': 61,
'Panchamukhi Hanuman': 110,
'Patan Dhoka': 104,
'Pilot Baba': 97,
'PimBahal Gumba': 103,
'pratap malla column': 64,
'pratappur temple': 160,
'Ram Mandir': 118,
'Ranipokhari': 118,
'red gumba': 96,
'sahid gate': 116,
'Sankha Statue': 124,
'Sano Pashupati': 108,
'Santaneshwor Mahadev': 128,
'shantidham': 74,
'Shiva Temple': 91,
'shveta bhairava': 54,
'Siddhi Lakshmi temple': 135,
'simha sattal': 67,
'Swoyambhunath': 111,
'taleju bell pds': 52,
'taleju bell_BDS': 99,
'taleju bell_KDS': 128,
'taleju temple': 57,
'taleju_temple_south': 67,
'trailokya mohan': 58,
'Tridevi Temple': 128,
'uma maheshwor': 152,
'ume_maheshwara': 94,
'Vastala Temple': 51,
'vishnu temple': 63,
'Wakupati Narayan Temple': 82,
'wishing well budhha statue': 88,
'Yetkha Bahal': 108,
'yog_narendra_malla_statue': 58
}

val={'Akash Bhairav': 106,
 'Badrinath': 48,
 'Bagbairav': 60,
 'BalNilkantha': 104,
 'Balkumari, Bhaktapur': 101,
 'Bhadrakali Temple': 112,
 'Bhimsen Temple': 102,
 'Bhupatindra Malla Column': 53,
 'Buddha Statue': 98,
 'Chandeshwori Temple': 102,
 'Char Narayan Temple': 54,
 'Chayasilin Mandap': 58,
 'Dakshin Barahi': 100,
 'Dharahara': 98,
 'Fasidega Temple': 49,
 'Garud Statue': 52,
 'Ghantaghar': 141,
 'Gopinath Krishna Temple': 58,
 'Gopinath krishna Temple': 87,
 'Harishankar Temple': 62,
 'Isckon Temple': 86,
 'Jalbinayak': 110,
 'Jamachen Monastry': 106,
 'Kedamatha Tirtha': 60,
 'Khumbeshwor mahadev': 102,
 'Kotilingeshvara': 88,
 'Krishna mandir PDS': 68,
 'Krishna_temple _kobahal': 96,
 'Kumari Ghar': 48,
 'Lumadhi Bhadrakali Temple Sankata': 140,
 'Mahabauddha Asan': 88,
 'Maipi Temple': 66,
 'Maitidevi Temple': 122,
 'National Gallery': 80,
 'Naxal Bhagwati': 104,
 'Nyatapola temple': 130,
 'Palace of 55 Windows': 67,
 'Panchamukhi Hanuman': 102,
 'Patan Dhoka': 104,
 'Pilot Baba': 97,
 'PimBahal Gumba': 103,
 'Ram Mandir': 118,
 'Ranipokhari': 118,
 'Sankha Statue': 124,
 'Sano Pashupati': 108,
 'Santaneshwor Mahadev': 128,
 'Shiva Temple': 91,
 'Siddhi Lakshmi temple': 135,
 'Swoyambhunath': 106,
 'Tridevi Temple': 128,
 'Vastala Temple': 61,
 'Wakupati Narayan Temple': 82,
 'Yetkha Bahal': 108,
 'ashok stupa': 138,
 'badrinath': 58,
 'basantapur tower': 86,
 'bhairavnath temple': 99,
 'bhaktapur tower': 93,
 'bhimeleshvara': 93,
 'bhupatindra malla column': 67,
 'bhuvana lakshmeshvara': 71,
 'birupakshya': 116,
 'chakku bakku': 51,
 'chamunda mai': 118,
 'charumati': 149,
 'chasin dega': 74,
 'chayasilin mandap': 58,
 'chyasilin mandap': 70,
 'degu tale': 113,
 'fasidega temple': 126,
 'garud': 134,
 'golden gate': 35,
 'golden temple': 120,
 'gopinath krishna temple': 62,
 'guyeshwori': 132,
 'hanuman idol': 90,
 'indrapura': 63,
 'jagannatha temple': 48,
 'jame masjid': 104,
 'jaya bageshwori': 111,
 'kala-bhairava': 64,
 'kasthamandap': 65,
 'kavindrapura sattal': 72,
 'kiranteshwor mahadev': 85,
 'kirtipur tower': 98,
 'kotilingeshvara': 66,
 'kumaristhan': 99,
 'kumbheshwor mahadev': 56,
 'lalitpur tower': 55,
 'lokeshwor temple bhaktapur': 124,
 'mahadev temple': 108,
 'manamaiju temple': 78,
 'nagarmandap shree kriti bihar': 86,
 'narayan temple': 73,
 'palace of the 55 windows': 53,
 'panchamukhi hanuman': 68,
 'pratap malla column': 44,
 'pratappur temple': 160,
 'red gumba': 96,
 'sahid gate': 116,
 'shantidham': 74,
 'shveta bhairava': 54,
 'simha sattal': 67,
 'swayambhunath': 55,
 'taleju bell pds': 42,
 'taleju bell_BDS': 99,
 'taleju bell_KDS': 128,
 'taleju temple': 57,
 'taleju_temple_south': 67,
 'trailokya mohan': 48,
 'uma maheshwor': 152,
 'ume_maheshwara': 94,
 'vastala temple': 60,
 'vishnu temple': 63,
 'wishing well budhha statue': 88,
 'yog_narendra_malla_statue': 68}


classes = list(test.keys())
count1 = list(train.values())
count2 = list(test.values())
count3 = list(val.values())
fig, ax = plt.subplots(figsize=(12,6))
sum_values = [count1_val + count2_val+ count3_val for count1_val, count2_val,count3_val in zip(count1, count2,count3)]
a=ax.bar(classes, count1)
ax.bar_label(a,padding=5,fontsize=5)
ax.set_ylim(0,1600)
ax.set_xlabel('monuments', fontweight='bold')
ax.set_ylabel('no of instances', fontweight='bold')



# ax.set_xlabel('monument')
plt.xticks(rotation=90,fontsize=7)
# ax.set_ylabel('no of instances')
ax.set_title('Train dataset')
plt.tight_layout()
plt.savefig("train.png", dpi=None, bbox_inches='tight', format='png')


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