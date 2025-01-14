# Write a Python function that implements the decision tree learning algorithm for classification. 
# The function should use recursive binary splitting based on entropy and information gain to build a decision tree. 
# It should take a list of examples (each example is a dict of attribute-value pairs) and a list of attribute names as input, 
# and return a nested dictionary representing the decision tree.

# Example:
#         input: examples = [
#                     {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
#                     {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
#                     {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
#                     {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
#                 ],
#                 attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
#         output: {
#             'Outlook': {
#                 'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}},
#                 'Overcast': 'Yes',
#                 'Rain': {'Wind': {'Weak': 'Yes', 'Strong': 'No'}}
#             }
#         }
#         reasoning: Using the given examples, the decision tree algorithm determines that 'Outlook' is the best attribute to split the data initially. 
#         When 'Outlook' is 'Overcast', the outcome is always 'Yes', so it becomes a leaf node. In cases of 'Sunny' and 'Rain', it further splits based on 'Humidity' and 'Wind', 
#         respectively. The resulting tree structure is able to classify the training examples with the attributes 'Outlook', 'Temperature', 'Humidity', and 'Wind'.

import math
from collections import Counter
def calculate_entropy(labels):
    label_counts = Counter(labels)
    total_count = len(labels)
    entropy = -sum((count/total_count) * math.log2(count/total_count) for count in label_counts.values())
    return entropy

def calculate_information_gain(examples, attr, target_attr):
    total_entropy = calculate_entropy([example[target_attr] for example in examples])
    values = set(example[attr] for example in examples)
    attr_entropy = 0
    for value in values:
        value_subset = [example[target_attr] for example in examples if example[attr] == value]
        value_entropy = calculate_entropy(value_subset)
        attr_entropy += (len(value_subset) / len(examples)) * value_entropy
    return total_entropy - attr_entropy

def majority_class(examples, target_attr):
    return Counter([example[target_attr] for example in examples]).most_common(1)[0][0]

def learn_decision_tree(examples, attributes, target_attributes):
    if not examples:
        return 'No examples'
    
    if all(example[target_attributes] == examples[0][target_attributes] for example in examples):
        return examples[0][target_attributes]
    
    if not attributes:
        return majority_class(examples, target_attributes)
    
    gains = {attr: calculate_information_gain(examples, attributes, target_attributes) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}
    
    for value in set(example[best_attr] for example in examples):
        subset = [example for example in examples if example[best_attr] == value]
        new_attributes = attributes.copy()
        new_attributes.remove(best_attr)
        subtree = learn_decision_tree(subset, new_attributes, target_attributes)
        tree[best_attr][value] = subtree
    
    return tree