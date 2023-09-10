# Step 4: Create a Program

# Step 5: Read and Index Documents
def create_index(document_path):
    index = {}  # Initialize an empty index
    with open(document_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines):
            words = line.strip().split()
            for word in words:
                word = word.lower()  # Convert to lowercase for case-insensitive search
                if word not in index:
                    index[word] = []
                index[word].append(line_number + 1)  # Line numbers start from 1
    print(index)
    return index

# Step 6: Build a Search Function
def search(query, index):
    query = query.lower()  # Convert the query to lowercase for consistency
    if query in index:
        return index[query]
    else:
        return []

# Main program
if __name__ == "__main__":
    # Step 5: Read and Index Documents
    document_path = "navbar.txt"  # Change this to your text file name
    index = create_index(document_path)
    
    # Step 6: Build a Search Function
    while True:
        user_query = input("Enter a word to search (or 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        else:
            results = search(user_query, index)
            if results:
                print(f"Word '{user_query}' found in lines: {', '.join(map(str, results))}")
            else:
                print(f"Word '{user_query}' not found in the document.")
