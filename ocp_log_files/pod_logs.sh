#!/bin/bash

# Output file
output_file="all_pod_logs.log"

# Get all namespaces
namespaces=$(oc get namespaces -o=jsonpath='{.items[*].metadata.name}')

# Loop through namespaces
for namespace in $namespaces; do
  echo "Getting logs for namespace: $namespace"

  # Get all pod names in the namespace
  pod_names=$(oc get pods -n $namespace -o=jsonpath='{.items[*].metadata.name}')

  # Loop through pods in the namespace
  for pod in $pod_names; do
    echo "Getting logs for pod: $pod in namespace: $namespace"
    
    # Get pod logs and append to the output file
    oc logs $pod -n $namespace >> $output_file
  done
done

echo "All pod logs have been collected and stored in $output_file"




# #!/bin/bash

# # Set the OpenShift project and pod name
# PROJECT_NAME="your_project_name"
# POD_NAME="your_pod_name"

# # Set the output file name
# OUTPUT_FILE="pod_logs.txt"

# # Loop through pod logs and append them to the output file
# while true; do
#     oc logs -f -n $PROJECT_NAME $POD_NAME >> $OUTPUT_FILE
#     sleep 1  # Adjust the sleep duration based on your requirements
# done




# #!/bin/bash

# # Get the current project or use the provided namespace
# PROJECT=${1:-$(oc project -q)}

# # Specify default output filename (relative to current location)
# OUTPUT="./all_pods_logs.txt"

# # Parse options
# while getopts ":n:fo:" opt; do
#   case $opt in
#     n) PROJECT="$OPTARG" ;;
#     f) FOLLOW="-f" ;;
#     o) OUTPUT="$OPTARG" ;;
#     \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
#   esac
# done

# # Get all pods in the project/namespace
# PODS=$(oc get pods -n "$PROJECT" -o jsonpath="{.items[*].metadata.name}")

# # Loop through each pod
# for pod in $PODS; do
#   # Get logs without timestamps for cleaner output
#   oc logs "$pod" -n "$PROJECT" $FOLLOW --no-timestamp >> "$OUTPUT"
#   echo "" >> "$OUTPUT" # Add empty line between pods
# done

# echo "Logs saved to: $OUTPUT"