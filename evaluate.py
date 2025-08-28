# evaluate.py
import main # Import the main parser function
import time
import json

# Evaluation dataset (a sample of 5 cases for demonstration)
TEST_CASES = [
    {"name": "Easy - Open App", "command": "open calculator", "tier": 1},
    {"name": "Easy - Create File", "command": 'write a file named "easy.txt" with content "test"', "tier": 1},
    {"name": "Medium - Open App with extra words", "command": "can you please launch notepad for me", "tier": 2},
    {"name": "Hard - Complex file content", "command": 'create a file named "report.csv" with content "id,name\\n1,test"', "tier": 3},
    {"name": "Failure - Bad command", "command": "what is the weather", "tier": 1},
]

def run_evaluation():
    results = []
    passed_count = 0

    for test in TEST_CASES:
        print(f"Running test: {test['name']}...")
        start_time = time.time()
        
        # Execute the command using our parser
        output = main.parse_and_execute(test["command"])
        
        latency = time.time() - start_time # Metric 2: Latency [cite: 58]

        # Determine pass/fail status
        status = "FAIL"
        if "successfully" in output.lower():
            status = "PASS"
            passed_count += 1
        # For the intentional failure case
        if test["name"] == "Failure - Bad command" and "don't understand" in output:
            status = "PASS"
            passed_count += 1

        # Log results in the required format [cite: 51]
        results.append({
            "Test Name": test["name"],
            "Description": test["command"],
            "Status": status,
            "Error": "" if status == "PASS" else output,
            "Latency (s)": round(latency, 4)
        })

    # Calculate overall success rate
    pass_rate = (passed_count / len(TEST_CASES)) * 100
    print(f"\n--- Evaluation Complete ---")
    print(f"Pass Rate: {pass_rate:.2f}%")

    # Save results to a JSON file as required [cite: 50]
    with open("evaluation_log.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Results saved to evaluation_log.json")

if __name__ == "__main__":
    run_evaluation()