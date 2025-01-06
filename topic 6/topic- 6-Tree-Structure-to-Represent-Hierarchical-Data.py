class TreeNode:
    def __init__(self, label):
        """Initialize a tree node with a label and an empty list of children."""
        self.label = label  # The label for the node (e.g., category name, question ID)
        self.children = []  # List to hold child nodes (e.g., subcategories, questions, answers)

    def add_child(self, child_node):
        """Add a child node to the current node."""
        self.children.append(child_node)

    def display(self, level=0):
        """Display the tree structure starting from the current node."""
        # Indentation based on the tree level
        indent = " " * (level * 4)
        print(f"{indent}{self.label}")
        # Display all children
        for child in self.children:
            child.display(level + 1)

# Example of using the Tree to represent a survey structure:

# Create the root node representing the survey
survey_tree = TreeNode("Online Survey for Education Research")

# Create category nodes
category_1 = TreeNode("Category 1: Teaching Methods")
category_2 = TreeNode("Category 2: Learning Outcomes")

# Add categories to the survey
survey_tree.add_child(category_1)
survey_tree.add_child(category_2)

# Create question nodes under Category 1
question_1 = TreeNode("Question 1: How effective is the lecture method?")
question_2 = TreeNode("Question 2: How effective is the online learning method?")

# Add questions to Category 1
category_1.add_child(question_1)
category_1.add_child(question_2)

# Create answers for Question 1
answer_1_q1 = TreeNode("Strongly Agree")
answer_2_q1 = TreeNode("Agree")
answer_3_q1 = TreeNode("Neutral")
answer_4_q1 = TreeNode("Disagree")
answer_5_q1 = TreeNode("Strongly Disagree")

# Add answers to Question 1
question_1.add_child(answer_1_q1)
question_1.add_child(answer_2_q1)
question_1.add_child(answer_3_q1)
question_1.add_child(answer_4_q1)
question_1.add_child(answer_5_q1)

# Create answers for Question 2
answer_1_q2 = TreeNode("Strongly Agree")
answer_2_q2 = TreeNode("Agree")
answer_3_q2 = TreeNode("Neutral")
answer_4_q2 = TreeNode("Disagree")
answer_5_q2 = TreeNode("Strongly Disagree")

# Add answers to Question 2
question_2.add_child(answer_1_q2)
question_2.add_child(answer_2_q2)
question_2.add_child(answer_3_q2)
question_2.add_child(answer_4_q2)
question_2.add_child(answer_5_q2)

# Create a question under Category 2
question_3 = TreeNode("Question 3: Do you think technology impacts learning outcomes?")
category_2.add_child(question_3)

# Create answers for Question 3
answer_1_q3 = TreeNode("Strongly Agree")
answer_2_q3 = TreeNode("Agree")
answer_3_q3 = TreeNode("Neutral")
answer_4_q3 = TreeNode("Disagree")
answer_5_q3 = TreeNode("Strongly Disagree")

# Add answers to Question 3
question_3.add_child(answer_1_q3)
question_3.add_child(answer_2_q3)
question_3.add_child(answer_3_q3)
question_3.add_child(answer_4_q3)
question_3.add_child(answer_5_q3)

# Display the entire survey structure
survey_tree.display()
