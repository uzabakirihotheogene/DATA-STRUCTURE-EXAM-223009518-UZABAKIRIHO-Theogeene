def merge_sort(arr, key='priority_score'):
    """Perform merge sort on an array of survey responses based on priority_score."""
    if len(arr) > 1:
        # Find the middle of the list
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half, key)
        merge_sort(right_half, key)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # If there are any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def display_responses(responses):
    """Display the list of survey responses."""
    for response in responses:
        print(f"Response ID: {response['response_id']}, Priority Score: {response['priority_score']}, Text: {response['response_text']}")

# Example Survey Responses (unsorted)
survey_responses = [
    {"response_id": 1001, "priority_score": 5, "response_text": "Agree"},
    {"response_id": 1002, "priority_score": 2, "response_text": "Strongly Disagree"},
    {"response_id": 1003, "priority_score": 4, "response_text": "Neutral"},
    {"response_id": 1004, "priority_score": 1, "response_text": "Strongly Agree"},
    {"response_id": 1005, "priority_score": 3, "response_text": "Disagree"}
]

# Display original survey responses
print("Original Survey Responses:")
display_responses(survey_responses)
print()

# Sort the survey responses based on priority_score using Merge Sort
merge_sort(survey_responses, key='priority_score')

# Display sorted survey responses
print("Sorted Survey Responses (by Priority Score):")
display_responses(survey_responses)
