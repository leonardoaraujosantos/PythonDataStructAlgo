import fire
# Example:
# python fibonnaci.py iterative 8
# python fibonnaci.py recursive 8


class Fibonnaci(object):

    @staticmethod
    def iterative(n=3, print_result=True):
        fibs = [0, 1]
        if n < 1:
            fibs = fibs[0:n + 1]
        for f in range(1, n):
            fibs.append(fibs[-1] + fibs[-2])

        if print_result:
            print(fibs)
            return
        return fibs

    @staticmethod
    def recursive(n):
        if n < 2:
            return n
        return Fibonnaci.recursive(n - 1) + Fibonnaci.recursive(n - 2)


if __name__ == '__main__':
    fire.Fire(Fibonnaci)
