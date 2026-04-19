def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    # Output
    print("Process\tSize\tBlock")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"P{i+1}\t{processes[i]}\t{allocation[i]+1}")
        else:
            print(f"P{i+1}\t{processes[i]}\tNot Allocated")


# MAIN
blocks = list(map(int, input("Enter block sizes: ").split()))
processes = list(map(int, input("Enter process sizes: ").split()))

first_fit(blocks, processes)