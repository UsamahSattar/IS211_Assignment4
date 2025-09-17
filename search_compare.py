import random
import time


TARGET = 99_999_999  



def sequential_search(a_list, item):
    """Unordered sequential search."""
    start = time.perf_counter()
    found = False
    for x in a_list:
        if x == item:
            found = True
            break
    end = time.perf_counter()
    return found, (end - start)


def ordered_sequential_search(a_list, item):
    """Sequential search on a sorted list (early stop when current > item)."""
    start = time.perf_counter()
    found = False
    for x in a_list:
        if x == item:
            found = True
            break
        if x > item:  
            break
    end = time.perf_counter()
    return found, (end - start)


def binary_search_iterative(a_list, item):
    """Iterative binary search on a sorted list."""
    start = time.perf_counter()
    low, high = 0, len(a_list) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if a_list[mid] == item:
            found = True
        elif item < a_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    end = time.perf_counter()
    return found, (end - start)


def _binary_search_recursive_core(a_list, item, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if a_list[mid] == item:
        return True
    if item < a_list[mid]:
        return _binary_search_recursive_core(a_list, item, low, mid - 1)
    else:
        return _binary_search_recursive_core(a_list, item, mid + 1, high)


def binary_search_recursive(a_list, item):
    """Recursive binary search on a sorted list."""
    start = time.perf_counter()
    found = _binary_search_recursive_core(a_list, item, 0, len(a_list) - 1)
    end = time.perf_counter()
    return found, (end - start)



def run_one_size(n, trials=100):
    """Return average times for each algorithm over `trials` random lists of size `n`."""
    t_seq = t_ord = t_bin_it = t_bin_rec = 0.0

    for _ in range(trials):
        lst = [random.randint(1, 1_000_000) for _ in range(n)]

        
        _, dt = sequential_search(lst, TARGET)
        t_seq += dt

        
        sorted_lst = sorted(lst)

        _, dt = ordered_sequential_search(sorted_lst, TARGET)
        t_ord += dt

        _, dt = binary_search_iterative(sorted_lst, TARGET)
        t_bin_it += dt

        _, dt = binary_search_recursive(sorted_lst, TARGET)
        t_bin_rec += dt

    return (t_seq / trials, t_ord / trials, t_bin_it / trials, t_bin_rec / trials)


def main():
    for n in (500, 1000, 5000):
        avg_seq, avg_ord, avg_bin_it, avg_bin_rec = run_one_size(n, trials=100)
        print(f"\nList size: {n}")
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {avg_ord:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {avg_bin_it:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {avg_bin_rec:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
