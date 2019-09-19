import fire
# Example:
# python sort.py bubble_sort [4,7,1,4]


class Sort(object):

    @staticmethod
    def bubble_sort(lst_in=[4, 3, 2, 0], print_result=True):
        """
            Bubble Sort Algorithm,
            Time Complexity: O(n^2)
            Space Complexity: O(1), because it sorts in-place
        """
        # ie: [4,3,2,0] last=3
        last = len(lst_in) - 1
        print('last:', last)
        # Iterate from 0 to 2
        for i in range(last):
            # Iterate from i+1 to 2
            for j in range(i + 1, last):
                if lst_in[i] > lst_in[j]:
                    # Swap current and next element
                    lst_in[i], lst_in[j] = lst_in[j], lst_in[i]

        if print_result:
            print(lst_in)
            return
        return lst_in


if __name__ == '__main__':
    fire.Fire(Sort)
