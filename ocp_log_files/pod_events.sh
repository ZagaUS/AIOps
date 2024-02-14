#!/bin/bash

# Define the output file
output_file="openshift_pod_events-cluster.log"

# Get the list of namespaces starting with "openshift"
openshift_namespaces=$(oc get namespaces --no-headers | awk '$1 ~ /^openshift/ {print $1}')

# Loop through each namespace
for namespace in $openshift_namespaces; do
    echo "Fetching pod events for namespace: $namespace"
    
    # Get pod events and append them to the output file
    oc get events -n "$namespace" --field-selector involvedObject.kind=Pod >> "$output_file"
done

echo "Pod events for OpenShift namespaces have been collected and stored in: $output_file"