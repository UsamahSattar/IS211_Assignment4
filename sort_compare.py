import random
import time



def insertion_sort(a_list):
    """In-place insertion sort. Returns elapsed seconds."""
    
    lst = list(a_list)
    start = time.perf_counter()
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value
    end = time.perf_counter()
    return end - start


def shell_sort(a_list):
    """In-place shell sort. Returns elapsed seconds."""
    lst = list(a_list)
    start = time.perf_counter()
    gap = len(lst) // 2
    while gap > 0:
        for start_pos in range(gap):
            
            for i in range(start_pos + gap, len(lst), gap):
                current_value = lst[i]
                pos = i
                while pos >= gap and lst[pos - gap] > current_value:
                    lst[pos] = lst[pos - gap]
                    pos -= gap
                lst[pos] = current_value
        gap //= 2
    end = time.perf_counter()
    return end - start


def python_sort(a_list):
    """Wrapper around built-in Timsort."""
    lst = list(a_list)
    start = time.perf_counter()
    lst.sort()
    end = time.perf_counter()
    return end - start



def run_one_size(n, trials=100):
    """Return average times (insertion, shell, python) for lists of size n."""
    t_ins = t_shell = t_py = 0.0
    for _ in range(trials):
        lst = [random.randint(1, 1_000_000) for _ in range(n)]
        t_ins += insertion_sort(lst)
        t_shell += shell_sort(lst)
        t_py += python_sort(lst)
    return (t_ins / trials, t_shell / trials, t_py / trials)


def main():
    for n in (500, 1000, 5000):
        avg_ins, avg_shell, avg_py = run_one_size(n, trials=100)
        print(f"\nList size: {n}")
        print(f"Insertion Sort took {avg_ins:10.7f} seconds to run, on average")
        print(f"Shell Sort took    {avg_shell:10.7f} seconds to run, on average")
        print(f"Python Sort took   {avg_py:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()

