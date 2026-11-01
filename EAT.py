
tlb_time = 10
memory_time = 80

h = 0.90

# Calculate EAT for TLB hit ratio 0.90
eat1 = h * (tlb_time + memory_time) + (1 - h) * (tlb_time + 2 * memory_time)

print("TLB Hit Ratio:", h)
print("TLB Lookup Time:", tlb_time, "ns")
print("Main Memory Access Time:", memory_time, "ns")
print("Effective Access Time:", eat1, "ns")

# Calculate EAT for TLB hit ratio 0.75
h = 0.75

eat2 = h * (tlb_time + memory_time) + (1 - h) * (tlb_time + 2 * memory_time)

print("\nTLB Hit Ratio:", h)
print("Effective Access Time:", eat2, "ns")

# Compare both results
print("\nComparison:")
if eat1 < eat2:
    print("TLB hit ratio 0.90 gives better performance.")
else:
    print("TLB hit ratio 0.75 gives better performance.")
